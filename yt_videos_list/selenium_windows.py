import re
import json
import subprocess

from .windows import get_drive_letter, get_user_name


def firefox_exists(browser):
    drive = get_drive_letter()
    return browser in subprocess.getoutput(rf'dir "{drive}:\Program Files"')

def opera_exists(browser):
    drive = get_drive_letter()
    user  = get_user_name()
    return browser in subprocess.getoutput(rf'dir {drive}:\Users\{user}\AppData\Local\Programs')

def chrome_exists(browser):
    drive = get_drive_letter()
    return browser in  subprocess.getoutput(rf'dir "{drive}:\Program Files (x86)\Google"')

def browser_exists(browser):
    if   browser == 'Mozilla Firefox': return firefox_exists(browser)
    elif browser == 'Opera':           return opera_exists(browser)
    elif browser == 'Chrome':          return chrome_exists(browser)


def get_firefox_version():
    drive   = get_drive_letter()
    firefox = subprocess.getoutput(rf'more "{drive}:\Program Files\Mozilla Firefox\application.ini"')
    return re.search(r'MinVersion=(\d+\.[\d\.]*)', firefox)[1]

def get_opera_version():
    drive = get_drive_letter()
    user  = get_user_name()
    with open(rf'{drive}:\Users\{user}\AppData\Local\Programs\Opera\installation_status.json', 'r') as file:
        opera = json.load(file)
    return opera['_subfolder']

def get_chrome_version():
    drive  = get_drive_letter()
    chrome = subprocess.getoutput(rf'dir "{drive}:\Program Files (x86)\Google\Chrome\Application"')
    return re.search(r'(\d\d\.[\d\.]*)', chrome)[1]

def get_browser_version(browser):
    if   browser == 'Mozilla Firefox': return get_firefox_version()
    elif browser == 'Opera':           return get_opera_version()
    elif browser == 'Chrome':          return get_chrome_version()
