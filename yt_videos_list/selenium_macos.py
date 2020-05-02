import re
import sys
import subprocess

def browser_exists(browser):
    return browser in subprocess.getoutput('ls /Applications')

def get_browser_version(browser):
    with open (f'/Applications/{browser}.app/Contents/Info.plist') as f:
        info_plist = f.read()
    return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]

def download(user_driver):
    print(f'Automatic Selenium dependency download for MacOS is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the {user_driver} driver.')
    sys.exit()

def download_dependencies():
    application_name = {
        # 'driver': 'browser_name'
        'firefox':  'Firefox',
        'opera':    'Opera',
        'chrome':   'Google Chrome'
    }

    for driver in application_name:
        browser = application_name[driver]
        if browser_exists(browser):
            full_version_number = get_browser_version(browser)
            major_version = full_version_number.split('.')[0]
