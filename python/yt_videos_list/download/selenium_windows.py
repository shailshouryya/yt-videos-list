import re
import json
import subprocess
from .windows_info import get_drive_letter, get_user_name
from .user_os_info import determine_user_os
if determine_user_os() == 'windows':
 DRIVE = get_drive_letter()
 USER = get_user_name()
def firefox_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files"')
def opera_exists(browser):
 return browser in subprocess.getoutput(rf'dir {DRIVE}:\Users\{USER}\AppData\Local\Programs')
def chrome_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Google"')
def brave_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/BraveSoftware"') or browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files/BraveSoftware"')
def edge_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/Microsoft"')
def browser_exists(browser):
 return {
  'Mozilla Firefox': firefox_exists(browser),
  'Opera': opera_exists(browser),
  'Chrome': chrome_exists(browser),
  'Brave-Browser': brave_exists(browser),
  'Edge': edge_exists(browser)
 }[browser]
def get_firefox_version():
 firefox = subprocess.getoutput(rf'more "{DRIVE}:\Program Files\Mozilla Firefox\application.ini"')
 return re.search('MinVersion=(\d+\.[\d\.]*)', firefox)[1]
def get_opera_version():
 with open(rf'{DRIVE}:\Users\{USER}\AppData\Local\Programs\Opera\installation_status.json', mode='r', encoding='utf-8') as file:
  opera = json.load(file)
 return opera['_subfolder']
def get_chrome_version():
 chrome = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Google\Chrome\Application"')
 return re.search('(\d\d\.[\d\.]*)', chrome)[1]
def get_brave_version():
 if 'Brave-Browser' in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/BraveSoftware"'): program_file_path = 'Program Files (x86)'
 else: program_file_path = 'Program Files'
 brave = subprocess.getoutput(rf'dir "{DRIVE}:\{program_file_path}\BraveSoftware\Brave-Browser\Application"')
 return re.search('(\d\d\.[\d\.]*)', brave)[1]
def get_edge_version():
 edge = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Microsoft\Edge\Application"')
 return re.search('(\d\d\.[\d\.]*)', edge)[1]
def get_browser_version(browser):
 return {
  'Mozilla Firefox': get_firefox_version(),
  'Opera': get_opera_version(),
  'Chrome': get_chrome_version(),
  'Brave-Browser': get_brave_version(),
  'Edge': get_edge_version()
 }[browser]
