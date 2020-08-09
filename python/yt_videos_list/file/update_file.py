import functools
import time
import csv
import re
import os
from . import write
NEWLINE = '\n'
def store_already_written_videos(file_name, file_type):
 with open(f'{file_name}.{file_type}') as file:
  if file_type == 'txt' or file_type == 'md': return set(re.findall(r'(https://www\.youtube\.com/watch\?v=.+?)(?:\s|\n)', file.read()))
  if file_type == 'csv':       return set(re.findall(r'(https://www\.youtube\.com/watch\?v=.+?),', file.read()))
def scroll_down(driver, scroll_pause_time):
 driver.execute_script('window.scrollBy(0, 50000);')
 time.sleep(scroll_pause_time * 2)
 new_elements_count = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
 print(f'Found {new_elements_count} videos...')
 if driver.find_elements_by_xpath('//*[@id="video-title"]')[-1].get_attribute("href") in VISITED_VIDEOS:
  return True
 return False
def save_elements_to_list(driver, start_time, scroll_pause_time, url):
 elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
 end_time = time.perf_counter()
 total_time = end_time - start_time - scroll_pause_time
 print(f'It took {total_time} seconds to find {len(elements)} videos from {url}{NEWLINE}')
 return elements
def scroll_to_old_videos(url, driver, scroll_pause_time, txt_exists, csv_exists, md_exists, file_name):
 global VISITED_VIDEOS, STORED_IN_TXT, STORED_IN_CSV, STORED_IN_MD
 STORED_IN_TXT = set()
 STORED_IN_CSV = set()
 STORED_IN_MD  = set()
 if txt_exists: STORED_IN_TXT = store_already_written_videos(file_name, 'txt')
 if csv_exists: STORED_IN_CSV = store_already_written_videos(file_name, 'csv')
 if md_exists:  STORED_IN_MD =  store_already_written_videos(file_name, 'md' )
 VISITED_VIDEOS = STORED_IN_TXT.intersection(STORED_IN_CSV).intersection(STORED_IN_MD)
 print(f'Detected an existing file with the name {file_name} in this directory, checking for new videos to update {file_name}....')
 start_time = time.perf_counter()
 found_old_videos = False
 while found_old_videos is False:
  found_old_videos = scroll_down(driver, scroll_pause_time)
 return save_elements_to_list(driver, start_time, scroll_pause_time, url)
def time_writer_function(writer_function):
 @functools.wraps(writer_function)
 def wrapper_timer(*args, **kwargs):
  start_time = time.perf_counter()
  extension  = writer_function.__name__.split('_')[-1]
  temp_file  = f'yt_videos_list_temp.{extension}'
  print(f'Opened {temp_file}, writing new video information to file....')
  file_name, new_videos_written, reverse_chronological = writer_function(*args, **kwargs)
  file_name = f'{file_name}.{extension}'
  if reverse_chronological: os.replace(temp_file, file_name)
  else:      os.remove(temp_file)
  end_time = time.perf_counter()
  total_time = end_time - start_time
  print(f'Finished writing to {temp_file}')
  print(f'{new_videos_written} new videos written to {temp_file}')
  print(f'Closing {temp_file}')
  print(f'Successfully completed write, renamed {temp_file} to {file_name}')
  print(f'It took {total_time} seconds to write the {new_videos_written} new videos to the pre-existing {file_name} {NEWLINE}')
 return wrapper_timer
def find_number_of_new_videos(list_of_videos, videos_set):
 visited_on_page = {selenium_element.get_attribute("href") for selenium_element in list_of_videos}
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
def txt_writer(new_file, old_file, visited_videos, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes):
 for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
  if selenium_element.get_attribute("href") in visited_videos: continue
  else:
   video_number, total_writes = write.txt_entry(new_file, markdown_formatting, selenium_element, NEWLINE, spacing, video_number, incrementer, total_writes)
   if total_writes % 250 == 0:
    print(f'{total_writes} new videos written to {new_file.name}...')
 if reverse_chronological:
  old_file.seek(0)
  for line in old_file: new_file.write(line)
 else:
  new_file.seek(0)
  for line in new_file: old_file.write(line)
@time_writer_function
def write_to_txt(list_of_videos, file_name, reverse_chronological):
 if 'STORED_IN_TXT' not in locals(): stored_in_txt = store_already_written_videos(file_name, 'txt')
 else:          stored_in_txt = STORED_IN_TXT
 markdown_formatting = False
 spacing    = f'{NEWLINE}' + ' '*4
 with open(f'{file_name}.txt', 'r+') as old_file, open('yt_videos_list_temp.txt', 'w+') as txt_file:
  video_number          =  int(max(re.findall(r'^Video Number:\s*(\d+)', old_file.read(), re.M), key = lambda i: int(i)))
  video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, stored_in_txt, video_number, reverse_chronological)
  txt_writer(txt_file, old_file, stored_in_txt, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes)
 return file_name, new_videos, reverse_chronological
@time_writer_function
def write_to_md(list_of_videos, file_name, reverse_chronological):
 if 'STORED_IN_MD'  not in locals(): stored_in_md = store_already_written_videos(file_name, 'md')
 else:          stored_in_md = STORED_IN_MD
 markdown_formatting = True
 spacing    = f'{NEWLINE}' + '- ' + f'{NEWLINE}'
 with open(f'{file_name}.md', 'r+') as old_file, open('yt_videos_list_temp.md', 'w+') as md_file:
  video_number          =  int(max(re.findall(r'^Video Number:\s*(\d+)', old_file.read(), re.M), key = lambda i: int(i)))
  video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, stored_in_md, video_number, reverse_chronological)
  txt_writer(md_file, old_file, stored_in_md, markdown_formatting, reverse_chronological, list_of_videos, spacing, video_number, incrementer, total_writes)
 return file_name, new_videos, reverse_chronological
@time_writer_function
def write_to_csv(list_of_videos, file_name, reverse_chronological):
 if 'STORED_IN_CSV' not in locals(): stored_in_csv = store_already_written_videos(file_name, 'csv')
 else:          stored_in_csv = STORED_IN_CSV
 with open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8') as old_file, open('yt_videos_list_temp.csv', 'w+', newline='', encoding='utf-8') as csv_file:
  video_number =  int(max(re.findall(r'^(\d+)?,', old_file.read(), re.M), key = lambda i: int(i)))
  video_number, new_videos, total_writes, incrementer = prepare_output(list_of_videos, stored_in_csv, video_number, reverse_chronological)
  fieldnames = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  if reverse_chronological: writer.writeheader()
  for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
   if selenium_element.get_attribute("href") in stored_in_csv: continue
   else:
    video_number, total_writes = write.csv_entry(writer, selenium_element, video_number, incrementer, total_writes)
    if total_writes % 250 == 0:
     print(f'{total_writes} videos written to {csv_file.name}...')
  if reverse_chronological:
   old_file.seek(0)
   old_file.readline()
   for line in old_file: csv_file.write(line)
  else:
   csv_file.seek(0)
   for line in csv_file: old_file.write(line)
 return file_name, new_videos, reverse_chronological
