import re
import sys
import subprocess

from .notifications import Common
from . import download_dependencies

def browser_exists(browser):
    return browser in subprocess.getoutput('ls /Applications')

def get_browser_version(browser):
    with open (f'/Applications/{browser}.app/Contents/Info.plist') as f:
        info_plist = f.read()
    return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]

def download_driver(driver, version):
    download_dependencies.execute_download_command(driver, 'macos', version)

def download(user_driver):
    print(f'Automatic Selenium dependency download for MacOS is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the {user_driver} driver.')
    sys.exit()

def download_all_dependencies():
    common_message = Common()
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
            common_message.display_browser_found_information(browser, full_version_number)
            major_version = full_version_number.split('.')[0]
            download_driver(driver, major_version)
        else:
            common_message.display_browser_not_found_information(browser, full_version_number)
