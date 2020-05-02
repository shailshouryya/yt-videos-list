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
