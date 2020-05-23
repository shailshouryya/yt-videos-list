import functools
import platform
import time
import csv
import os

from .notifications import Common as common_message


if platform.system().lower().startswith('windows'): NEWLINE = '\r\n'
else:                                               NEWLINE = '\n'

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
        temp_file  = 'yt_videos_list_temp'
        temp_file  = f'{temp_file}.{extension}'
        print(f'Opened {temp_file}, writing video information to file....')

        # check name of file and number of videos written
        filename, videos_written = writer_function(*args, **kwargs)
        filename = f'{filename}.{extension}'

        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f'Finished writing to {temp_file}')
        print(f'{videos_written} videos written to {temp_file}')
        print(f'Closing {temp_file}')
        print(f'Successfully completed write, renamed {temp_file} to {filename}')
        print(f'It took {total_time} to write all {videos_written} videos to {filename}{NEWLINE}')
    return wrapper_timer


@time_writer_function
def write_to_txt(list_of_videos, file_name, chronological):
    with open('yt_videos_list_temp.txt', 'x') as txt_file:
        spacing = f'{NEWLINE}' + ' '*4

        for video_number, selenium_element in enumerate(list_of_videos, 1) if chronological is False else enumerate(list_of_videos[::-1], 1):
            txt_file.write(f'Video Number: {video_number}{NEWLINE}')
            txt_file.write(f'Video Title:  {selenium_element.get_attribute("title")}{NEWLINE}')
            txt_file.write(f'Video URL:    {selenium_element.get_attribute("href")}{NEWLINE}')
            txt_file.write(f'Watched?{spacing}{NEWLINE}')
            txt_file.write(f'Watch again later?{spacing}{NEWLINE}')
            txt_file.write(f'Notes:{spacing}{NEWLINE}')
            txt_file.write('*'*75 + NEWLINE)
            if video_number % 250 == 0:
                print(f'{video_number} videos written to {txt_file.name}...')
    os.rename('yt_videos_list_temp.txt', f'{file_name}.txt')
    return file_name, video_number


@time_writer_function
def save_to_mem_write_to_txt(list_of_videos, file_name, chronological):
    # this takes a little bit longer than the write_to_txt() function
    with open('yt_videos_list_temp.txt', 'x') as memory_file:
        text = ''
        spacing = NEWLINE + ' '*4

        for video_number, selenium_element in enumerate(list_of_videos, 1) if chronological is False else enumerate(list_of_videos[::-1], 1):
            text += f'Video Number: {video_number}{NEWLINE}'
            text += f'Video Title:  {selenium_element.get_attribute("title")}{NEWLINE}'
            text += f'Video URL:    {selenium_element.get_attribute("href")}{NEWLINE}'
            text += f'Watched?{spacing}{NEWLINE}'
            text += f'Watch again later?{spacing}{NEWLINE}'
            text += f'Notes:{spacing}{NEWLINE}'
            text += '*'*75 + NEWLINE
            if video_number % 250 == 0:
                print(f'{video_number} videos saved to memory...')
        print(f'Finished saving video information to memory')
        memory_file.write(text)
    os.rename('yt_videos_list_temp.txt', f'{file_name}.txt')
    return file_name, video_number


@time_writer_function
def write_to_csv(list_of_videos, file_name, chronological):
    with open('yt_videos_list_temp.csv', 'x') as csv_file:
        fieldnames = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for video_number, selenium_element in enumerate(list_of_videos, 1) if chronological is False else enumerate(list_of_videos[::-1], 1):
            writer.writerow(
                {'Video Number': f'{video_number}', 'Video Title': f'{selenium_element.get_attribute("title")}', 'Video URL': f'{selenium_element.get_attribute("href")}', 'Watched?': '', 'Watch again later?': '', 'Notes': ''}
                )
            if video_number % 250 == 0:
                print(f'{video_number} videos written to {csv_file.name}...')
    os.rename('yt_videos_list_temp.csv', f'{file_name}.csv')
    return file_name, video_number
