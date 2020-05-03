import re
import sys
import subprocess


def firefox_exists():
    pass

def opera_exists():
    pass

def chrome_exists():
    pass

def browser_exists(browser):
    # return browser in subprocess.getoutput('ls /Applications')
    if   browser == 'Mozilla Firefox': return firefox_exists()
    elif browser == 'Opera':           return opera_exists()
    elif browser == 'Google':          return chrome_exists()

def get_browser_version(browser):
    # with open (f'/Applications/{browser}.app/Contents/Info.plist') as f:
    #     info_plist = f.read()
    # return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]
    sys.exit()
