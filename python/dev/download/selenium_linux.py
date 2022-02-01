import sys


def browser_exists(browser):
    # return browser in subprocess.getoutput('ls /Applications')
    raise RuntimeError('Automatic selenium updates are not yet available for Linux distributions!\nPlease update your selenium driver manually.')

def get_browser_version(browser):
    # with open(f'/Applications/{browser}.app/Contents/Info.plist', mode='r', encoding='utf-8') as f:
    #     info_plist = f.read()
    # return re.search('<key>CFBundleShortVersionString</key>\s*<string>([0-9\.]+)', info_plist)[1]
    raise RuntimeError('Automatic selenium updates are not yet available for Linux distributions!\nPlease update your selenium driver manually.')
