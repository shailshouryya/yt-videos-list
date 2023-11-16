import re
import json
import subprocess

from typing import (
    Dict,
    Match,
    Optional,
)

from .windows_info import get_drive_letter, get_user_name
from .user_os_info import determine_user_os


# importing this module without this check results in errors on non-Windows platforms
if determine_user_os() == 'windows':
    DRIVE = get_drive_letter()
    USER  = get_user_name()


def verify_firefox_exists(
    browser: str,
) -> bool:
    return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files"')

def verify_opera_exists(
    browser: str,
) -> bool:
    return browser in subprocess.getoutput(rf'dir {DRIVE}:\Users\{USER}\AppData\Local\Programs')

def verify_chrome_exists(
    browser: str,
) -> bool:
    return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Google"')

def verify_brave_exists(
    browser: str,
) -> bool:
    return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/BraveSoftware"') or browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files/BraveSoftware"')

def verify_edge_exists(
    browser: str,
) -> bool:
    return browser in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/Microsoft"')

def verify_browser_exists(
    browser: str,
) -> bool:
    return {
        'Mozilla Firefox': verify_firefox_exists(browser),
        'Opera':           verify_opera_exists(browser),
        'Chrome':          verify_chrome_exists(browser),
        'Brave-Browser':   verify_brave_exists(browser),
        'Edge':            verify_edge_exists(browser)
    }[browser]


BROWSER_VERSION_REGEX = '\d+\.[\d\.]*'

def load_match(
    match: Optional[Match[str]],
) -> str:
    assert match is not None
    return match[1]


def get_firefox_version(
) -> str:
    firefox = subprocess.getoutput(rf'more "{DRIVE}:\Program Files\Mozilla Firefox\application.ini"')
    return load_match(re.search(f'MinVersion=({BROWSER_VERSION_REGEX})', firefox))

def get_opera_version(
) -> str:
    with open(rf'{DRIVE}:\Users\{USER}\AppData\Local\Programs\Opera\installation_status.json', mode='r', encoding='utf-8') as file:
        opera: Dict[str, str] = json.load(file)
    return opera['_subfolder']

def get_chrome_version(
) -> str:
    chrome = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Google\Chrome\Application"')
    return load_match(re.search(f'({BROWSER_VERSION_REGEX})', chrome))

def get_brave_version(
) -> str:
    if 'Brave-Browser' in subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)/BraveSoftware"'): program_file_path = 'Program Files (x86)'
    else:                                                                                             program_file_path = 'Program Files'
    brave = subprocess.getoutput(rf'dir "{DRIVE}:\{program_file_path}\BraveSoftware\Brave-Browser\Application"')
    return load_match(re.search(f'({BROWSER_VERSION_REGEX})', brave))

def get_edge_version(
) -> str:
    edge = subprocess.getoutput(rf'dir "{DRIVE}:\Program Files (x86)\Microsoft\Edge\Application"')
    return load_match(re.search(f'({BROWSER_VERSION_REGEX})', edge))

def get_browser_version(
    browser: str,
) -> str:
    return {
        'Mozilla Firefox': get_firefox_version(),
        'Opera':           get_opera_version(),
        'Chrome':          get_chrome_version(),
        'Brave-Browser':   get_brave_version(),
        'Edge':            get_edge_version()
    }[browser]
