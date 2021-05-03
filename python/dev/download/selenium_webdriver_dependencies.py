import os

from .               import selenium_linux, selenium_macos, selenium_windows
from .user_os_info   import determine_user_os
from ..notifications import Common


COMMON_MESSAGE = Common()
APPLICATION_NAME = {
    'macos': {
        # 'driver': 'browser_name'
        'firefox':  'Firefox',
        'opera':    'Opera',
        'chrome':   'Google Chrome',
        'brave':    'Brave Browser',
        'edge':     'Microsoft Edge'
    },
    'linux': {
        'firefox':  'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the firefoxdriver.',
        'opera':    'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the operadriver.',
        'chrome':   'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the chromedriver.'
    },
    'windows': {
        'firefox':  'Mozilla Firefox',
        'opera':    'Opera',
        'chrome':   'Chrome',
        'brave':    'Brave-Browser',
        'edge':     'Edge'
    }
}


def download_specific_dependency(driver, user_os):
    selenium_user_os = globals()[f'selenium_{user_os}']
    browser = APPLICATION_NAME[user_os][driver]
    if selenium_user_os.browser_exists(browser):
        full_version_number = selenium_user_os.get_browser_version(browser)
        COMMON_MESSAGE.display_browser_found_information(browser, full_version_number)
        major_version = full_version_number.split('.')[0]
        execute_download_command(driver, user_os, major_version)
    else:
        COMMON_MESSAGE.display_browser_not_found_information(browser, user_os)

def download_all_dependencies(user_os):
    print(COMMON_MESSAGE.automated_driver_update)
    for driver in APPLICATION_NAME[user_os]:
        download_specific_dependency(driver, user_os)

def execute_download_command(driver, user_os, major_version):
    # indexed values in reverse order to avoid having to map every version to a different element every time a new driver/browser version comes out since all the values get shifted down by 2 with new additions to the top of the list
    row_in_list = {
        'firefox': {
            '99': -9,
            '98': -9,
            '97': -9,
            '96': -9,
            '95': -9,
            '94': -9,
            '93': -9,
            '92': -9,
            '91': -9,
            '90': -9,
            '89': -9,
            '88': -9,
            '87': -9,
            '86': -7,
            '85': -7,
            '84': -7,
            '83': -5,
            '82': -5,
            '81': -3,
            '80': -3,
            '79': -3,
            '78': -3,
            '77': -1,
            '76': -1,
            '75': -1,
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
            '99': -41,
            '98': -41,
            '97': -41,
            '96': -41,
            '95': -41,
            '94': -41,
            '93': -41,
            '92': -41,
            '91': -41,
            '90': -41,
            '89': -41,
            '88': -41,
            '87': -41,
            '86': -41,
            '85': -41,
            '84': -41,
            '83': -41,
            '82': -41,
            '81': -41,
            '80': -41,
            '79': -41,
            '78': -41,
            '77': -41,
            '76': -41,
            '75': -39,
            '74': -37,
            '73': -35,
            '72': -33,
            '71': -31,
            '70': -29,
            '69': -27,
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
            '99': -41,
            '98': -41,
            '97': -41,
            '96': -41,
            '95': -41,
            '94': -41,
            '93': -41,
            '92': -41,
            '91': -41,
            '90': -39,
            '89': -37,
            '88': -35,
            '87': -33,
            '86': -31,
            '85': -29,
            '84': -27,
            '83': -25,
            # there was no 82
            '81': -23,
            '80': -21,
            '79': -19,
            '78': -17,
            '77': -15,
            '76': -13,
            '75': -11,
            '74': -9,
            '73': -7,
            '72': -5,
            '71': -5,
            '70': -3,
            '69': -1
        },
        'brave': {
            '99': -29,
            '98': -29,
            '97': -29,
            '96': -29,
            '95': -29,
            '94': -29,
            '93': -29,
            '92': -29,
            '91': -29,
            '90': -29,
            '89': -27,
            '88': -25,
            '87': -23,
            '86': -21,
            '85': -19,
            '84': -17,
            '83': -15,
            # there was no 82
            '81': -13,
            '80': -11,
            '79': -9,
            '78': -7,
            '77': -5,
            '76': -3,
            '75': -1
        },
        'edge': {
            '99': -23,
            '98': -23,
            '97': -23,
            '96': -23,
            '95': -23,
            '94': -23,
            '93': -23,
            '92': -23,
            '91': -23,
            '90': -23,
            '89': -21,
            '88': -19,
            '87': -17,
            '86': -15,
            '85': -13,
            '84': -11,
            '83': -9,
            '82': -7,
            '81': -5,
            '80': -3,
            '79': -1
        }
    }
    row = row_in_list[driver][major_version]
    print(f'Now downloading the corresponding selenium driver for {driver} version {major_version} on {user_os}:')
    print(f'{COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row-1]} #')
    print(f'{COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row]}')
    os.system(COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row])

def download_all():
    user_os = determine_user_os()
    download_all_dependencies(user_os)
