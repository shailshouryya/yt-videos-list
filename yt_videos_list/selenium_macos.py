import re
import sys
import subprocess

from .download_dependencies import execute_download

def browser_exists(browser):
    return browser in subprocess.getoutput('ls /Applications')

def get_browser_version(browser):
    with open (f'/Applications/{browser}.app/Contents/Info.plist') as f:
        info_plist = f.read()
    return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]

def download_driver(driver, version):
    execute_download(driver, 'macos', version)

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
            print(f'\nFound an installed version of {browser}.\nYou are currently running {browser} version: {full_version_number}')

            major_version = full_version_number.split('.')[0]
            globals()[f'download_driver'](driver, major_version)
        else:
            print(f'Did not find an installed version of {browser}.\nIf you DO have {browser} installed but it was not detected, it may be because your {browser} was installed in a non-default location.\nPlease follow the directions under the {browser.title()} section at https://github.com/Shail-Shouryya/yt_videos_list/extra/README.md for "Setting up your Selenium dependencies for user_os.title"\n')
