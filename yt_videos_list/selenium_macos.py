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
