import re
import sys
import json
import subprocess


USER = subprocess.getoutput("whoami").split('\\')[1]

def firefox_exists(browser):
    return browser in r'more "C:\Program Files"'

def opera_exists(browser):
    return browser in rf'C:\Users\{USER}\AppData\Local\Programs'

def chrome_exists(browser):
    return browser in rf'dir "C:\Program Files (x86)\Google"'

def browser_exists(browser):
    if   browser == 'Mozilla Firefox': return firefox_exists(browser)
    elif browser == 'Opera':           return opera_exists(browser)
    elif browser == 'Google':          return chrome_exists(browser)


def get_firefox_version():
    firefox = subprocess.getoutput(r'more "C:\Program Files\Mozilla Firefox\application.ini"')
    return re.search('MinVersion=(\d+\.[\d\.]*)', firefox)[1]

def get_opera_version():
    with open(rf'C:\Users\{USER}\AppData\Local\Programs\Opera\installation_status.json', 'r') as f:
        opera = json.load(f)
    return opera['_subfolder']

def get_chrome_version():
    pass

def get_browser_version(browser):
    if   browser == 'Mozilla Firefox': return get_firefox_version()
    elif browser == 'Opera':           return get_opera_version()
    elif browser == 'Google':          return get_chrome_version()
