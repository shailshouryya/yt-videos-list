import functools
import time
import csv
import re
from .      import write
from ..custom_logger import log, log_extraction_information
NEWLINE = '\n'
def store_already_written_videos(file_name, file_type):
 with open(f'{file_name}.{file_type}', 'r', encoding='utf-8') as file:
  if file_type == 'txt' or file_type == 'md': return set(re.findall('(https://www\.youtube\.com/watch\?v=.+?)(?:\s|\n)', file.read()))
  if file_type == 'csv':       return set(re.findall('(https://www\.youtube\.com/watch\?v=.+?),', file.read()))
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
 total_time = end_time - start_time - scroll_pause_time
 log(f'It took {total_time} seconds to find {len(elements)} videos from {url}{NEWLINE}', logging_locations)
 return elements
def scroll_to_old_videos(url, driver, scroll_pause_time, file_name, logging_locations):
 stored_in_txt = store_already_written_videos(file_name, 'txt')
 stored_in_csv = store_already_written_videos(file_name, 'csv')
 stored_in_md =  store_already_written_videos(file_name, 'md' )
 visited_videos = stored_in_txt.intersection(stored_in_csv).intersection(stored_in_md)
 log(f'Detected an existing file with the name {file_name} in this directory, checking for new videos to update {file_name}....', logging_locations)
 start_time    = time.perf_counter()
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
 return len(visited_on_page.difference(videos_set))
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
def txt_writer(new_file, old_file, visited_videos, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes, logging_locations):
 for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
  if selenium_element.get_attribute('href') in visited_videos: continue
  else:
   video_number, total_writes = write.txt_entry(new_file, markdown_formatting, selenium_element, NEWLINE, spacing, video_number, incrementer, total_writes)
   if total_writes % 250 == 0:
    log(f'{total_writes} new videos written to {new_file.name}...', logging_locations)
 if reverse_chronological:
  old_file.seek(0)
  for line in old_file: new_file.write(line)
 else:
  new_file.seek(0)
  for line in new_file: old_file.write(line)
@time_writer_function
def write_to_txt(list_of_videos, file_name, reverse_chronological, logging_locations, timestamp, stored_in_txt):
 if stored_in_txt is None: stored_in_txt = store_already_written_videos(file_name, 'txt')
 markdown_formatting = False
 spacing    = f'{NEWLINE}' + ' '*4
 with open(f'{file_name}.txt', 'r+', encoding='utf-8') as old_file, open(f'temp_{file_name}_{timestamp}.txt', 'w+', encoding='utf-8') as temp_file:
  video_number          =  int(max(re.findall('^Video Number:\s*(\d+)', old_file.read(), re.M), key = lambda i: int(i)))
  video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, stored_in_txt, video_number, reverse_chronological)
  ####### defer to txt_writer() function to find new videos and format updated file #######
  txt_writer(temp_file, old_file, stored_in_txt, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes, logging_locations)
 return file_name, new_videos, reverse_chronological, logging_locations
@time_writer_function
def write_to_md(list_of_videos, file_name, reverse_chronological, logging_locations, timestamp, stored_in_md):
 if stored_in_md is None: stored_in_md = store_already_written_videos(file_name, 'md')
 markdown_formatting = True
 spacing    = f'{NEWLINE}' + '- ' + f'{NEWLINE}'
 with open(f'{file_name}.md', 'r+', encoding='utf-8') as old_file, open(f'temp_{file_name}_{timestamp}.md', 'w+', encoding='utf-8') as temp_file:
  video_number          =  int(max(re.findall('^Video Number:\s*(\d+)', old_file.read(), re.M), key = lambda i: int(i)))
  video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, stored_in_md, video_number, reverse_chronological)
  ####### defer to txt_writer() function to find new videos and format updated file #######
  txt_writer(temp_file, old_file, stored_in_md, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes, logging_locations)
 return file_name, new_videos, reverse_chronological, logging_locations
@time_writer_function
def write_to_csv(list_of_videos, file_name, reverse_chronological, logging_locations, timestamp, stored_in_csv):
 if stored_in_csv is None: stored_in_csv = store_already_written_videos(file_name, 'csv')
 with open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8') as old_file, open(f'temp_{file_name}_{timestamp}.csv', 'w+', newline='', encoding='utf-8') as temp_file:
  video_number          =  int(max(re.findall('^(\d+)?,', old_file.read(), re.M), key = lambda i: int(i)))
  video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, stored_in_csv, video_number, reverse_chronological)
  fieldnames            = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
  writer             = csv.DictWriter(temp_file, fieldnames=fieldnames)
  if reverse_chronological: writer.writeheader()
  for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
   if selenium_element.get_attribute('href') in stored_in_csv: continue
   else:
    video_number, total_writes = write.csv_entry(writer, selenium_element, video_number, incrementer, total_writes)
    if total_writes % 250 == 0:
     log(f'{total_writes} videos written to {temp_file.name}...', logging_locations)
  if reverse_chronological:
   old_file.seek(0)
   old_file.readline()
   for line in old_file: temp_file.write(line)
  else:
   temp_file.seek(0)
   for line in temp_file: old_file.write(line)
 return file_name, new_videos, reverse_chronological, logging_locations
