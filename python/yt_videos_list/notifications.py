from .download.windows_info import get_drive_letter
class Common:
 '''
 This class contains messages that are common regardless of whether the package is being run as a module using the -m option from the CLI or as a module from within the Python interpreter (or another Python script).
 '''
 indent = ' ' * 4
 ds = ' ' * 2
 offset = '\n\n\n'
 error = '===>ERROR!<===\n'
 debugging_info = '\n\nFor further debugging, this was the exact error message (might also be blank):\n'
 missing_url = 'create_list_for() missing 1 required positional argument: "url"'
 not_writing_to_any_files = '\nBased on your provided settings, yt_videos_list will not be writing to a csv file, nor a txt file, nor a md file, nor to memory.'
 no_videos_found = 'No videos were found for the channel you provided. Are you sure you entered the url correctly?\n\n'
 invalid_response = 'The response you entered was invalid.'
 invalid_driver = f'The driver you specified is invalid. Please try rerunning the last command after specifying a valid driver. Supported drivers include:\n{indent}Firefox\n{indent}Opera\n{indent}Safari\n{indent}Chrome\n{indent}Brave'
 unsupported_opera_headless = '\nHeadless mode is unsupported in OperaDriver. We are waiting on the Opera dev team to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
 unsupported_safari_headless = '\nHeadless mode is unsupported in SafariDriver. We are waiting on Apple to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
 unsupported_brave_headless = '\nHeadless mode is unsupported in BraveDriver. We are waiting for a Brave release that supports headless before offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
 unsupported_edge_headless = '\nHeadless mode is unsupported in EdgeDriver. We are waiting for on the Miscrosoft Edge release to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
 unsupported_edge = 'ERROR! Selenium automation with msedgedriver (Microsoft Edge) is not yet supported on your platform. Please use a different browser!'
 unsupported_os = 'The system you are using is not yet supported. Please create an issue at https://github.com/slow-but-steady/yt-videos-list/issues\nThanks!'
 automated_driver_update = '\n=====> Now updating Selenium driver binaries and fixing any version incompatibility problems. <=====\nThis will update all corresponding Selenium drivers for browsers (which are installed in their default locations and) supported by the yt_videos_list package...'
 url_prefix_geckodriver = 'https://github.com/mozilla/geckodriver/releases/download'
 url_prefix_operadriver = 'https://github.com/operasoftware/operachromiumdriver/releases/download'
 url_prefix_chromedriver = 'https://chromedriver.storage.googleapis.com'
 url_prefix_msedgedriver = 'https://msedgedriver.azureedge.net'
 chromedriver_source_code_urls = 'https://chromium.googlesource.com/chromium/src/ or\nhttps://source.chromium.org/chromium/chromium/src'
 more_driver_info = {
  'firefox': ['geckodriver', 'https://github.com/mozilla/geckodriver', 'https://github.com/mozilla/geckodriver/releases', 'Mozilla Firefox', 'https://www.mozilla.org/en-US/firefox/new/'],
  'opera': ['operadriver', 'https://github.com/operasoftware/operachromiumdriver', 'https://github.com/operasoftware/operachromiumdriver/releases', 'Opera Browser', 'https://www.opera.com/'],
  'chrome': ['chromedriver', chromedriver_source_code_urls, 'https://sites.google.com/chromium.org/driver/downloads', 'Google Chrome', 'https://www.google.com/chrome/'],
  'brave': ['bravedriver', 'https://github.com/operasoftware/operachromiumdriver', 'https://github.com/operasoftware/operachromiumdriver/releases', 'Brave Browser', 'https://brave.com/'],
  'edge': ['msedgedriver', 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/', 'https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver?comp=list&timeout=60000', 'Microsoft Edge', 'https://www.microsoft.com/en-us/edge']
 }
 def __init__(self):
  self.driver_downloads_for_os = {
   'firefox': {
    'macos': self.create_list_for('macos', 'geckodriver'),
    'linux': self.create_list_for('linux64', 'geckodriver') + self.create_list_for('linux32', 'geckodriver'),
    'windows': self.create_list_for('win32', 'geckodriver') + self.create_list_for('win64', 'geckodriver')
   },
   'opera': {
    'macos': self.create_list_for('mac64', 'operadriver'),
    'linux': self.create_list_for('linux64', 'operadriver'),
    'windows': self.create_list_for('win32', 'operadriver') + self.create_list_for('win64', 'operadriver')
   },
   'safari': {
    'macos': self.create_list_for('macos', 'safaridriver'),
    'linux': self.create_list_for('linux', 'safaridriver'),
    'windows': self.create_list_for('windows', 'safaridriver')
   },
   'chrome': {
    'macos': self.create_list_for('mac64', 'chromedriver'),
    'linux': self.create_list_for('linux64', 'chromedriver'),
    'windows': self.create_list_for('win32', 'chromedriver')
   },
   'brave': {
    'macos': self.create_list_for('mac64', 'bravedriver'),
    'linux': self.create_list_for('linux64', 'bravedriver'),
    'windows': self.create_list_for('win64', 'bravedriver')
   },
   'edge': {
    'macos': self.create_list_for('mac64', 'msedgedriver'),
    'linux': ['There is currently no dedicated msedgedriver for Linux.\nHere are possible commands for an arm64 operating system.\nPlease visit https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ for more information.'] + \
         self.create_list_for('arm64', 'msedgedriver'),
    'windows': self.create_list_for('win32', 'msedgedriver') + self.create_list_for('win64', 'msedgedriver')
   }
  }
 @classmethod
 def create_list_for(cls, operating_system, driver):
  formatter_function = getattr(cls, f'format_{driver}_list')
  return formatter_function(operating_system)
 @classmethod
 def format_geckodriver_list(cls, operating_system):
  driver_name = 'geckodriver'
  browser_name = 'Mozilla Firefox'
  return [
   cls.format_driver_information (operating_system, 'v0.30.0', '≥ 92', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v0.30.0'),
   cls.format_driver_information (operating_system, 'v0.29.1', '≥ 87', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v0.29.1'),
   cls.format_driver_information (operating_system, 'v0.29.0', '≥ 84', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v0.29.0'),
   cls.format_driver_information (operating_system, 'v0.28.0', '≥ 82', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v0.28.0'),
   cls.format_driver_information (operating_system, 'v0.27.0', '≥ 78', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v0.27.0'),
   cls.format_driver_information (operating_system, 'v0.26.0', '≥ 60', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v0.26.0')
  ]
 @classmethod
 def format_operadriver_list(cls, operating_system):
  driver_name = 'operadriver'
  browser_name = 'Opera Browser'
  return [
   cls.format_driver_information (operating_system, 'v.95.0.4638.54', 'Stable 81', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.95.0.4638.54'),
   cls.format_driver_information (operating_system, 'v.94.0.4606.61', 'Stable 80', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.94.0.4606.61'),
   cls.format_driver_information (operating_system, 'v.93.0.4577.63', 'Stable 79', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.93.0.4577.63'),
   cls.format_driver_information (operating_system, 'v.92.0.4515.107', 'Stable 78', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.92.0.4515.107'),
   cls.format_driver_information (operating_system, 'v.91.0.4472.77', 'Stable 77', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.91.0.4472.77'),
   cls.format_driver_information (operating_system, 'v.90.0.4430.85', 'Stable 76', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.90.0.4430.85'),
   cls.format_driver_information (operating_system, 'v.89.0.4389.82', 'Stable 75', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.89.0.4389.82'),
   cls.format_driver_information (operating_system, 'v.88.0.4324.104', 'Stable 74', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.88.0.4324.104'),
   cls.format_driver_information (operating_system, 'v.87.0.4280.67', 'Stable 73', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.87.0.4280.67'),
   cls.format_driver_information (operating_system, 'v.86.0.4240.80', 'Stable 72', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.86.0.4240.80'),
   cls.format_driver_information (operating_system, 'v.85.0.4183.102', 'Stable 71', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.85.0.4183.102'),
   cls.format_driver_information (operating_system, 'v.84.0.4147.89', 'Stable 70', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.84.0.4147.89'),
   cls.format_driver_information (operating_system, 'v.83.0.4103.97', 'Stable 69', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.83.0.4103.97'),
   cls.format_driver_information (operating_system, 'v.81.0.4044.113', 'Stable 68', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.81.0.4044.113'),
   cls.format_driver_information (operating_system, 'v.80.0.3987.100', 'Stable 67', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.80.0.3987.100'),
   cls.format_driver_information (operating_system, 'v.79.0.3945.79', 'Stable 66', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.79.0.3945.79'),
   cls.format_driver_information (operating_system, 'v.78.0.3904.87', 'Stable 65', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.78.0.3904.87'),
   cls.format_driver_information (operating_system, 'v.77.0.3865.120', '64', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.77.0.3865.120'),
   cls.format_driver_information (operating_system, 'v.76.0.3809.132', '63', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.76.0.3809.132'),
   cls.format_driver_information (operating_system, 'v.75.0.3770.100', '62', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.75.0.3770.100'),
   cls.format_driver_information (operating_system, 'v.2.45', '60', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.45'),
   cls.format_driver_information (operating_system, 'v.2.42', '58', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.42'),
   cls.format_driver_information (operating_system, 'v.2.41', '57', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.41'),
   cls.format_driver_information (operating_system, 'v.2.40', '56', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.40'),
   cls.format_driver_information (operating_system, 'v.2.38', '55', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.38'),
   cls.format_driver_information (operating_system, 'v.2.37', '54', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.37'),
   cls.format_driver_information (operating_system, 'v.2.36', '53', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.36'),
   cls.format_driver_information (operating_system, 'v.2.35', '52', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.35'),
   cls.format_driver_information (operating_system, 'v.2.33', '50', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.33'),
   cls.format_driver_information (operating_system, 'v.2.32', '49', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.32'),
   cls.format_driver_information (operating_system, 'v.2.30', '48', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.30'),
   cls.format_driver_information (operating_system, 'v.2.29', '46', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.2.29'),
  ]
 @classmethod
 def format_chromedriver_list(cls, operating_system):
  driver_name = 'chromedriver'
  browser_name = 'Google Chrome'
  return [
   cls.format_driver_information (operating_system, '97.0.4692.20', '97', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '97.0.4692.20'),
   cls.format_driver_information (operating_system, '96.0.4664.45', '96', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '96.0.4664.45'),
   cls.format_driver_information (operating_system, '95.0.4638.69', '95', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '95.0.4638.69'),
   cls.format_driver_information (operating_system, '94.0.4606.113', '94', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '94.0.4606.113'),
   cls.format_driver_information (operating_system, '93.0.4577.63', '93', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '93.0.4577.63'),
   cls.format_driver_information (operating_system, '92.0.4515.107', '92', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '92.0.4515.107'),
   cls.format_driver_information (operating_system, '91.0.4472.101', '91', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '91.0.4472.101'),
   cls.format_driver_information (operating_system, '90.0.4430.24', '90', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '90.0.4430.24'),
   cls.format_driver_information (operating_system, '89.0.4389.23', '89', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '89.0.4389.23'),
   cls.format_driver_information (operating_system, '88.0.4324.96', '88', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '88.0.4324.96'),
   cls.format_driver_information (operating_system, '87.0.4280.88', '87', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '87.0.4280.88'),
   cls.format_driver_information (operating_system, '86.0.4240.22', '86', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '86.0.4240.22'),
   cls.format_driver_information (operating_system, '85.0.4183.87', '85', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '85.0.4183.87'),
   cls.format_driver_information (operating_system, '84.0.4147.30', '84', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '84.0.4147.30'),
   cls.format_driver_information (operating_system, '83.0.4103.39', '83', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '83.0.4103.39'),
   cls.format_driver_information (operating_system, '81.0.4044.138', '81', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '81.0.4044.138'),
   cls.format_driver_information (operating_system, '80.0.3987.106', '80', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '80.0.3987.106'),
   cls.format_driver_information (operating_system, '79.0.3945.36', '79', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '79.0.3945.36'),
   cls.format_driver_information (operating_system, '78.0.3904.105', '78', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '78.0.3904.105'),
   cls.format_driver_information (operating_system, '77.0.3865.40', '77', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '77.0.3865.40'),
   cls.format_driver_information (operating_system, '76.0.3809.126', '76', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '76.0.3809.126'),
   cls.format_driver_information (operating_system, '75.0.3770.140', '75', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '75.0.3770.140'),
   cls.format_driver_information (operating_system, '74.0.3729.6', '74', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '74.0.3729.6'),
   cls.format_driver_information (operating_system, '73.0.3683.68', '73', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '73.0.3683.68'),
   cls.format_driver_information (operating_system, '2.46', 'v71-73', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '2.46'),
   cls.format_driver_information (operating_system, '2.45', 'v70-72', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '2.45'),
   cls.format_driver_information (operating_system, '2.44', 'v69-71', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '2.44'),
   cls.format_driver_information (operating_system, '2.43', 'v69-71 (use chromedriver 2.44)', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '2.43'),
   cls.format_driver_information (operating_system, '2.42', 'v68-70', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '2.42'),
   cls.format_driver_information (operating_system, '2.41', 'v67-69', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '2.41'),
  ]
 @classmethod
 def format_bravedriver_list(cls, operating_system):
  driver_name = 'bravedriver (operadriver based)'
  browser_name = 'Brave Browser'
  return [
   cls.format_driver_information (operating_system, 'v.95.0.4638.54', '95', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.95.0.4638.54'),
   cls.format_driver_information (operating_system, 'v.94.0.4606.61', '94', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.94.0.4606.61'),
   cls.format_driver_information (operating_system, 'v.93.0.4577.63', '93', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.93.0.4577.63'),
   cls.format_driver_information (operating_system, 'v.92.0.4515.107', '92', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.92.0.4515.107'),
   cls.format_driver_information (operating_system, 'v.91.0.4472.77', '91', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.91.0.4472.77'),
   cls.format_driver_information (operating_system, 'v.90.0.4430.85', '90', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.90.0.4430.85'),
   cls.format_driver_information (operating_system, 'v.89.0.4389.82', '89', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.89.0.4389.82'),
   cls.format_driver_information (operating_system, 'v.88.0.4324.104', '88', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.88.0.4324.104'),
   cls.format_driver_information (operating_system, 'v.87.0.4280.67', '87', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.87.0.4280.67'),
   cls.format_driver_information (operating_system, 'v.86.0.4240.80', '86', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.86.0.4240.80'),
   cls.format_driver_information (operating_system, 'v.85.0.4183.102', '85', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.85.0.4183.102'),
   cls.format_driver_information (operating_system, 'v.84.0.4147.89', '84', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.84.0.4147.89'),
   cls.format_driver_information (operating_system, 'v.83.0.4103.97', '83', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.83.0.4103.97'),
   cls.format_driver_information (operating_system, 'v.81.0.4044.113', '81', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.81.0.4044.113'),
   cls.format_driver_information (operating_system, 'v.80.0.3987.100', '80', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.80.0.3987.100'),
   cls.format_driver_information (operating_system, 'v.79.0.3945.79', '79', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.79.0.3945.79'),
   cls.format_driver_information (operating_system, 'v.78.0.3904.87', '78', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.78.0.3904.87'),
   cls.format_driver_information (operating_system, 'v.77.0.3865.120', '77', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.77.0.3865.120'),
   cls.format_driver_information (operating_system, 'v.76.0.3809.132', '76', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.76.0.3809.132'),
   cls.format_driver_information (operating_system, 'v.75.0.3770.100', '75', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, 'v.75.0.3770.100')
  ]
 @classmethod
 def format_msedgedriver_list(cls, operating_system):
  driver_name = 'msedgedriver'
  browser_name = 'Microsoft Edge'
  return [
   cls.format_driver_information (operating_system, '98.0.1086.0', '98', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '98.0.1086.0'),
   cls.format_driver_information (operating_system, '97.0.1072.8', '97', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '97.0.1072.8'),
   cls.format_driver_information (operating_system, '96.0.1054.26', '96', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '96.0.1054.26'),
   cls.format_driver_information (operating_system, '95.0.1020.53', '95', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '95.0.1020.53'),
   cls.format_driver_information (operating_system, '94.0.992.58', '94', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '94.0.992.58'),
   cls.format_driver_information (operating_system, '93.0.961.52', '93', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '93.0.961.52'),
   cls.format_driver_information (operating_system, '92.0.902.84', '92', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '92.0.902.84'),
   cls.format_driver_information (operating_system, '91.0.864.71', '91', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '91.0.864.71'),
   cls.format_driver_information (operating_system, '90.0.818.66', '90', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '90.0.818.66'),
   cls.format_driver_information (operating_system, '89.0.774.77', '89', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '89.0.774.77'),
   cls.format_driver_information (operating_system, '88.0.705.74', '88', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '88.0.705.74'),
   cls.format_driver_information (operating_system, '87.0.669.0', '87', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '87.0.669.0'),
   cls.format_driver_information (operating_system, '86.0.622.58', '86', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '86.0.622.58'),
   cls.format_driver_information (operating_system, '85.0.564.68', '85', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '85.0.564.68'),
   cls.format_driver_information (operating_system, '84.0.524.0', '84', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '84.0.524.0'),
   cls.format_driver_information (operating_system, '83.0.478.58', '83', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '83.0.478.58'),
   cls.format_driver_information (operating_system, '82.0.459.1', '82', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '82.0.459.1'),
   cls.format_driver_information (operating_system, '81.0.409.0', '81', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '81.0.409.0'),
   cls.format_driver_information (operating_system, '80.0.361.111', '80', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '80.0.361.111'),
   cls.format_driver_information (operating_system, '79.0.313.0', '79', driver_name, browser_name),
   cls.format_download_command(driver_name, operating_system, '79.0.313.0')
  ]
 @staticmethod
 def format_safaridriver_list(operating_system):
  return {
   'macos': [
    'In order to run safaridriver, you need to enable remote automation. To do so, open up the Safari browser and in the menu bar, go to\n"Safari" -> "Preferences" -> "Advanced" tab -> click "Show develop menu in menu bar"\nOnce you do that, "Develop" should appear in your menu bar. Click on the "Develop" bar, and then enable "Allow Remote Automation" (should be near the bottom of the list).\n\nAfter doing that, try rerunning the last command!\n :)'
   ],
   'linux': [
    'Safari is probably not supported on Linux operating systems. In order for the safaridriver to run on a Linux OS, you will likely need to do many manual configurations. For this reason, this package does not provide built in support for safaridriver on a Linux OS.'
   ],
   'windows': [
    'Safari is probably not supported on Windows operating systems. In order for the safaridriver to run on a Windows OS, you will likely need to do many manual configurations. For this reason, this package does not provide built in support for safaridriver on a Windows OS.'
   ]
  }.get(operating_system)
 @staticmethod
 def format_driver_information(operating_system, version, major_version, driver, browser):
  return f'# {operating_system} {driver} {version} (supports {browser} version: {major_version})'
 @classmethod
 def format_download_command(cls, driver, operating_system, version):
  ### NOTE that Brave Browser doesn't have its own bravedriver, but since it's chromium we can just download operadriver (a chromium based driver) and use the corresponding operadriver for the Brave version (with it renamed to "bravedriver" in order to avoud conflict with different versions of Chrome/Opera and Brave installed at the same time) ###
  if operating_system.startswith('win'):
   if driver.startswith('geckodriver'): return cls.format_windows_download(f'{cls.url_prefix_geckodriver}/{version}/geckodriver-{version}-{operating_system}.zip', 'geckodriver')
   elif driver.startswith('bravedriver'): return cls.format_windows_download(f'{cls.url_prefix_operadriver}/{version}/operadriver_{operating_system}.zip', 'bravedriver')
   elif driver.startswith('msedgedriver'): return cls.format_windows_download(f'{cls.url_prefix_msedgedriver}/{version}/edgedriver_{operating_system}.zip', 'msedgedriver')
   else: return cls.format_windows_download(f'''{getattr(cls, 'url_prefix_' + driver)}/{version}/{driver}_{operating_system}.zip''', driver)
  else:
   if driver.startswith('geckodriver'): return cls.format_unix_download (f'{cls.url_prefix_geckodriver}/{version}/geckodriver-{version}-{operating_system}.tar.gz', 'geckodriver')
   elif driver.startswith('bravedriver'): return cls.format_unix_download (f'{cls.url_prefix_operadriver}/{version}/operadriver_{operating_system}.zip', 'bravedriver')
   elif driver.startswith('msedgedriver'): return cls.format_unix_download (f'{cls.url_prefix_msedgedriver}/{version}/edgedriver_{operating_system}.zip', 'msedgedriver')
   else: return cls.format_unix_download (f'''{getattr(cls, 'url_prefix_' + driver)}/{version}/{driver}_{operating_system}.zip''', driver)
 strip_component = '--strip-components=1'
 @classmethod
 def format_unix_download(cls, url, driver):
  if driver == 'operadriver': driver_specific_command = f'-C /usr/local/bin/ {cls.strip_component} && rm /usr/local/bin/sha512_sum'
  elif driver == 'bravedriver': driver_specific_command = f'-O > /usr/local/bin/{driver} {cls.strip_component}'
  else: driver_specific_command = '-C /usr/local/bin/'
  return f'curl -SL {url} | tar -xzvf - {driver_specific_command} && chmod +x /usr/local/bin/{driver}' + '\n'
 @classmethod
 def format_windows_download(cls, url, driver):
  drive = get_drive_letter()
  if driver == 'operadriver': driver_specific_command = rf'-C {drive}:\Windows {cls.strip_component} && del {drive}:\Windows\sha512_sum'
  elif driver == 'bravedriver': driver_specific_command = rf'-O > {drive}:\Windows\bravedriver.exe {cls.strip_component}'
  else: driver_specific_command = rf'-C {drive}:\Windows'
  return rf'curl -SL --ssl-no-revoke {url} -o {drive}:\Windows\{driver} && tar -xzvf {drive}:\Windows\{driver} {driver_specific_command} && del {drive}:\Windows\{driver}' + '\n'
 @staticmethod
 def display_browser_found_information(browser, full_version_number):
  print(f'\nFound an installed version of {browser}.\nYou are currently running {browser} version: {full_version_number}')
 @staticmethod
 def display_browser_not_found_information(browser, user_os):
  print(f'\nDid not find an installed version of {browser}.\nIf you DO have {browser} installed but it was not detected, it may be because your {browser} was installed in a non-default location.\nPlease modify the commands under the {browser} you want to use at https://github.com/slow-but-steady/yt-videos-list/blob/main/docs/dependencies_pseudo_json.txt for {user_os.title()}"\nIf you are unsure how to do that, please file an issue at https://github.com/slow-but-steady/yt-videos-list/issues and we will respond as soon as possible!')
 @classmethod
 def display_url_error(cls, error_message):
  print(f'{cls.offset}{cls.error}The url you provided could not be parsed properly. Please check the url you provided to make sure there are no typos!{cls.debugging_info}{error_message}{cls.offset}')
 def display_dependency_setup_instructions(self, user_driver, user_os):
  terminal_copy_paste_directions = 'Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T (or CTRL+N or CTRL+D depending on your keyboard/OS) from an active terminal session), and paste the command you just copied. Once you\'ve done that, you should be able to come back to this session and rerun the last command without an error!\n\n'
  if user_os != 'windows' and user_driver != 'safari':
   print(terminal_copy_paste_directions)
  geckodriver_download_instructions = '(The given command downloads a geckodriver ("Firefoxdriver") version that is compatible with Firefox versions ≥ 60. To see more information about the differences compared to older versions, please visit https://github.com/mozilla/geckodriver/releases)'
  operadriver_download_instructions = '(Your Opera browser version should match the "supports Opera ## release" below)'
  chromedriver_download_instructions = '(Your Chrome browser version should match the first numbers before the decimal place of the chromedriver version below)'
  bravedriver_download_instructions = '(Your Brave browser version should match the first numbers before the decimal place of the bravedriver version below. Note that there is currently no dedicated bravedriver, so this package substitutes the chromium operadriver.)'
  edgedriver_download_instructions = '(Your Edge browser version should match the first numbers before the decimal place of the msedgedriver version below)'
  if user_driver == 'firefox': print(geckodriver_download_instructions)
  elif user_driver == 'opera': print(operadriver_download_instructions)
  elif user_driver == 'safari': print('This is an MacOS specific driver.')
  elif user_driver == 'chrome': print(chromedriver_download_instructions)
  elif user_driver == 'brave': print(bravedriver_download_instructions)
  elif user_driver == 'edge': print(edgedriver_download_instructions)
  for driver_version_download in self.driver_downloads_for_os[user_driver][user_os]:
   print(driver_version_download)
  def display_more_dependency_information(user_driver):
   driver_name, driver_source_code_url, driver_releases_page_url, browser_name, browser_url = self.more_driver_info[user_driver]
   print(f'\n\n# For more information about the {driver_name}, please visit\n{driver_source_code_url}\n{driver_releases_page_url}{self.indent}{self.ds}(all supported versions)\n\nNOTE! You must also have the {browser_name} browser installed to use this. If you don\'t have it installed, install it from\n{browser_url}')
  if user_driver != 'safari':
   display_more_dependency_information(user_driver)
 @classmethod
 def display_selenium_dependency_error(cls, error_message):
  print(f'{cls.offset}{cls.offset}\n{cls.error}There was an error while trying to open up the remote selenium instance. The exact error was:\n{error_message}\nDon\'t worry though, this is an easy fix!')
 @classmethod
 def display_selenium_dependency_update_error(cls, error_message):
  print(f'{cls.error}Could not automatically update selenium dependencies!{cls.debugging_info}{error_message}{cls.offset}')
 @classmethod
 def display_selenium_unable_to_load_elements_error(cls, error_message):
  print(f'{cls.error}The page did not load elements! If you\'ve scraped many channels within a short period of time, please try rerunning the program after waiting to make sure YouTube isn\'t throttling your IP address!{cls.debugging_info}{error_message}{cls.offset}')
 @classmethod
 def display_possible_topic_channel_in_headless_error(cls, error_message):
  print(f'{cls.error}There was a problem running the selenium webdriver!\n\nTry running the program again with headless=False if you are currently running the program with headless=True.{cls.debugging_info}{error_message}{cls.offset}')
 @staticmethod
 def tell_user_to_download_driver(user_driver):
  print('\n' * 25 + '=' * 130)
  print(f'It looks like you don\'t have the correct Selenium dependency set up to run this program using the remote {user_driver}driver.\nThe version of your {user_driver.title()} browser - usually found by going to {user_driver.title()} -> \"About browser\" in the menu bar within a {user_driver.title()} window - should match the comment for the corresponding command.\nPlease download it using the relevant command from the list of commands below.\n')
 @classmethod
 def display_unable_to_update_driver_automatically(cls, user_driver):
  print('\n' + '*' * 81)
  print('*****Looks like the package could not automatically update the dependencies.*****')
  print('Please try running the following commands to update the package (newer package versions will support newer drivers) before retrying, and if that doesn\'t work, follow the directions given above.')
  print(f'pip{cls.ds}install -U yt-videos-list #Windows\npip3 install -U yt-videos-list #MacOS/Linux\n\n')
  print('If that does not work, try:')
  print(f'python{cls.ds}-m pip install -U yt-videos-list #Windows\npython3 -m pip install -U yt-videos-list #MacOS/Linux\n')
  print('If this still doesn\'t fix the problem, please try using a different driver or file an issue at https://github.com/slow-but-steady/yt-videos-list/issues')
  print(f'The problem is likely caused by trying to run yt_videos_list with an updated version of the driver you\'re trying to use than what yt_videos_list currently supports (we update the binaries a few weeks after the initial release to allow time for bug fixing). If this is the case, the version of the driver downloaded won\'t match the output of\n"You are currently running {user_driver} version: " above.\n')
  print('To see other drivers you can use (and other options), run:\n')
  print('import yt_videos_list\nhelp(yt_videos_list)')
  print('*' * 81)
 @classmethod
 def display_cookie_redirection(cls):
  print(f'{cls.offset}Redirected to consent.youtube.com!')
 @classmethod
 def display_blocking_cookie_consent(cls):
  print(f'Blocking consent for all cookies since program running with cookie_consent=False ...{cls.offset}')
 @classmethod
 def display_accepting_cookie_consent(cls):
  print(f'Accepting consent for all cookies since program running with cookie_consent=True ...{cls.offset}')
 @staticmethod
 def display_invalid_cookie_consent_option(cookie_consent):
  print(f'YouTube is redircting to youtube.consent.com, but you entered an invalid argument for the cookie_consent instance attrribute!\nPlease use cookie_consent=True or cookie_consent=False.\nYour current setting is: cookie_consent={cookie_consent}')
 @staticmethod
 def no_new_videos_found(pause_time):
  return f'No new videos were found since the last scroll. Waiting another {pause_time} seconds to see if more videos can be loaded....\n'
class ModuleMessage(Common):
 '''
 This class contains messages that are relevant for the package when it is being run as a module from within the Python interpreter (or another Python script).
 '''
 indent = ' ' * 4
 not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt OR md or all_video_data_in_memory attribute to True.\nThis program will now exit...'
 running_default_driver = '\nNo driver specified during ListCreator instantiation, so running program using the Firefox driver.'
 show_driver_options = f'''To use a different driver, specify the driver in the driver argument during the ListCreator instantiation. For example:
 {indent}lc = ListCreator(driver='firefox')
 {indent}lc = ListCreator(driver='opera')
 {indent}lc = ListCreator(driver='safari')
 {indent}lc = ListCreator(driver='chrome')
 {indent}lc = ListCreator(driver='brave')
 {indent}lc = ListCreator(driver='edge')'''
class ScriptMessage(Common):
 '''
 This class contains messages that relevant for the package it is being run as a module using the -m option from the CLI.
 '''
 not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt OR md setting TO FLAG.\nThis program will now exit...'
 running_default_driver = '\nNo driver flag used, so running program using the Firefox driver.'
 input_message = "What is the name of the YouTube channel you want to generate the list for?\n\nIf you're unsure, click on the channel and look at the URL.\nIt should be in the format:\nhttps://www.youtube.com/user/YourChannelName\nOR\nhttps://www.youtube.com/channel/YourChannelName\n\nSubstitute what you see for YourChannelName and type it in below:\n"
 show_driver_options = 'To use a different driver, specify the driver in the driver flag. For example:'
