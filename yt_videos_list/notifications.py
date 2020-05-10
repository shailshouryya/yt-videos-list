from .windows import get_drive_letter


class Common:
    '''
    This class contains messages that are common regardless of whether the package is being run as a module using the -m option from the CLI or as a module from within the Python interpreter (or another Python script).
    '''


    missing_url = 'create_list_for() missing 1 required positional argument: "url"'

    not_writing_to_any_files = '\nBased on your provided settings, yt_videos_list will not be writing to either a csv file or a txt file.'

    no_videos_found = 'No videos were found for the channel you provided. Are you sure you entered the url correctly?\n'
    no_new_videos_found = 'No new videos were found since the last scroll. Waiting another 0.6 seconds to see if more videos can be loaded....'
    invalid_response = 'The response you entered was invalid.'

    invalid_driver = 'The driver you specified is invalid. Please try rerunning the last command after specifying a valid driver. Supported drivers include:\n   Firefox\n   Opera\n   Safari\n   Chrome\n   Brave'

    unsupported_opera_headless = '\nHeadless mode is unsupported in OperaDriver. We are waiting on the Opera dev team to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_safari_headless = '\nHeadless mode is unsupported in SafariDriver. We are waiting on Apple to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_brave_headless = '\nHeadless mode is unsupported in BraveDriver. We are waiting for a Brave release that supports headless before offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_os = 'The system you are using is not yet supported. Please create an issue at https://github.com/Shail-Shouryya/yt_videos_list/issues\nThanks!'

    automated_driver_update = '\n=====> Now updating Selenium driver binaries and fixing any version incompatibility problems.<=====\nThis will update all corresponding Selenium drivers for browsers (which are installed in their default locations and) supported by the yt_videos_list package...'

    url_prefix_geckodriver  = 'https://github.com/mozilla/geckodriver/releases/download'
    url_prefix_operadriver  = 'https://github.com/operasoftware/operachromiumdriver/releases/download'
    url_prefix_chromedriver = 'https://chromedriver.storage.googleapis.com'


    def __init__(self):
        self.driver_downloads_for_os = {
            'firefox': {
                'macos': [
                    '# macos geckodriver (Firefoxdriver) v0.26.0',
                    self.format_macos_geckodriver_download_command('v0.26.0/')
                ],
                'linux': [
                    '# linux64 geckodriver (Firefoxdriver) v0.26.0',
                    self.format_linux_geckodriver_download_command('v0.26.0', '64'),
                    '# linux32 geckodriver (Firefoxdriver) v0.26.0',
                    self.format_linux_geckodriver_download_command('v0.26.0', '32')
                ],
                'windows': [
                    '# windows32 geckodriver (Firefoxdriver) v0.26.0',
                    self.format_windows_geckodriver_download_command('v0.26.0', '32'),
                    '# windows64 geckodriver (Firefoxdriver) v0.26.0',
                    self.format_windows_geckodriver_download_command('v0.26.0', '64')
                ]
            },
            'opera': {
                'macos' : [
                    '# mac64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_macos_operadriver_download_command('v.81.0.4044.113'),
                    '# mac64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_macos_operadriver_download_command('v.80.0.3987.100'),
                    '# mac64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_macos_operadriver_download_command('v.79.0.3945.79'),
                    '# mac64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_macos_operadriver_download_command('v.78.0.3904.87'),
                    '# mac64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_macos_operadriver_download_command('v.77.0.3865.120'),
                    '# mac64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_macos_operadriver_download_command('v.76.0.3809.132'),
                    '# mac64 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                    self.format_macos_operadriver_download_command('v.75.0.3770.100'),
                    '# mac64 Operadriver 2.45 (supports Opera 60 release)',
                    self.format_macos_operadriver_download_command('v.2.45'),
                    '# mac64 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_macos_operadriver_download_command('v.2.42'),
                    '# mac64 Operadriver 2.41 (supports Opera 57 release)',
                    self.format_macos_operadriver_download_command('v.2.41'),
                    '# mac64 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_macos_operadriver_download_command('v.2.40'),
                    '# mac64 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_macos_operadriver_download_command('v.2.38'),
                    '# mac64 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_macos_operadriver_download_command('v.2.37')
                ],
                'linux': [
                    '# linux64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_linux_operadriver_download_command('v.81.0.4044.113'),
                    '# linux64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_linux_operadriver_download_command('v.80.0.3987.100'),
                    '# linux64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_linux_operadriver_download_command('v.79.0.3945.79'),
                    '# linux64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_linux_operadriver_download_command('v.78.0.3904.87'),
                    '# linux64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_linux_operadriver_download_command('v.77.0.3865.120'),
                    '# linux64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_linux_operadriver_download_command('v.76.0.3809.132'),
                    '# linux64 Operadriver 75.0.3770.100 (supports Opera 62) release',
                    self.format_linux_operadriver_download_command('v.75.0.3770.100'),
                    '# linux64 Operadriver 2.45 (supports Opera 60 release)',
                    self.format_linux_operadriver_download_command('v.2.45'),
                    '# linux64 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_linux_operadriver_download_command('v.2.42'),
                    '# linux64 Operadriver 2.41 (supports Opera 57) release',
                    self.format_linux_operadriver_download_command('v.2.41'),
                    '# linux64 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_linux_operadriver_download_command('v.2.40'),
                    '# linux64 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_linux_operadriver_download_command('v.2.38'),
                    '# linux64 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_linux_operadriver_download_command('v.2.37')
                ],
                'windows': [
                    '# windows32 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_windows_operadriver_download_command('v.81.0.4044.113/', '32'),
                    '# windows32 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_windows_operadriver_download_command('v.80.0.3987.100/', '32'),
                    '# windows32 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_windows_operadriver_download_command('v.79.0.3945.79/', '32'),
                    '# windows32 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_windows_operadriver_download_command('v.78.0.3904.87/', '32'),
                    '# windows32 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_windows_operadriver_download_command('v.77.0.3865.120/', '32'),
                    '# windows32 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_windows_operadriver_download_command('v.76.0.3809.132/', '32'),
                    '# windows32 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                    self.format_windows_operadriver_download_command('v.75.0.3770.100/', '32'),
                    '# windows32 Operadriver 2.45 (supports Opera 60) release',
                    self.format_windows_operadriver_download_command('v.2.45/', '32'),
                    '# windows32 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_windows_operadriver_download_command('v.2.42/', '32'),
                    '# windows32 Operadriver 2.41 (supports Opera 57 release)',
                    self.format_windows_operadriver_download_command('v.2.41/', '32'),
                    '# windows32 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_windows_operadriver_download_command('v.2.40/', '32'),
                    '# windows32 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_windows_operadriver_download_command('v.2.38/', '32'),
                    '# windows32 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_windows_operadriver_download_command('v.2.37/', '32') + '\n',

                    '# windows64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_windows_operadriver_download_command('v.81.0.4044.113', '64'),
                    '# windows64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_windows_operadriver_download_command('v.80.0.3987.100', '64'),
                    '# windows64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_windows_operadriver_download_command('v.79.0.3945.79', '64'),
                    '# windows64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_windows_operadriver_download_command('v.78.0.3904.87', '64'),
                    '# windows64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_windows_operadriver_download_command('v.77.0.3865.120', '64'),
                    '# windows64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_windows_operadriver_download_command('v.76.0.3809.132', '64'),
                    '# windows64 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                    self.format_windows_operadriver_download_command('v.75.0.3770.100', '64'),
                    '# windows64 Operadriver 2.45 (supports Opera 60 release)',
                    self.format_windows_operadriver_download_command('v.2.45', '64'),
                    '# windows64 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_windows_operadriver_download_command('v.2.42', '64'),
                    '# windows64 Operadriver 2.41 (supports Opera 57 release)',
                    self.format_windows_operadriver_download_command('v.2.41', '64'),
                    '# windows64 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_windows_operadriver_download_command('v.2.40', '64'),
                    '# windows64 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_windows_operadriver_download_command('v.2.38', '64'),
                    '# windows64 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_windows_operadriver_download_command('v.2.37', '64')
                ]
            },
            'safari': {
                'macos' : [
                    'In order to run safaridriver, you need to enable remote automation. To do so, open up the Safari browser and in the menu bar, go to\n"Safari" -> "Preferences" -> "Advanced" tab -> click "Show develop menu in menu bar"\nOnce you do that, "Develop" should appear in your menu bar. Click on the "Develop" bar, and then enable "Allow Remote Automation" (should be near the bottom of the list).\n\nAfter doing that, try rerunning the last command!\n :)'
                ],
                'linux': [
                    'Safari is probably not supported on Linux operating systems. In order for the safaridriver to run on a Linux OS, you will likely need to do many manual configurations. For this reason, this package does not provide built in support for safaridriver on a Linux OS.'
                ],
                'windows': [
                    'Safari is probably not supported on Windows operating systems. In order for the safaridriver to run on a Windows OS, you will likely need to do many manual configurations. For this reason, this package does not provide built in support for safaridriver on a Windows OS.'
                ]
            },
            'chrome': {
                'macos' : [
                    '# mac64 Chromedriver 81.0.4044.69',
                    self.format_macos_chromedriver_download_command('81.0.4044.69'),
                    '# mac64 Chromedriver 80.0.3987.106',
                    self.format_macos_chromedriver_download_command('80.0.3987.106'),
                    '# mac64 Chromedriver 79.0.3945.36',
                    self.format_macos_chromedriver_download_command('79.0.3945.36'),
                    '# mac64 Chromedriver 78.0.3904.105',
                    self.format_macos_chromedriver_download_command('78.0.3904.105'),
                    '# mac64 Chromedriver 77.0.3865.40',
                    self.format_macos_chromedriver_download_command('77.0.3865.40'),
                    '# mac64 Chromedriver 76.0.3809.126',
                    self.format_macos_chromedriver_download_command('76.0.3809.126'),
                    '# mac64 Chromedriver 75.0.3770.140',
                    self.format_macos_chromedriver_download_command('75.0.3770.140'),
                    '# mac64 Chromedriver 74.0.3729.6',
                    self.format_macos_chromedriver_download_command('74.0.3729.6'),
                    '# mac64 Chromedriver 73.0.3683.68',
                    self.format_macos_chromedriver_download_command('73.0.3683.68'),
                    '# mac64 Chromedriver 2.46 (Supports Chrome v71-73)',
                    self.format_macos_chromedriver_download_command('2.46')
                ],
                'linux': [
                    '# linux64 Chromedriver 81.0.4044.69',
                    self.format_linux_chromedriver_download_command('81.0.4044.69'),
                    '# linux64 Chromedriver 80.0.3987.106',
                    self.format_linux_chromedriver_download_command('80.0.3987.106'),
                    '# linux64 Chromedriver 79.0.3945.36',
                    self.format_linux_chromedriver_download_command('79.0.3945.36'),
                    '# linux64 Chromedriver 78.0.3904.105',
                    self.format_linux_chromedriver_download_command('78.0.3904.105'),
                    '# linux64 Chromedriver 77.0.3865.40',
                    self.format_linux_chromedriver_download_command('77.0.3865.40'),
                    '# linux64 Chromedriver 76.0.3809.126',
                    self.format_linux_chromedriver_download_command('76.0.3809.126'),
                    '# linux64 Chromedriver 75.0.3770.140',
                    self.format_linux_chromedriver_download_command('75.0.3770.140'),
                    '# linux64 Chromedriver 74.0.3729.6',
                    self.format_linux_chromedriver_download_command('74.0.3729.6'),
                    '# linux64 Chromedriver 73.0.3683.68',
                    self.format_linux_chromedriver_download_command('73.0.3683.68'),
                    '# linux64 Chromedriver 2.46 (Supports Chrome v71-73)',
                    self.format_linux_chromedriver_download_command('2.46')
                ],
                'windows': [
                    '# win32 Chromedriver 81.0.4044.69',
                    self.format_windows_chromedriver_download_command('81.0.4044.69'),
                    '# win32 Chromedriver 80.0.3987.106',
                    self.format_windows_chromedriver_download_command('80.0.3987.106'),
                    '# win32 Chromedriver 79.0.3945.36',
                    self.format_windows_chromedriver_download_command('79.0.3945.36'),
                    '# win32 Chromedriver 78.0.3904.105',
                    self.format_windows_chromedriver_download_command('78.0.3904.105'),
                    '# win32 Chromedriver 77.0.3865.40',
                    self.format_windows_chromedriver_download_command('77.0.3865.40'),
                    '# win32 Chromedriver 76.0.3809.126',
                    self.format_windows_chromedriver_download_command('76.0.3809.126'),
                    '# win32 Chromedriver 75.0.3770.140',
                    self.format_windows_chromedriver_download_command('75.0.3770.140'),
                    '# win32 Chromedriver 74.0.3729.6',
                    self.format_windows_chromedriver_download_command('74.0.3729.6'),
                    '# win32 Chromedriver 73.0.3683.68',
                    self.format_windows_chromedriver_download_command('73.0.3683.68'),
                    '# win32 Chromedriver 2.46 (Supports Chrome v71-73)',
                    self.format_windows_chromedriver_download_command('2.46')
                ]
            },
            'brave': {
                'macos' : [
                    '# mac64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_macos_bravedriver_download_command('v.81.0.4044.113'),
                    '# mac64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_macos_bravedriver_download_command('v.80.0.3987.100'),
                    '# mac64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_macos_bravedriver_download_command('v.79.0.3945.79'),
                    '# mac64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_macos_bravedriver_download_command('v.78.0.3904.87'),
                    '# mac64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_macos_bravedriver_download_command('v.77.0.3865.120'),
                    '# mac64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_macos_bravedriver_download_command('v.76.0.3809.132'),
                    '# mac64 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                    self.format_macos_bravedriver_download_command('v.75.0.3770.100'),
                    '# mac64 Operadriver 2.45 (supports Opera 60 release)',
                    self.format_macos_bravedriver_download_command('v.2.45'),
                    '# mac64 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_macos_bravedriver_download_command('v.2.42'),
                    '# mac64 Operadriver 2.41 (supports Opera 57 release)',
                    self.format_macos_bravedriver_download_command('v.2.41'),
                    '# mac64 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_macos_bravedriver_download_command('v.2.40'),
                    '# mac64 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_macos_bravedriver_download_command('v.2.38'),
                    '# mac64 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_macos_bravedriver_download_command('v.2.37')
                ],
                'linux': [
                    '# linux64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_linux_bravedriver_download_command('v.81.0.4044.113'),
                    '# linux64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_linux_bravedriver_download_command('v.80.0.3987.100'),
                    '# linux64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_linux_bravedriver_download_command('v.79.0.3945.79'),
                    '# linux64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_linux_bravedriver_download_command('v.78.0.3904.87'),
                    '# linux64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_linux_bravedriver_download_command('v.77.0.3865.120'),
                    '# linux64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_linux_bravedriver_download_command('v.76.0.3809.132'),
                    '# linux64 Operadriver 75.0.3770.100 (supports Opera 62) release',
                    self.format_linux_bravedriver_download_command('v.75.0.3770.100'),
                    '# linux64 Operadriver 2.45 (supports Opera 60 release)',
                    self.format_linux_bravedriver_download_command('v.2.45'),
                    '# linux64 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_linux_bravedriver_download_command('v.2.42'),
                    '# linux64 Operadriver 2.41 (supports Opera 57) release',
                    self.format_linux_bravedriver_download_command('v.2.41'),
                    '# linux64 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_linux_bravedriver_download_command('v.2.40'),
                    '# linux64 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_linux_bravedriver_download_command('v.2.38'),
                    '# linux64 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_linux_bravedriver_download_command('v.2.37')
                ],
                'windows': [
                    '# windows64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                    self.format_windows_bravedriver_download_command('v.81.0.4044.113'),
                    '# windows64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                    self.format_windows_bravedriver_download_command('v.80.0.3987.100'),
                    '# windows64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                    self.format_windows_bravedriver_download_command('v.79.0.3945.79'),
                    '# windows64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                    self.format_windows_bravedriver_download_command('v.78.0.3904.87'),
                    '# windows64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                    self.format_windows_bravedriver_download_command('v.77.0.3865.120'),
                    '# windows64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                    self.format_windows_bravedriver_download_command('v.76.0.3809.132'),
                    '# windows64 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                    self.format_windows_bravedriver_download_command('v.75.0.3770.100'),
                    '# windows64 Operadriver 2.45 (supports Opera 60 release)',
                    self.format_windows_bravedriver_download_command('v.2.45'),
                    '# windows64 Operadriver 2.42 (supports Opera 58 release)',
                    self.format_windows_bravedriver_download_command('v.2.42'),
                    '# windows64 Operadriver 2.41 (supports Opera 57 release)',
                    self.format_windows_bravedriver_download_command('v.2.41'),
                    '# windows64 Operadriver 2.40 (supports Opera 56 release)',
                    self.format_windows_bravedriver_download_command('v.2.40'),
                    '# windows64 Operadriver 2.38 (supports Opera 55 release)',
                    self.format_windows_bravedriver_download_command('v.2.38'),
                    '# windows64 Operadriver 2.37 (supports Opera 54 release)',
                    self.format_windows_bravedriver_download_command('v.2.37')
                ]
            }
        }

    more_driver_info = {
        # 'driver': ['driverName', 'url for more driver info',  'url for driver releases', 'browser name', 'url for browser download']
        'firefox': ['geckodriver',  'https://github.com/mozilla/geckodriver',                    'https://github.com/mozilla/geckodriver/releases',                'Mozilla Firefox', 'https://www.mozilla.org/en-US/firefox/new/'],
        'opera':   ['operadriver',  'https://github.com/operasoftware/operachromiumdriver',      'https://github.com/operasoftware/operachromiumdriver/releases',  'Opera',           'https://www.opera.com/'],
        'chrome':  ['chromedriver', 'https://sites.google.com/a/chromium.org/chromedriver/home', 'https://sites.google.com/a/chromium.org/chromedriver/downloads', 'Chrome',          'https://www.google.com/chrome/']
    }

    @classmethod
    def format_macos_geckodriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_geckodriver}/{binary_version}/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin/' + '\n'

    @classmethod
    def format_linux_geckodriver_download_command(cls, binary_version, system):
        return f'curl -SL {cls.url_prefix_geckodriver}/{binary_version}/geckodriver-v0.26.0-linux{system}.tar.gz | tar -xzvf - -C /usr/local/bin/' + '\n'

    @classmethod
    def format_windows_geckodriver_download_command(cls, binary_version, system):
        drive = get_drive_letter()
        return fr'curl -SL {cls.url_prefix_geckodriver}/{binary_version}/geckodriver-v0.26.0-win{system}.zip -o {drive}:\Windows\geckodriver && tar -xzvf {drive}:\Windows\geckodriver -C {drive}:\Windows && del {drive}:\Windows\geckodriver' + '\n'


    @classmethod
    def format_macos_operadriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_operadriver}/{binary_version}/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum' + '\n'

    @classmethod
    def format_linux_operadriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_operadriver}/{binary_version}/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum' + '\n'

    @classmethod
    def format_windows_operadriver_download_command(cls, binary_version, system):
        drive = get_drive_letter()
        return fr'curl -SL {cls.url_prefix_operadriver}/{binary_version}/operadriver_win{system}.zip -o {drive}:\Windows\operadriver && tar -xzvf {drive}:\Windows\operadriver --strip-components=1 -C {drive}:\Windows && del {drive}:\Windows\operadriver && del {drive}:\Windows\sha512_sum' + '\n'

    @classmethod
    def format_macos_chromedriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_chromedriver}/{binary_version}/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/' + '\n'

    @classmethod
    def format_linux_chromedriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_chromedriver}/{binary_version}/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/' + '\n'

    @classmethod
    def format_windows_chromedriver_download_command(cls, binary_version):
        drive = get_drive_letter()
        return fr'curl -SL {cls.url_prefix_chromedriver}/{binary_version}/chromedriver_win32.zip -o {drive}:\Windows\chromedriver && tar -xzvf {drive}:\Windows\chromedriver -C {drive}:\Windows && del {drive}:\Windows\chromedriver' + '\n'

    ### Brave Browser doesn't have its own bravedriver, but since it's chromium we can just download the chromedriver and use the corresponding chromedriver for the Brave version (with it renamed to "bravedriver" in order to avoud conflict with different versions of Chrome and Brave installed at the same time) ###
    @classmethod
    def format_macos_bravedriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_operadriver}/{binary_version}/operadriver_mac64.zip | tar -xzvf - --strip-components=1 -O > /usr/local/bin/bravedriver && chmod +x /usr/local/bin/bravedriver && rm /usr/local/bin/sha512_sum' + '\n'

    @classmethod
    def format_linux_bravedriver_download_command(cls, binary_version):
        return f'curl -SL {cls.url_prefix_operadriver}/{binary_version}/operadriver_linux64.zip | tar -xzvf - --strip-components=1 -O > /usr/local/bin/bravedriver && chmod +x /usr/local/bin/bravedriver && rm /usr/local/bin/sha512_sum' + '\n'

    @classmethod
    def format_windows_bravedriver_download_command(cls, binary_version):
        drive  = get_drive_letter()
        system = 64
        return fr'curl -SL {cls.url_prefix_operadriver}/{binary_version}/operadriver_win{system}.zip -o {drive}:\Windows\bravedriver && tar -xzvf {drive}:\Windows\bravedriver --strip-components=1 -O > {drive}:\Windows\bravedriver.exe && del {drive}:\Windows\bravedriver && del {drive}:\Windows\sha512_sum' + '\n'


    @staticmethod
    def display_browser_found_information(browser, full_version_number):
        print(f'\nFound an installed version of {browser}.\nYou are currently running {browser} version: {full_version_number}')

    @staticmethod
    def display_browser_not_found_information(browser, user_os):
        print(f'\nDid not find an installed version of {browser}.\nIf you DO have {browser} installed but it was not detected, it may be because your {browser} was installed in a non-default location.\nPlease follow the directions under the {browser} section at https://github.com/Shail-Shouryya/yt_videos_list/extra/README.md for "Setting up your Selenium dependencies for {user_os.title()}"\n')


    def display_dependency_setup_instructions(self, user_driver, user_os):
        terminal_copy_paste_directions = 'Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T (or CTRL+N or CTRL+D depending on your keyboard/OS) from an active terminal session), and paste the command you just copied. Once you\'ve done that, you should be able to come back to this session and rerun the last command without an error!\n\n'

        if user_os != 'windows' and user_driver != 'safari':
            print(terminal_copy_paste_directions)

        geckodriver_download_instructions = '(The given command downloads a geckodriver ("Firefoxdriver") version that is compatible with Firefox versions ≥ 60. To see more information about the differences compared to older versions, please visit https://github.com/mozilla/geckodriver/releases)'
        operadriver_download_instructions  = '(Your Opera browser version should match the "supports Opera ## release" below)'
        chromedriver_download_instructions = '(Your Chrome browser version should match the first numbers before the decimal place of the chromedriver version below)'
        bravedriver_download_instructions  = '(Your Brave browser version should match the first numbers before the decimal place of the chromedriver version below'

        if   user_driver == 'firefox':  print(geckodriver_download_instructions)
        elif user_driver == 'opera':    print(operadriver_download_instructions)
        elif user_driver == 'safari':   print('This is an MacOS specific driver.')
        elif user_driver == 'chrome':   print(chromedriver_download_instructions)
        elif user_driver == 'brave':    print(bravedriver_download_instructions)

        for driver_version_download in self.driver_downloads_for_os[user_driver][user_os]:
            print(driver_version_download)

        def display_more_dependency_information(user_driver):
            print(f'\n\n# For more information about the {self.more_driver_info[user_driver][0]}, please visit\n{self.more_driver_info[user_driver][1]}\n{self.more_driver_info[user_driver][2]}      (all supported versions)\n\nNOTE! You must also have the {self.more_driver_info[user_driver][3]} browser installed to use this. If you don\'t have it installed, install it from\n{self.more_driver_info[user_driver][4]}')

        if user_driver != 'safari':
            display_more_dependency_information(user_driver)

    @staticmethod
    def display_selenium_dependency_error(error_message):
        print(f'\n\n\n\n\n\n\nThere was an error while trying to open up the remote selenium instance. The exact error was:\n{error_message}\nDon\'t worry though, this is an easy fix!')

    @staticmethod
    def tell_user_to_download_driver(user_driver):
        print(f'\nIt looks like you don\'t have the correct Selenium dependency set up to run this program using the remote {user_driver}driver.\nThe version of your {user_driver.title()} browser - usually found by going to {user_driver.title()} -> \"About browser\" in the menu bar within a {user_driver.title()} window - should match the comment for the corresponding command.\nPlease download it using the relevant command from the list of commands below.\n')

    @staticmethod
    def display_file_already_exists_warning(filename):
        print(f'\nWARNING! A file with the name {filename} already exists in the current directory.')

    @staticmethod
    def display_file_already_exists_prompt(filename):
        print(f'If you wish to proceed and overwrite {filename}, type "proceed", otherwise move the file to a different directory on your computer OR rename the file before typing "proceed"')
        print(f'If you wish to skip the creation of {filename}, type "skip"')



