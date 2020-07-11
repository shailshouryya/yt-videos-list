import sys
import time
import selenium
from selenium import webdriver
from . import program
from .download.selenium_webdriver_dependencies import download_all
from .download.windows_info     import get_drive_letter
from .download.user_os_info     import determine_user_os
from .notifications       import Common, ModuleMessage, ScriptMessage
def logic(channel, channel_type, file_name, txt, csv, markdown, reverse_chronological, headless, scroll_pause_time, user_driver, execution_type):
 common_message = Common()
 module_message = ModuleMessage()
 script_message = ScriptMessage()
 def check_user_input():
  nonlocal channel, channel_type, user_driver
  base_url  = 'https://www.youtube.com'
  videos    = 'videos'
  url    = f'{base_url}/{channel_type}/{channel}/{videos}'
  if txt is False and csv is False:
   print(common_message.not_writing_to_any_files)
   print(module_message.not_writing_to_any_files_hint) if execution_type == 'module' else print(script_message.not_writing_to_any_files_hint)
   sys.exit()
  if user_driver is None:
   print(module_message.running_default_driver) if execution_type == 'module' else print(script_message.running_default_driver)
   print(module_message.show_driver_options) if execution_type == 'module' else print(script_message.show_driver_options)
   user_driver = 'firefox'
  seleniumdriver = check_driver()
  if seleniumdriver == 'invalid':
   sys.exit()
  return url, seleniumdriver
 def check_driver():
  if   'firefox' in user_driver: return webdriver.Firefox
  elif 'opera'   in user_driver: return webdriver.Opera
  elif 'chrome'  in user_driver: return webdriver.Chrome
  elif 'brave'   in user_driver: return configure_brave_driver
  elif 'edge' in user_driver: return configure_edge_driver
  elif 'safari'  in user_driver:
   if user_os != 'macos':
    common_message.display_dependency_setup_instructions('safari', user_os)
    sys.exit()
   return webdriver.Safari
  else:
   print(common_message.invalid_driver)
   return 'invalid'
 def configure_brave_driver():
  options = webdriver.ChromeOptions()
  if user_os == 'windows':
   drive  = get_drive_letter()
   options.binary_location = rf'{drive}:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
   executable_path   = rf'{drive}:\Windows\bravedriver.exe'
  else:
   options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
   executable_path   = '/usr/local/bin/bravedriver'
  return webdriver.Chrome(options=options, executable_path=executable_path)
 def configure_edge_driver():
  if user_os == 'windows':
   drive  = get_drive_letter()
   executable_path   = rf'{drive}:\Windows\msedgedriver.exe'
  else:
   executable_path   = '/usr/local/bin/msedgedriver'
   print(common_message.unsupported_edge)
   print(module_message.show_driver_options)
   sys.exit()
  return webdriver.Edge(executable_path=executable_path)
 def open_user_driver():
  if headless is False:
   return seleniumdriver()
  else:
   if   user_driver == 'firefox': return set_up_headless_firefox_driver()
   elif user_driver == 'opera':   return set_up_headless_opera_driver()
   elif user_driver == 'safari':  return set_up_headless_safari_driver()
   elif user_driver == 'chrome':  return set_up_headless_chrome_driver()
   elif user_driver == 'brave':   return set_up_headless_brave_driver()
   elif user_driver == 'edge': return set_up_headless_edge_driver()
 def set_up_headless_firefox_driver():
  options = selenium.webdriver.firefox.options.Options()
  options.headless = True
  return seleniumdriver(options=options)
 def set_up_headless_opera_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  driver = seleniumdriver(options=options)
  print(common_message.unsupported_opera_headless)
  return driver
 def set_up_headless_safari_driver():
  print(common_message.unsupported_safari_headless)
  return seleniumdriver()
 def set_up_headless_chrome_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  return seleniumdriver(chrome_options=options)
 def set_up_headless_brave_driver():
  print(common_message.unsupported_brave_headless)
  return configure_brave_driver()
 def set_up_headless_edge_driver():
  print(common_message.unsupported_edge_headless)
  return configure_edge_driver()
 def determine_file_name():
  if file_name is not None:
   return file_name.strip('.csv').strip('.txt')
  else:
   channel_name = driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-channel-name']").text.replace(' ', '')
   return f'{channel_name}_videos_list'
 def show_user_how_to_set_up_selenium():
  if user_driver != 'safari':
   common_message.tell_user_to_download_driver(user_driver)
  common_message.display_dependency_setup_instructions(user_driver, user_os)
 user_os    = determine_user_os()
 url, seleniumdriver = check_user_input()
 program_start    = time.perf_counter()
 try:
  driver = open_user_driver()
 except selenium.common.exceptions.WebDriverException as err:
  common_message.display_selenium_dependency_error(err)
  try:
   download_all()
   driver = open_user_driver()
  except:
   show_user_how_to_set_up_selenium()
   return
 with driver:
  print(f'\n\n\nNow scraping {url} using the {user_driver}driver:')
  driver.get(url)
  driver.set_window_size(780, 800)
  driver.set_window_position(0, 0)
  file_name = determine_file_name()
  program.determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name, txt, csv, markdown)
 program_end = time.perf_counter()
 total_time  = program_end - program_start
 print(f'This program took {total_time} seconds to complete.\n')
