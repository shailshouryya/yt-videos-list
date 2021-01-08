import os
from .      import selenium_linux, selenium_macos, selenium_windows
from .user_os_info   import determine_user_os
from ..notifications import Common
COMMON_MESSAGE = Common()
APPLICATION_NAME = {
 'macos': {
  'firefox':  'Firefox',
  'opera': 'Opera',
  'chrome':   'Google Chrome',
  'brave': 'Brave Browser',
  'edge':  'Microsoft Edge'
 },
 'linux': {
  'firefox':  'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the firefoxdriver.',
  'opera': 'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the operadriver.',
  'chrome':   'Automatic Selenium dependency download for Windows is not yet supported. Please follow the instructions below to set up the correct selenium dependecy for the chromedriver.'
 },
 'windows': {
  'firefox':  'Mozilla Firefox',
  'opera': 'Opera',
  'chrome':   'Chrome',
  'brave': 'Brave-Browser',
  'edge':  'Edge'
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
def execute_download_command(driver, user_os, version):
 row_in_list = {
  'firefox': {
   '99': -5,
   '98': -5,
   '97': -5,
   '96': -5,
   '95': -5,
   '94': -5,
   '93': -5,
   '92': -5,
   '91': -5,
   '90': -5,
   '89': -5,
   '88': -5,
   '87': -5,
   '86': -5,
   '85': -5,
   '84': -5,
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
   '99': -35,
   '98': -35,
   '97': -35,
   '96': -35,
   '95': -35,
   '94': -35,
   '93': -35,
   '92': -35,
   '91': -35,
   '90': -35,
   '89': -35,
   '88': -35,
   '87': -35,
   '86': -33,
   '85': -33,
   '84': -33,
   '83': -33,
   '82': -33,
   '81': -33,
   '80': -33,
   '79': -33,
   '78': -33,
   '77': -33,
   '76': -33,
   '75': -33,
   '74': -33,
   '73': -33,
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
   '60': -11,
   '58': -9,
   '57': -7,
   '56': -5,
   '55': -3,
   '54': -1,
  },
  'chrome': {
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
   '89': -29,
   '88': -29,
   '87': -29,
   '86': -27,
   '85': -25,
   '84': -23,
   '83': -21,
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
  },
  'brave': {
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
   '89': -23,
   '88': -23,
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
   '99': -21,
   '98': -21,
   '97': -21,
   '96': -21,
   '95': -21,
   '94': -21,
   '93': -21,
   '92': -21,
   '91': -21,
   '90': -21,
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
 row = row_in_list[driver][version]
 print(f'Now downloading the corresponding selenium driver for {driver} version {version} on {user_os}:')
 print(f'{COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row-1]} #')
 print(f'{COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row]}')
 os.system(COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row])
def download_all():
 user_os = determine_user_os()
 download_all_dependencies(user_os)
