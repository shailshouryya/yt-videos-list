import re
import json
import subprocess
from .windows_info import get_drive_letter, get_user_name
from .user_os_info import determine_user_os
if determine_user_os() == 'windows':
 DRIVE = get_drive_letter()
 USER  = get_user_name()
def firefox_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files"')
def opera_exists(browser):
 return browser in subprocess.getoutput(rf'dir {DRIVE}:\Users\{USER}\AppData\Local\Programs')
def chrome_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Google"')
def brave_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/BraveSoftware"')
def edge_exists(browser):
 return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/Microsoft"')
def browser_exists(browser):
 if   browser == 'Mozilla Firefox': return firefox_exists(browser)
 elif browser == 'Opera':     return opera_exists(browser)
 elif browser == 'Chrome':    return chrome_exists(browser)
 elif browser == 'Brave-Browser':   return brave_exists(browser)
 elif browser == 'Edge':   return edge_exists(browser)
def get_firefox_version():
 firefox = subprocess.getoutput(rf'more "{DRIVE}:\Program Files\Mozilla Firefox\application.ini"')
 return re.search(r'MinVersion=(\d+\.[\d\.]*)', firefox)[1]
def get_opera_version():
 with open(rf'{DRIVE}:\Users\{USER}\AppData\Local\Programs\Opera\installation_status.json', 'r') as file:
  opera = json.load(file)
 return opera['_subfolder']
def get_chrome_version():
 chrome = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Google\Chrome\Application"')
 return re.search(r'(\d\d\.[\d\.]*)', chrome)[1]
def get_brave_version():
 brave = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\BraveSoftware\Brave-Browser\Application"')
 return re.search(r'(\d\d\.[\d\.]*)', brave)[1]
def get_edge_version():
 edge = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Microsoft\Edge\Application"')
 return re.search(r'(\d\d\.[\d\.]*)', edge)[1]
def get_browser_version(browser):
 if   browser == 'Mozilla Firefox': return get_firefox_version()
 elif browser == 'Opera':     return get_opera_version()
 elif browser == 'Chrome':    return get_chrome_version()
 elif browser == 'Brave-Browser':   return get_brave_version()
 elif browser == 'Edge':   return get_edge_version()
