import functools
import time
import csv
import re

from .               import write
from ..custom_logger import log, log_extraction_information

NEWLINE = '\n'


def store_already_written_videos(file_name, file_type):
    with open(f'{file_name}.{file_type}', 'r', encoding='utf-8') as file:
        if file_type == 'txt' or file_type == 'md': return set(re.findall('(https://www\.youtube\.com/watch\?v=.+?)(?:\s|\n)', file.read()))
        if file_type == 'csv':                      return set(re.findall('(https://www\.youtube\.com/watch\?v=.+?),',         file.read()))

def scroll_down(driver, scroll_pause_time, visited_videos, logging_locations):
    driver.execute_script('window.scrollBy(0, 50000);')
    time.sleep(scroll_pause_time * 2)
    new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    log(f'Found {new_elements_count} videos...', logging_locations)
    if driver.find_elements_by_xpath('//*[@id="video-title"]')[-1].get_attribute('href') in visited_videos:
        return True
    return False

def save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_locations):
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end_time = time.perf_counter()
    total_time = end_time - start_time - scroll_pause_time # subtract scroll_pause_time to account for the extra waiting time to verify end of page
    log(f'It took {total_time} seconds to find {len(elements)} videos from {url}{NEWLINE}', logging_locations)
    return elements

def scroll_to_old_videos(url, driver, scroll_pause_time, logging_locations, file_name, txt_exists, csv_exists, md_exists):
    stored_in_txt = store_already_written_videos(file_name, 'txt') if txt_exists else set()
    stored_in_csv = store_already_written_videos(file_name, 'csv') if csv_exists else set()
    stored_in_md  = store_already_written_videos(file_name, 'md' ) if md_exists  else set()
    existing_videos = []
    if stored_in_txt: existing_videos.append(stored_in_txt)
    if stored_in_csv: existing_videos.append(stored_in_csv)
    if stored_in_md:  existing_videos.append(stored_in_md)
    if   len(existing_videos) == 3: visited_videos = existing_videos[0].intersection(existing_videos[1]).intersection(existing_videos[2]) # find videos that exist in all 3 files           # same as stored_in_txt & stored_in_csv & stored_in_md #
    elif len(existing_videos) == 2: visited_videos = existing_videos[0].intersection(existing_videos[1])                                  # find videos that exist in the 2 files the program is updating
    else:                           visited_videos = existing_videos[0]                                                                   # take all videos  from the     1 file  the program is updating
    log(f'Detected an existing file with the name {file_name} in this directory, checking for new videos to update {file_name}....', logging_locations)
    start_time       = time.perf_counter() # timer stops in save_elements_to_list() function
    found_old_videos = False
    while found_old_videos is False:
        found_old_videos = scroll_down(driver, scroll_pause_time, visited_videos, logging_locations)
    return save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_locations), stored_in_txt, stored_in_csv, stored_in_md


def time_writer_function(writer_function):
    @functools.wraps(writer_function)
    def wrapper_timer(*args, **kwargs):
        log_extraction_information(__name__, writer_function, args, kwargs)
    return wrapper_timer


def find_number_of_new_videos(list_of_videos, videos_set):
    visited_on_page = {selenium_element.get_attribute('href') for selenium_element in list_of_videos}
    return len(visited_on_page.difference(videos_set))                                            # same as len(visited_on_page - visited_videos)


def prepare_output(list_of_videos, videos_set, video_number, reverse_chronological):
    new_videos = find_number_of_new_videos(list_of_videos, videos_set)
    total_writes = 0
    if reverse_chronological:
        video_number += new_videos
        incrementer   = -1
    else:
        video_number += 1
        incrementer   = 1
    return video_number, new_videos, total_writes, incrementer



def update_file(file_type, new_file, old_file, csv_writer, visited_videos, reverse_chronological, list_of_videos, video_number, logging_locations):
    formatting = {
        # file_type: (markdown_formatting, spacing)
        'txt': (False, f'{NEWLINE}' + ' '*4),
        'md' : (True,  f'{NEWLINE}' + '- ' + f'{NEWLINE}'),
        'csv': (None,  None)
    }
    video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, visited_videos, video_number, reverse_chronological)
    markdown_formatting, spacing                        = formatting[file_type]
    for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
        if selenium_element.get_attribute('href') in visited_videos: continue
        else:
            video_number, total_writes = write.entry(file_type, new_file, csv_writer, markdown_formatting, selenium_element, NEWLINE, spacing, video_number, incrementer, total_writes)
            if total_writes % 250 == 0:
                log(f'{total_writes} new videos written to {new_file.name}...', logging_locations)
    if reverse_chronological:
        old_file.seek(0)
        if file_type == 'csv': old_file.readline() # skip the header since that's already written at the top of temp file
        for line in old_file:  new_file.write(line)
    else:
        new_file.seek(0)
        for line in new_file: old_file.write(line)
    return new_videos


# if reverse_chronological is True, start at the end of the selenium elements list and ignore all videos that are already in the file
# add new videos to temp file until first element is reached
# then append new videos to end of old file - make sure to remove temp file!
# otherwise start at the beginning of the list and continue adding videos to the temp file until a video that is already in the list is reached
# ignore all videos that are already in the original file
# then take the contents of the original file and append it to the end of the temp file before renaming temp file to file_name.txt (overwrites original file)

@time_writer_function
def write_to(file_type, list_of_videos, file_name, reverse_chronological, logging_locations, timestamp, stored_in_file):
    if stored_in_file is None: stored_in_file = store_already_written_videos(file_name, file_type)
    if file_type == 'csv': newline = ''
    else:                  newline = None
    with open(f'{file_name}.{file_type}', 'r+', newline=newline, encoding='utf-8') as old_file, open(f'temp_{file_name}_{timestamp}.{file_type}', 'w+', newline=newline, encoding='utf-8') as temp_file:
        if file_type == 'csv':
            video_number = int(max(re.findall('^(\d+)?,', old_file.read(), re.M), key = lambda i: int(i)))
            fieldnames   = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
            csv_writer       = csv.DictWriter(temp_file, fieldnames=fieldnames)
            if reverse_chronological: csv_writer.writeheader()
        else:
            video_number = int(max(re.findall('^Video Number:\s*(\d+)', old_file.read(), re.M), key = lambda i: int(i)))
            csv_writer   = None
        ####### defer to update_file() function to update file with new videos #######
        new_videos = update_file(file_type, temp_file, old_file, csv_writer, stored_in_file, reverse_chronological, list_of_videos, video_number, logging_locations)
    return file_name, new_videos, reverse_chronological, logging_locations
