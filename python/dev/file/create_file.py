import functools
import time
import csv

from .               import write
from ..notifications import Common as common_message
from ..custom_logger import log, log_extraction_information


def scroll_down(current_elements_count, driver, scroll_pause_time, logging_locations):
    driver.execute_script('window.scrollBy(0, 50000);')
    time.sleep(scroll_pause_time)
    new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    log(f'Found {new_elements_count} videos...', logging_locations)
    if new_elements_count == current_elements_count:
        # wait scroll_pause_time seconds and check again to verify you really did reach the end of the page, and there wasn't a buffer loading period
        log(common_message.no_new_videos_found(scroll_pause_time * 2), logging_locations)
        time.sleep(scroll_pause_time * 2)
        new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
        if new_elements_count == current_elements_count:
            log(f'Reached end of page!', logging_locations)
    return new_elements_count


def save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_locations):
    elements   = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end_time   = time.perf_counter()
    total_time = end_time - start_time - scroll_pause_time # subtract scroll_pause_time to account for the extra waiting time to verify end of page
    log(f'It took {total_time} seconds to find all {len(elements)} videos from {url}\n', logging_locations)
    return elements


def scroll_to_bottom(url, driver, scroll_pause_time, logging_locations):
    start_time = time.perf_counter() # timer stops in save_elements_to_list() function
    driver.get(url)
    current_elements_count = None
    new_elements_count     = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    while new_elements_count != current_elements_count:
        current_elements_count = new_elements_count
        new_elements_count     = scroll_down(current_elements_count, driver, scroll_pause_time, logging_locations)
    return save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_locations)


def time_writer_function(writer_function):
    @functools.wraps(writer_function)
    def wrapper_timer(*args, **kwargs):
        log_extraction_information(__name__, writer_function, args, kwargs)
    return wrapper_timer


def prepare_output(list_of_videos, reverse_chronological):
    total_videos = len(list_of_videos)
    total_writes = 0
    if reverse_chronological:
        video_number = total_videos
        incrementer  = -1
    else:
        video_number = 1
        incrementer  = 1
    return total_videos, total_writes, video_number, incrementer


def txt_writer(file_type, file, csv_writer, reverse_chronological, list_of_videos, logging_locations):
    total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
    for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
        video_number, total_writes = write.entry(file_type, file, csv_writer, selenium_element, video_number, incrementer, total_writes)
        if total_writes % 250 == 0:
            log(f'{total_writes} videos written to {file.name}...', logging_locations)
    return total_videos

@time_writer_function
def write_to(file_type, list_of_videos, file_name, reverse_chronological, logging_locations, timestamp):
    if file_type == 'csv': newline = ''
    else:                  newline = None
    csv_writer = None
    with open(f'temp_{file_name}_{timestamp}.{file_type}', 'w', newline=newline, encoding='utf-8') as temp_file:
        if file_type == 'csv':
            fieldnames = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
            csv_writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        total_videos = txt_writer(file_type, temp_file, csv_writer, reverse_chronological, list_of_videos, logging_locations)
    return file_name, total_videos, reverse_chronological, logging_locations