class ModuleMessage(Common):
    '''
    This class contains messages that are relevant for the package when it is being run as a module from within the Python interpreter (or another Python script).
    '''


    url_argument_usage = '\n\n    Please copy and paste the url to the YouTube channel you want to scrape as the first argument (make sure you put quotes around the url) and rerun this method!\n    EXAMPLES:\n        lc.create_list_for("https://www.youtube.com/user/schafer5")\n        lc.create_list_for(url="https://www.youtube.com/user/schafer5")\n        lc.create_list_for(url="https://www.youtube.com/user/schafer5", file_name="CoreySchafer")\n        lc.create_list_for("https://www.youtube.com/user/schafer5", "CoreySchafer")'

    not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt setting to True.\nThis program will now exit...'

    running_default_driver = '\nNo driver specified during ListCreator instantiation, so running program using the Firefox driver.'
    run_in_headless_hint = '\nAdvanced usage: you can run this program in headless mode with the optional "headless" parameter set to True to speed up execution slightly:'
    run_in_headless_example = '    lc = ListCreator(headless=True)\n\n\n'

    file_already_exists = 'This error indicates that a file of this name already exists in the current directory. If you want to overwrite this file, run the create_list_for method again with the optional parameter "write_format" set to "w"'
    file_already_exists_rerun_usage = 'Example usage:\n lc.create_list_for(write_format="w")\n'

    show_driver_options = 'To use a different driver, specify the driver in the driver argument during the ListCreator instantiation. For example:' + \
        "\n    lc = ListCreator(driver='firefox')" + \
        "\n    lc = ListCreator(driver='opera')" + \
        "\n    lc = ListCreator(driver='safari')" + \
        "\n    lc = ListCreator(driver='chrome')" + \
        "\n    lc = ListCreator(driver='brave')"



class ScriptMessage(Common):
    '''
    This class contains messages that relevant for the package it is being run as a module using the -m option from the CLI.
    '''


    not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt setting TO FLAG.\nThis program will now exit...'

    running_default_driver = '\nNo driver flag used, so running program using the Firefox driver.'

    input_message = "What is the name of the YouTube channel you want to generate the list for?\n\nIf you're unsure, click on the channel and look at the URL.\nIt should be in the format:\nhttps://www.youtube.com/user/YourChannelName\nOR\nhttps://www.youtube.com/channel/YourChannelName\n\nSubstitute what you see for YourChannelName and type it in below:\n"

    show_driver_options = 'To use a different driver, specify the driver in the driver flag. For example:'
