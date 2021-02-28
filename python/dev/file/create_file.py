import time

from ..notifications import Common as common_message
from ..custom_logger import log

def scroll_to_bottom(url, driver, scroll_pause_time, logging_locations):
    start_time = time.perf_counter() # timer stops in save_elements_to_list() function
    driver.get(url)
    current_elements_count = None
    new_elements_count     = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    while new_elements_count != current_elements_count:
        current_elements_count = new_elements_count
        new_elements_count     = scroll_down(current_elements_count, driver, scroll_pause_time, logging_locations)
    return save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_locations)


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
