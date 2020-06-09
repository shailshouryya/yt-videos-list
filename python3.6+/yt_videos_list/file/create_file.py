import functools
import time
import csv
import os

from . import write
from ..notifications import Common as common_message


NEWLINE = '\n'


def scroll_down(current_elements_count, driver, scroll_pause_time):
    driver.execute_script('window.scrollBy(0, 50000);')
    time.sleep(scroll_pause_time)
    new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    print(f'Found {new_elements_count} videos...')
    if new_elements_count == current_elements_count:
        # wait scroll_pause_time seconds and check again to verify you really did reach the end of the page, and there wasn't a buffer loading period
        print(common_message.no_new_videos_found)
        time.sleep(scroll_pause_time)
        new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
        if new_elements_count == current_elements_count:
            print('Reached end of page!')
    return new_elements_count


def save_elements_to_list(driver, start_time, scroll_pause_time, url):
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end_time = time.perf_counter()
    total_time = end_time - start_time - scroll_pause_time # subtract scroll_pause_time to account for the extra waiting time to verify end of page
    print(f'It took {total_time} seconds to find all {len(elements)} videos from {url}{NEWLINE}')
    return elements


def scroll_to_bottom(url, driver, scroll_pause_time):
    driver.set_window_size(780, 880)
    start_time = time.perf_counter() # timer stops in save_elements_to_list() function
    driver.get(url)

    current_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    while True:
        new_elements_count = scroll_down(current_elements_count, driver, scroll_pause_time)
        if new_elements_count == current_elements_count:
            break
        else:
            current_elements_count = new_elements_count
    return save_elements_to_list(driver, start_time, scroll_pause_time, url)


def time_writer_function(writer_function):
    @functools.wraps(writer_function)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        extension  = writer_function.__name__.split('_')[-1]
        temp_file  = f'yt_videos_list_temp.{extension}'
        print(f'Opened {temp_file}, writing video information to file....')

        # check name of file and number of videos written
        file_name, videos_written = writer_function(*args, **kwargs)
        file_name = f'{file_name}.{extension}'
        os.replace(temp_file, file_name)

        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f'Finished writing to {temp_file}')
        print(f'{videos_written} videos written to {temp_file}')
        print(f'Closing {temp_file}')
        print(f'Successfully completed write, renamed {temp_file} to {file_name}')
        print(f'It took {total_time} to write all {videos_written} videos to {file_name}{NEWLINE}')
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


@time_writer_function
def write_to_txt(list_of_videos, file_name, reverse_chronological):
    total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
    with open('yt_videos_list_temp.txt', 'w') as txt_file:
        spacing = f'{NEWLINE}' + ' '*4

        for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
            video_number, total_writes = write.txt_entry(txt_file, selenium_element, NEWLINE, spacing, video_number, incrementer, total_writes)
            if total_writes % 250 == 0:
                print(f'{total_writes} videos written to {txt_file.name}...')
    return file_name, total_videos


@time_writer_function
def save_to_mem_write_to_txt(list_of_videos, file_name, reverse_chronological):
    # this takes a little bit longer than the write_to_txt() function
    total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
    with open('yt_videos_list_temp.txt', 'w') as memory_file:
        text = ''
        spacing = NEWLINE + ' '*4

        for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
            text += f'Video Number: {video_number}{NEWLINE}'
            text += f'Video Title:  {selenium_element.get_attribute("title")}{NEWLINE}'
            text += f'Video URL:    {selenium_element.get_attribute("href")}{NEWLINE}'
            text += f'Watched?{spacing}{NEWLINE}'
            text += f'Watch again later?{spacing}{NEWLINE}'
            text += f'Notes:{spacing}{NEWLINE}'
            text += '*'*75 + NEWLINE
            video_number += incrementer
            total_writes += 1
            if total_writes % 250 == 0:
                print(f'{total_writes} videos saved to memory...')
        print(f'Finished saving video information to memory')
        memory_file.write(text)
    return file_name, total_videos


@time_writer_function
def write_to_csv(list_of_videos, file_name, reverse_chronological):
    total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
    with open('yt_videos_list_temp.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
            video_number, total_writes = write.csv_entry(writer, selenium_element, video_number, incrementer, total_writes)
            if total_writes % 250 == 0:
                print(f'{total_writes} videos written to {csv_file.name}...')
    return file_name, total_videos
