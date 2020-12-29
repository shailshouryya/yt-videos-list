import functools
import time
import csv
import os
from .      import write
from ..notifications import Common as common_message
from ..custom_logger import log
NEWLINE = '\n'
def scroll_down(current_elements_count, driver, scroll_pause_time, logging_output_location):
 driver.execute_script('window.scrollBy(0, 50000);')
 time.sleep(scroll_pause_time)
 new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
 log(f'Found {new_elements_count} videos...', logging_output_location)
 if new_elements_count == current_elements_count:
  log(common_message.no_new_videos_found(scroll_pause_time * 2), logging_output_location)
  time.sleep(scroll_pause_time * 2)
  new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
  if new_elements_count == current_elements_count:
   log(f'Reached end of page!', logging_output_location)
 return new_elements_count
def save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_output_location):
 elements   = driver.find_elements_by_xpath('//*[@id="video-title"]')
 end_time   = time.perf_counter()
 total_time = end_time - start_time - scroll_pause_time
 log(f'It took {total_time} seconds to find all {len(elements)} videos from {url}{NEWLINE}', logging_output_location)
 return elements
def scroll_to_bottom(url, driver, scroll_pause_time, logging_output_location):
 start_time = time.perf_counter()
 driver.get(url)
 current_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
 while True:
  new_elements_count = scroll_down(current_elements_count, driver, scroll_pause_time, logging_output_location)
  if new_elements_count == current_elements_count:
   break
  else:
   current_elements_count = new_elements_count
 return save_elements_to_list(driver, start_time, scroll_pause_time, url, logging_output_location)
def time_writer_function(writer_function):
 @functools.wraps(writer_function)
 def wrapper_timer(*args, **kwargs):
  start_time    = time.perf_counter()
  extension     = writer_function.__name__.split('_')[-1]
  timestamp     = kwargs.get('timestamp', 'undeteremined_start_time')
  file_name, videos_written, logging_output_location = writer_function(*args, **kwargs)
  log(f'Opening a temp {extension} file and writing video information to the file....', logging_output_location)
  end_time      = time.perf_counter()
  total_time    = end_time - start_time
  temp_file     = f'temp_{file_name}_{timestamp}.{extension}'
  final_file    = f'{file_name}.{extension}'
  log(f'Finished writing to'.ljust(66) + f'{temp_file}', logging_output_location)
  log(f'{videos_written} videos written to'.ljust(66) + f'{temp_file}', logging_output_location)
  log(f'Closing'.ljust(66) + f'{temp_file}', logging_output_location)
  os.replace(temp_file, final_file)
  log(f'Successfully completed write, renamed {temp_file} to {final_file}', logging_output_location)
  log(f'It took {total_time} seconds to write all {videos_written} videos to {final_file}{NEWLINE}', logging_output_location)
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
def txt_writer(file, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes, logging_output_location):
 for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
  video_number, total_writes = write.txt_entry(file, markdown_formatting, selenium_element, NEWLINE, spacing, video_number, incrementer, total_writes)
  if total_writes % 250 == 0:
   log(f'{total_writes} videos written to {file.name}...', logging_output_location)
@time_writer_function
def write_to_txt(list_of_videos, file_name, reverse_chronological, logging_output_location, timestamp):
 total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
 markdown_formatting           = False
 spacing              = f'{NEWLINE}' + ' '*4
 with open(f'temp_{file_name}_{timestamp}.txt', 'w', encoding='utf-8') as txt_file:
  txt_writer(txt_file, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes, logging_output_location)
 return file_name, total_videos, logging_output_location
@time_writer_function
def write_to_md(list_of_videos, file_name, reverse_chronological, logging_output_location, timestamp):
 total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
 markdown_formatting           = True
 spacing              = f'{NEWLINE}' + '- ' + f'{NEWLINE}'
 with open(f'temp_{file_name}_{timestamp}.md', 'w', encoding='utf-8') as md_file:
  txt_writer(md_file, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes, logging_output_location)
 return file_name, total_videos, logging_output_location
@time_writer_function
def write_to_csv(list_of_videos, file_name, reverse_chronological, logging_output_location, timestamp):
 total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
 with open(f'temp_{file_name}_{timestamp}.csv', 'w', newline='', encoding='utf-8') as csv_file:
  fieldnames = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
  writer  = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
   video_number, total_writes = write.csv_entry(writer, selenium_element, video_number, incrementer, total_writes)
   if total_writes % 250 == 0:
    log(f'{total_writes} videos written to {csv_file.name}...', logging_output_location)
 return file_name, total_videos, logging_output_location
