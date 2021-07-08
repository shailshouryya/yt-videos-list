import os
import datetime
import threading
from . import scroller, writer
from .notifications import Common
from .custom_logger import log
def determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name, file_buffering, txt, csv, markdown, logging_locations, verify_page_bottom_n_times):
 common_message = Common()
 txt_exists = os.path.isfile(f'{file_name}.txt') if txt else False
 csv_exists = os.path.isfile(f'{file_name}.csv') if csv else False
 md_exists = os.path.isfile(f'{file_name}.md') if markdown else False
 txt_videos = None
 csv_videos = None
 md_videos = None
 current_condition = (txt, txt_exists, csv, csv_exists, markdown, md_exists)
 update_conditions = set(
  (
   (True, True, True, True, True, True),
   (True, True, True, True, False, False),
   (True, True, False, False, True, True),
   (False, False, True, True, True, True),
   (True, True, False, False, False, False),
   (False, False, False, False, True, True),
   (False, False, True, True, False, False),
  )
 )
 if current_condition in update_conditions: videos_list, txt_videos, csv_videos, md_videos = scroller.scroll_to_old_videos(url, driver, scroll_pause_time, logging_locations, file_name, txt_exists, csv_exists, md_exists)
 else: videos_list = scroller.scroll_to_bottom (url, driver, scroll_pause_time, logging_locations, verify_page_bottom_n_times)
 if len(videos_list) == 0:
  log(common_message.no_videos_found, logging_locations)
  return
 use_threads = (int(txt) + int(csv) + int(markdown)) > 1
 if use_threads:
  #
  threads = []
  def call(function, file_type, file_videos=None):
   if function == 'update_file': return threading.Thread(target=writer.update_file, args=(file_type, videos_list, file_name, file_buffering, reverse_chronological, logging_locations), kwargs={'timestamp': now(), 'stored_in_file': file_videos})
   else: return threading.Thread(target=writer.create_file, args=(file_type, videos_list, file_name, file_buffering, reverse_chronological, logging_locations), kwargs={'timestamp': now()})
  if txt:
   if txt_exists: txt_thread = call('update_file', 'txt', txt_videos)
   else: txt_thread = call('create_file', 'txt')
   txt_thread.start()
   threads.append(txt_thread)
  if csv:
   if csv_exists: csv_thread = call('update_file', 'csv', csv_videos)
   else: csv_thread = call('create_file', 'csv')
   csv_thread.start()
   threads.append(csv_thread)
  if markdown:
   if md_exists: md_thread = call('update_file', 'md', md_videos)
   else: md_thread = call('create_file', 'md')
   md_thread.start()
   threads.append(md_thread)
  for thread in threads:
   thread.join()
 else:
  def call(function, file_type, file_videos=None):
   if function == 'update_file': return writer.update_file(file_type, videos_list, file_name, file_buffering, reverse_chronological, logging_locations, timestamp=now(), stored_in_file=file_videos)
   else: return writer.create_file(file_type, videos_list, file_name, file_buffering, reverse_chronological, logging_locations, timestamp=now())
  if txt:
   if txt_exists: call('update_file', 'txt', txt_videos)
   else: call('create_file', 'txt')
  if csv:
   if csv_exists: call('update_file', 'csv', csv_videos)
   else: call('create_file', 'csv')
  if markdown:
   if md_exists: call('update_file', 'md', md_videos)
   else: call('create_file', 'md')
def now():
 return datetime.datetime.now().isoformat().replace(':', '_').replace('.', '-')
