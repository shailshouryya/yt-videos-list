import os
import sys
import platform

from . import selenium_linux, selenium_macos, selenium_windows
from .notifications import Common


def determine_user_os():
    if   platform.system().lower().startswith('darwin'):  return 'macos'
    elif platform.system().lower().startswith('linux'):   return 'linux'
    elif platform.system().lower().startswith('windows'): return 'windows'
    else:
        print(Common().unsupported_os)
        sys.exit()

def execute_download(driver, user_os, version):
    common_message = Common()
    row_in_list = {
        'firefox': {
            '74': -1,
            '73': -1,
            '72': -1,
            '71': -1,
            '70': -1,
            '69': -1,
            '68': -1,
            '67': -1,
            '66': -1,
            '65': -1,
            '64': -1,
            '63': -1,
            '62': -1,
            '61': -1,
            '60': -1,
        },
        'opera': {
            '68': -25,
            '67': -23,
            '66': -21,
            '65': -19,
            '64': -17,
            '63': -15,
            '62': -13,
            # there was no version 61
            '60': -11,
            # there was no version 59
            '58': -9,
            '57': -7,
            '56': -5,
            '55': -3,
            '54': -1,
        },
        'chrome': {
            '81': -19,
            '80': -17,
            '79': -15,
            '78': -13,
            '77': -11,
            '76': -9,
            '75': -7,
            '74': -5,
            '73': -3,
            '72': -1,
            '71': -1
        }
    }
    row = row_in_list[driver][version]
    print(f'Now downloading the corresponding selenium driver for {driver} version {version} on {user_os}:')
    print(f'{common_message.driver_downloads_for_os[driver][user_os][row-1]} #')
    print(f'{common_message.driver_downloads_for_os[driver][user_os][row]}')
    os.system(common_message.driver_downloads_for_os[driver][user_os][row])

def run():
    user_os = determine_user_os()
    globals()[f'selenium_{user_os}'].download_dependencies()
