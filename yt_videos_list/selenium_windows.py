import re
import sys
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

def get_browser_version(browser):
    # with open (f'/Applications/{browser}.app/Contents/Info.plist') as f:
    #     info_plist = f.read()
    # return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]
    sys.exit()
