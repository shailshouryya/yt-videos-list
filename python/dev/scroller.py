import re
import time

from .custom_logger import log


def scroll_until_break(url, driver, scroll_pause_time, logging_locations, verify_page_bottom_n_times, force_to_page_bottom, file_name, txt_exists, csv_exists, md_exists):
    visited_videos, stored_in_txt, stored_in_csv, stored_in_md = determine_common_visited_videos(file_name, txt_exists, csv_exists, md_exists)
    if force_to_page_bottom: visited_videos.clear()                                  # clear any pre-existing video information if there are pre-existing files (will already be empty if there are no pre-existing files)
    else:                    verify_page_bottom_n_times       *= 3                   # it is VERY unlikely that a pre-existing file exists and the program reaches the end of the page before finding ANY pre-existing vides, so increase value for break condition by 3 to make sure this is actually the case and not a false positive
    scrolling_cpu_start_time                                   = time.perf_counter() # timer stops in save_elements_to_list() function
    start_real_time                                            = time.time()         # this timer also stops in save_elements_to_list() function
    current_elements_count                                     = None
    new_elements_count                                         = count_videos_on_page(driver)
    num_times_elements_count_same                              = -1
    found_old_videos                                           = False
    url_of_last_loaded_video_on_page                           = lambda: driver.find_elements_by_xpath('//*[@id="video-title"]')[-1].get_attribute('href').replace('shorts/', 'watch?v=').split('&pp')[0]
    if new_elements_count != 0:
        # ensure page has videos, otherwise url_of_last_loaded_video_on_page() breaks because indexing is not possible on an empty array
        while found_old_videos is False and num_times_elements_count_same < verify_page_bottom_n_times:
            current_elements_count = new_elements_count
            scroll_down(driver, scroll_pause_time, logging_locations)
            new_elements_count   = count_videos_on_page(driver)
            num_times_elements_count_same = verify_reached_page_bottom(new_elements_count, current_elements_count, num_times_elements_count_same, verify_page_bottom_n_times, logging_locations)
            if url_of_last_loaded_video_on_page() in visited_videos:
                # if force_to_page_bottom is True, visited_videos will be an empty set and this conditional will never execute
                found_old_videos = True
    return save_elements_to_list(driver, scrolling_cpu_start_time, start_real_time, url, logging_locations), stored_in_txt, stored_in_csv, stored_in_md, visited_videos



def determine_common_visited_videos(file_name, txt_exists, csv_exists, md_exists):
    stored_in_txt = store_already_written_videos(file_name, 'txt') if txt_exists else set()
    stored_in_csv = store_already_written_videos(file_name, 'csv') if csv_exists else set()
    stored_in_md  = store_already_written_videos(file_name, 'md' ) if md_exists  else set()
    existing_videos = []
    if stored_in_txt: existing_videos.append(stored_in_txt)
    if stored_in_csv: existing_videos.append(stored_in_csv)
    if stored_in_md:  existing_videos.append(stored_in_md)
    if   len(existing_videos) == 3: visited_videos = existing_videos[0].intersection(existing_videos[1]).intersection(existing_videos[2]) # find videos that exist in all 3 files                            # same as stored_in_txt & stored_in_csv & stored_in_md #
    elif len(existing_videos) == 2: visited_videos = existing_videos[0].intersection(existing_videos[1])                                  # find videos that exist in the 2 files the program is updating    # same as stored_in_txt & stored_in_csv #
    elif len(existing_videos) == 1: visited_videos = existing_videos[0]                                                                   # take all videos  from the     1 file  the program is updating    # same as stored_in_txt #
    else:                           visited_videos = set()                                                                                # there are no pre-existing videos #
    return visited_videos, stored_in_txt, stored_in_csv, stored_in_md

def store_already_written_videos(file_name, file_type):
    with open(f'{file_name}.{file_type}', mode='r', encoding='utf-8') as file:
        file_contents = file.read()
        if file_type in ('txt', 'md'):
            seen_videos = set(
                re.findall('^(?:### )?Video URL:\s*(https://www\.youtube\.com/watch\?v=.+?)(?:\s|\n)', file_contents, flags=re.MULTILINE) or
                re.findall('^(?:### )?Video ID:\s*([A-z0-9_-]{11})$',                                  file_contents, flags=re.MULTILINE)
            )
        if file_type == 'csv':
            seen_videos = set(
                re.findall(',(https://www\.youtube\.com/watch\?v=.+?),',        file_contents) or
                re.findall(',([A-z0-9_-]{11}),',                                file_contents)
            )
        if seen_videos:
            # the set exists
            # check to see if the entire video URL was stored or just the video ID
            random_video = seen_videos.pop()
            if 'https://www.youtube.com/watch?v=' not in random_video:
                # this file stored only the video IDs, so add the rest of the URL to
                # the video ID so url_of_last_loaded_video_on_page() lambda function in
                # scroll_until_break() can match the 'href' of the videos properly
                formatted_urls = set()
                random_video = 'https://www.youtube.com/watch?v=' + random_video
                formatted_urls.add(random_video)
                while seen_videos:
                    random_video = seen_videos.pop()
                    random_video = 'https://www.youtube.com/watch?v=' + random_video
                    formatted_urls.add(random_video)
                seen_videos = formatted_urls
            else:
                # this file stored the entire video URL, so no need to modify any of the URLs
                # just add the popped random_video back into the seen_videos set
                seen_videos.add(random_video)
        return seen_videos



def count_videos_on_page(driver):
    return driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')

def scroll_down(driver, scroll_pause_time, logging_locations):
    driver.execute_script('window.scrollBy(0, 50000);')
    time.sleep(scroll_pause_time)
    new_elements_count = count_videos_on_page(driver)
    log(f'Found {new_elements_count} videos...', logging_locations)

def verify_reached_page_bottom(new_elements_count, current_elements_count, num_times_elements_count_same, verify_page_bottom_n_times, logging_locations):
    if new_elements_count == current_elements_count:
        num_times_elements_count_same += 1
        times = 'time' if num_times_elements_count_same == 1 else 'times'
        log(f'Found {new_elements_count} videos. Verified this is the page bottom {num_times_elements_count_same} {times}. Need to verify {verify_page_bottom_n_times} {times} before writing to file...', logging_locations)
        if num_times_elements_count_same == verify_page_bottom_n_times:
            log('Reached end of page!', logging_locations)
    else:
        num_times_elements_count_same = -1
    return num_times_elements_count_same

def save_elements_to_list(driver, scrolling_cpu_start_time, start_real_time, url, logging_locations):
    elements   = driver.find_elements_by_xpath('//*[@id="video-title"]')
    scrolling_cpu_end_time   = time.perf_counter()
    end_real_time = time.time()
    scrolling_cpu_time = scrolling_cpu_end_time - scrolling_cpu_start_time
    total_real_time = end_real_time - start_real_time
    log(f'It took {scrolling_cpu_time} seconds ({total_real_time} seconds real time)) to find {len(elements)} videos from {url}\n', logging_locations)
    return elements
