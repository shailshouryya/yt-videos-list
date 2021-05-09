import os
from . import selenium_linux, selenium_macos, selenium_windows
from .user_os_info import determine_user_os
from ..notifications import Common
COMMON_MESSAGE = Common()
APPLICATION_NAME = {
 'macos': {
  'firefox': 'Firefox',
  'opera': 'Opera',
  'chrome': 'Google Chrome',
  'brave': 'Brave Browser',
  'edge': 'Microsoft Edge'
 },
 'linux': {
  'firefox': 'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the firefoxdriver.',
  'opera': 'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the operadriver.',
  'chrome': 'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the chromedriver.'
 },
 'windows': {
  'firefox': 'Mozilla Firefox',
  'opera': 'Opera',
  'chrome': 'Chrome',
  'brave': 'Brave-Browser',
  'edge': 'Edge'
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
   '99': -49,
   '98': -49,
   '97': -49,
   '96': -49,
   '95': -49,
   '94': -49,
   '93': -49,
   '92': -49,
   '91': -49,
   '90': -49,
   '89': -49,
   '88': -49,
   '87': -49,
   '86': -49,
   '85': -49,
   '84': -49,
   '83': -49,
   '82': -49,
   '81': -49,
   '80': -49,
   '79': -49,
   '78': -49,
   '77': -49,
   '76': -49,
   '75': -47,
   '74': -45,
   '73': -43,
   '72': -41,
   '71': -39,
   '70': -37,
   '69': -35,
   '68': -33,
   '67': -31,
   '66': -29,
   '65': -27,
   '64': -25,
   '63': -23,
   '62': -21,
   '60': -19,
   '58': -17,
   '57': -15,
   '56': -13,
   '55': -11,
   '54': -9,
   '53': -7,
   '52': -5,
   '50': -3,
   '49': -1
  },
  'chrome': {
   '99': -47,
   '98': -47,
   '97': -47,
   '96': -47,
   '95': -47,
   '94': -47,
   '93': -47,
   '92': -47,
   '91': -47,
   '90': -45,
   '89': -43,
   '88': -41,
   '87': -39,
   '86': -37,
   '85': -35,
   '84': -33,
   '83': -31,
   '81': -29,
   '80': -27,
   '79': -25,
   '78': -23,
   '77': -21,
   '76': -19,
   '75': -17,
   '74': -15,
   '73': -13,
   '72': -11,
   '71': -11,
   '70': -9,
   '69': -7,
   '68': -3,
   '67': -1
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
   '81': -13,
   '80': -11,
   '79': -9,
   '78': -7,
   '77': -5,
   '76': -3,
   '75': -1
  },
  'edge': {
   '99': -27,
   '98': -27,
   '97': -27,
   '96': -27,
   '95': -27,
   '94': -27,
   '93': -27,
   '92': -27,
   '91': -25,
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
