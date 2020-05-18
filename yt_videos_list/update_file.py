import functools
import platform
import sys
import time
import csv
import re

from .notifications import Common as common_message


if platform.system().lower().startswith('windows'): NEWLINE = '\r\n'
else:                                               NEWLINE = '\n'


def store_already_written_videos(file_name, file_type):
    with open(f'{file_name}.{file_type}') as file:
        if file_type == 'txt': return set(re.findall(r'(https://www\.youtube\.com/watch\?v=.+?)(?:\s|\n)', file.read()))
        if file_type == 'csv': return set(re.findall(r'(https://www\.youtube\.com/watch\?v=.+?),', file.read()))

def scroll_down(driver, scroll_pause_time):
    driver.execute_script('window.scrollBy(0, 50000);')
    time.sleep(scroll_pause_time)
    if driver.find_elements_by_xpath('//*[@id="video-title"]')[-1].get_attribute("href") in VISITED_VIDEOS:
        return True
    return False

def save_elements_to_list(driver, start_time, scroll_pause_time, url):
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end_time = time.perf_counter()
    total_time = end_time - start_time - scroll_pause_time # subtract scroll_pause_time to account for the extra waiting time to verify end of page
    print(f'It took {total_time} seconds to find {len(elements)} videos from {url}{NEWLINE}')
    return elements

def scroll_to_old_videos(url, driver, scroll_pause_time, txt_exists, csv_exists, file_name):
    global VISITED_VIDEOS
    driver.set_window_size(780, 880)
    stored_in_txt = None
    stored_in_csv = None
    if txt_exists: stored_in_txt = store_already_written_videos(file_name, 'txt')
    if csv_exists: stored_in_csv = store_already_written_videos(file_name, 'csv')
    if stored_in_txt and stored_in_csv: VISITED_VIDEOS = stored_in_txt.intersection(stored_in_csv) # same as stored_in_txt & stored_in_csv
    else:                               VISITED_VIDEOS = stored_in_txt or stored_in_csv            # takes values from whichever file exists
    print(f'Detected an existing file with the name {file_name} in this directory, checking for new videos to update {file_name}....')
    start_time = time.perf_counter() # timer stops in save_elements_to_list() function

    found_old_videos = False
    while found_old_videos is False:
        found_old_videos = scroll_down(driver, scroll_pause_time)
    return save_elements_to_list(driver, start_time, scroll_pause_time, url)


def time_writer_function(writer_function):
    @functools.wraps(writer_function)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

def write_to_txt(videos_list, file_name, chronological):
    # if file_name.txt is chronological, start at the end of the list
    # ignore all videos that are already in the file
    # add new videos to list until first element is reached
    # then take the contents of the original file and write it to a temp file
    # and append new videos to end of temp file before renaming temp file to file_name.txt (overwrites original file)
    # otherwise start at the beginning of the list and continue adding videos to the list until a video that is already in the list is reached
    # then break out of the loop
    # then take the new videos and add it to a temp file
    # and append contents of the original file to the end of temp file before renaming temp file to file_name.txt (overwrites original file)
    pass

def write_to_csv(videos_list, file_name, chronological):
    # if file_name.csv is chronological, start at the end of the list
    # ignore all videos that are already in the file
    # add new videos to list until first element is reached
    # then take the contents of the original file and write it to a temp file
    # and append new videos to end of temp file before renaming temp file to file_name.csv (overwrites original file)
    # otherwise start at the beginning of the list and continue adding videos to the list until a video that is already in the list is reached
    # then break out of the loop
    # then take the new videos and add it to a temp file
    # and append contents of the original file to the end of temp file before renaming temp file to file_name.csv (overwrites original file)
    pass
