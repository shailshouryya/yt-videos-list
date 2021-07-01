import re
import subprocess
def browser_exists(browser):
 return browser in subprocess.getoutput('ls /Applications')
def get_browser_version(browser):
 with open(f'/Applications/{browser}.app/Contents/Info.plist', mode='r', encoding='utf-8') as file:
  info_plist = file.read()
 return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]
