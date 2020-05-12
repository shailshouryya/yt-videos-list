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

    unsupported_edge = 'ERROR! Selenium automation with msedgedriver (edge) is not yet supported on your platform. Please use a different browser.'

    unsupported_opera_headless = '\nHeadless mode is unsupported in OperaDriver. We are waiting on the Opera dev team to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_safari_headless = '\nHeadless mode is unsupported in SafariDriver. We are waiting on Apple to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_brave_headless = '\nHeadless mode is unsupported in BraveDriver. We are waiting for a Brave release that supports headless before offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_edge_headless = '\nHeadless mode is unsupported in EdgeDriver. We are waiting for on the Miscrosoft Edge release to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_os = 'The system you are using is not yet supported. Please create an issue at https://github.com/Shail-Shouryya/yt_videos_list/issues\nThanks!'

    automated_driver_update = '\n=====> Now updating Selenium driver binaries and fixing any version incompatibility problems.<=====\nThis will update all corresponding Selenium drivers for browsers (which are installed in their default locations and) supported by the yt_videos_list package...'

    url_prefix_geckodriver  = 'https://github.com/mozilla/geckodriver/releases/download'
    url_prefix_operadriver  = 'https://github.com/operasoftware/operachromiumdriver/releases/download'
    url_prefix_chromedriver = 'https://chromedriver.storage.googleapis.com'
    url_prefix_msedgedriver = 'https://msedgedriver.azureedge.net'


    def __init__(self):
        self.driver_downloads_for_os = {
            'firefox': {
                'macos':   self.create_list_for('macos',   'geckodriver'),
                'linux':   self.create_list_for('linux64', 'geckodriver') + self.create_list_for('linux32', 'geckodriver'),
                'windows': self.create_list_for('win32',   'geckodriver') + self.create_list_for('win64',   'geckodriver')
            },
            'opera': {
                'macos':   self.create_list_for('mac64',   'operadriver'),
                'linux':   self.create_list_for('linux64', 'operadriver'),
                'windows': self.create_list_for('win32',   'operadriver') + self.create_list_for('win64',   'operadriver')
            },
            'safari': {
                'macos':   self.create_list_for('macos',   'safaridriver'),
                'linux':   self.create_list_for('linux',   'safaridriver'),
                'windows': self.create_list_for('windows', 'safaridriver')
            },
            'chrome': {
                'macos':   self.create_list_for('mac64',   'chromedriver'),
                'linux':   self.create_list_for('linux64', 'chromedriver'),
                'windows': self.create_list_for('win32',   'chromedriver')
            },
            'brave': {
                'macos':   self.create_list_for('mac64',   'bravedriver'),
                'linux':   self.create_list_for('linux64', 'bravedriver'),
                'windows': self.create_list_for('win64',   'bravedriver')
            },
            'edge': {
                'macos':   self.create_list_for('mac64', 'msedgedriver'),
                'linux':   ['There is currently no dedicated msedgedriver for Linux.\nHere are possible commands for an arm64 operating system.\nPlease visit https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ for more information.'] + \
                           self.create_list_for('arm64', 'msedgedriver'),
                'windows': self.create_list_for('win32', 'msedgedriver') + self.create_list_for('win64',   'msedgedriver')
            }
        }

    more_driver_info = {
        # 'driver': ['driverName', 'url for more driver info',  'url for driver releases', 'browser name', 'url for browser download']
        'firefox': ['geckodriver',  'https://github.com/mozilla/geckodriver',                                'https://github.com/mozilla/geckodriver/releases',                                                  'Mozilla Firefox', 'https://www.mozilla.org/en-US/firefox/new/'],
        'opera':   ['operadriver',  'https://github.com/operasoftware/operachromiumdriver',                  'https://github.com/operasoftware/operachromiumdriver/releases',                                    'Opera',           'https://www.opera.com/'],
        'chrome':  ['chromedriver', 'https://sites.google.com/a/chromium.org/chromedriver/home',             'https://sites.google.com/a/chromium.org/chromedriver/downloads',                                   'Google Chrome',   'https://www.google.com/chrome/'],
        'brave':   ['bravedriver',  'https://github.com/operasoftware/operachromiumdriver',                  'https://github.com/operasoftware/operachromiumdriver/releases',                                    'Brave',           'https://brave.com/'],
        'edge':    ['msedgedriver', 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/', 'https://github.com/MicrosoftDocs/edge-developer/blob/master/microsoft-edge/webdriver-chromium.md', 'Microsoft Edge',  'https://www.microsoft.com/en-us/edge']
    }

    @classmethod
    def create_list_for(cls, operating_system, driver):
        formatter_function = getattr(cls, f'format_{driver}_list')
        return formatter_function(operating_system)

    @classmethod
    def format_geckodriver_list(cls, operating_system):
        return [
            cls.format_driver_information(operating_system, 'geckodriver', 'Mozilla Firefox', 'v0.26.0', '≥ 60'),
            cls.format_geckodriver_download_command(operating_system, 'v0.26.0')
        ]

    @classmethod
    def format_operadriver_list(cls, operating_system):
        return [
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.81.0.4044.113', 'Stable 68'),
            cls.format_operadriver_download_command(operating_system, 'v.81.0.4044.113'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.80.0.3987.100', 'Stable 67'),
            cls.format_operadriver_download_command(operating_system, 'v.80.0.3987.100'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.79.0.3945.79', 'Stable 66'),
            cls.format_operadriver_download_command(operating_system, 'v.79.0.3945.79'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.78.0.3904.87', 'Stable 65'),
            cls.format_operadriver_download_command(operating_system, 'v.78.0.3904.87'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.77.0.3865.120', '64'),
            cls.format_operadriver_download_command(operating_system, 'v.77.0.3865.120'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.76.0.3809.132', '63'),
            cls.format_operadriver_download_command(operating_system, 'v.76.0.3809.132'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.75.0.3770.100', '62'),
            cls.format_operadriver_download_command(operating_system, 'v.75.0.3770.100'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.2.45', '60'),
            cls.format_operadriver_download_command(operating_system, 'v.2.45'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.2.42', '58'),
            cls.format_operadriver_download_command(operating_system, 'v.2.42'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.2.41', '57'),
            cls.format_operadriver_download_command(operating_system, 'v.2.41'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.2.40', '56'),
            cls.format_operadriver_download_command(operating_system, 'v.2.40'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.2.38', '55'),
            cls.format_operadriver_download_command(operating_system, 'v.2.38'),
            cls.format_driver_information(operating_system, 'operadriver', 'Opera', 'v.2.37', '54'),
            cls.format_operadriver_download_command(operating_system, 'v.2.37')
        ]

    @classmethod
    def format_chromedriver_list(cls, operating_system):
        return [
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '81.0.4044.69', 81),
            cls.format_chromedriver_download_command(operating_system, '81.0.4044.69'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '80.0.3987.106', 80),
            cls.format_chromedriver_download_command(operating_system, '80.0.3987.106'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '79.0.3945.36', 79),
            cls.format_chromedriver_download_command(operating_system, '79.0.3945.36'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '78.0.3904.105', 78),
            cls.format_chromedriver_download_command(operating_system, '78.0.3904.105'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '77.0.3865.40', 77),
            cls.format_chromedriver_download_command(operating_system, '77.0.3865.40'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '76.0.3809.126', 76),
            cls.format_chromedriver_download_command(operating_system, '76.0.3809.126'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '75.0.3770.140', 75),
            cls.format_chromedriver_download_command(operating_system, '75.0.3770.140'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '74.0.3729.6', 74),
            cls.format_chromedriver_download_command(operating_system, '74.0.3729.6'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '73.0.3683.68', 73),
            cls.format_chromedriver_download_command(operating_system, '73.0.3683.68'),
            cls.format_driver_information(operating_system, 'chromedriver', 'Google Chrome', '2.46', 'v71-73'),
            cls.format_chromedriver_download_command(operating_system, '2.46')
        ]

    @classmethod
    def format_bravedriver_list(cls, operating_system):
        return [
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)', 'v.81.0.4044.113', '81'),
            cls.format_bravedriver_download_command(operating_system, 'v.81.0.4044.113'),
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)','v.80.0.3987.100', '80'),
            cls.format_bravedriver_download_command(operating_system, 'v.80.0.3987.100'),
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)', 'v.79.0.3945.79', '79'),
            cls.format_bravedriver_download_command(operating_system, 'v.79.0.3945.79'),
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)', 'v.78.0.3904.87', '78'),
            cls.format_bravedriver_download_command(operating_system, 'v.78.0.3904.87'),
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)', 'v.77.0.3865.120', '77'),
            cls.format_bravedriver_download_command(operating_system, 'v.77.0.3865.120'),
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)', 'v.76.0.3809.132', '76'),
            cls.format_bravedriver_download_command(operating_system, 'v.76.0.3809.132'),
            cls.format_driver_information(operating_system, 'bravedriver', 'Brave Browser (Chromium)', 'v.75.0.3770.100', '75'),
            cls.format_bravedriver_download_command(operating_system, 'v.75.0.3770.100')
        ]

    @classmethod
    def format_msedgedriver_list(cls, operating_system):
        return [
            cls.format_driver_information(operating_system, 'msedgedriver', 'Microsoft Edge', '81.0.409.0', 81),
            cls.format_msedgedriver_download_command(operating_system, '81.0.409.0'),
            cls.format_driver_information(operating_system, 'msedgedriver', 'Microsoft Edge', '80.0.361.111', 80),
            cls.format_msedgedriver_download_command(operating_system, '80.0.361.111'),
            cls.format_driver_information(operating_system, 'msedgedriver', 'Microsoft Edge', '79.0.313.0', 79),
            cls.format_msedgedriver_download_command(operating_system, '79.0.313.0')
        ]

    @classmethod
    def format_safaridriver_list(cls, operating_system):
        if operating_system == 'macos':
            return [
                'In order to run safaridriver, you need to enable remote automation. To do so, open up the Safari browser and in the menu bar, go to\n"Safari" -> "Preferences" -> "Advanced" tab -> click "Show develop menu in menu bar"\nOnce you do that, "Develop" should appear in your menu bar. Click on the "Develop" bar, and then enable "Allow Remote Automation" (should be near the bottom of the list).\n\nAfter doing that, try rerunning the last command!\n :)'
            ]
        elif operating_system == 'linux':
            return [
                'Safari is probably not supported on Linux operating systems. In order for the safaridriver to run on a Linux OS, you will likely need to do many manual configurations. For this reason, this package does not provide built in support for safaridriver on a Linux OS.'
            ]
        elif operating_system == 'windows':
            return [
                'Safari is probably not supported on Windows operating systems. In order for the safaridriver to run on a Windows OS, you will likely need to do many manual configurations. For this reason, this package does not provide built in support for safaridriver on a Windows OS.'
            ]


    @classmethod
    def format_driver_information(cls, operating_system, driver, browser, version, major_version):
        return f'# {operating_system} {driver} {version} (supports {browser} {major_version})'

    @classmethod
    def format_geckodriver_download_command(cls, operating_system, version):
        if operating_system.startswith('win'): return cls.format_windows_download(f'{cls.url_prefix_geckodriver}/{version}/geckodriver-{version}-{operating_system}.zip', 'geckodriver')
        else:                                  return cls.format_unix_download   (f'{cls.url_prefix_geckodriver}/{version}/geckodriver-{version}-{operating_system}.tar.gz')

    @classmethod
    def format_operadriver_download_command(cls, operating_system, version):
        if operating_system.startswith('win'): return cls.format_windows_operadriver_download(f'{cls.url_prefix_operadriver}/{version}/operadriver_{operating_system}.zip', 'operadriver')
        else:                                  return cls.format_unix_operadriver_download   (f'{cls.url_prefix_operadriver}/{version}/operadriver_{operating_system}.zip')

    @classmethod
    def format_chromedriver_download_command(cls, operating_system, version):
        if operating_system.startswith('win'): return cls.format_windows_download(f'{cls.url_prefix_chromedriver}/{version}/chromedriver_{operating_system}.zip', 'chromedriver')
        else:                                  return cls.format_unix_download   (f'{cls.url_prefix_chromedriver}/{version}/chromedriver_{operating_system}.zip')

    @classmethod
    def format_bravedriver_download_command(cls, operating_system, version):
        ### Brave Browser doesn't have its own bravedriver, but since it's chromium we can just download the chromedriver and use the corresponding chromedriver for the Brave version (with it renamed to "bravedriver" in order to avoud conflict with different versions of Chrome and Brave installed at the same time) ###
        if operating_system.startswith('win'): return cls.format_windows_bravedriver_download(f'{cls.url_prefix_operadriver}/{version}/operadriver_{operating_system}.zip', 'bravedriver')
        else:                                  return cls.format_unix_bravedriver_download   (f'{cls.url_prefix_operadriver}/{version}/operadriver_{operating_system}.zip')

    @classmethod
    def format_msedgedriver_download_command(cls, operating_system, version):
        if operating_system.startswith('win'): return cls.format_windows_download(f'{cls.url_prefix_msedgedriver}/{version}/edgedriver_{operating_system}.zip', 'msedgedriver')
        else:                                  return cls.format_unix_download   (f'{cls.url_prefix_msedgedriver}/{version}/edgedriver_{operating_system}.zip')


    @staticmethod
    def format_unix_download(url):
        return f'curl -SL {url} | tar -xzvf - -C /usr/local/bin/' + '\n'

    @staticmethod
    def format_unix_operadriver_download(url):
        return f'curl -SL {url} | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum' + '\n'

    @staticmethod
    def format_unix_bravedriver_download(url):
        return f'curl -SL {url} | tar -xzvf - --strip-components=1 -O > /usr/local/bin/bravedriver && chmod +x /usr/local/bin/bravedriver && rm /usr/local/bin/sha512_sum' + '\n'


    @staticmethod
    def format_windows_download(url, driver):
        drive = get_drive_letter()
        return fr'curl -SL {url} -o {drive}:\Windows\{driver} && tar -xzvf {drive}:\Windows\{driver} -C {drive}:\Windows && del {drive}:\Windows\{driver}' + '\n'

    @staticmethod
    def format_windows_operadriver_download(url, driver):
        drive = get_drive_letter()
        return fr'curl -SL {url} -o {drive}:\Windows\{driver} && tar -xzvf {drive}:\Windows\{driver} --strip-components=1 -C {drive}:\Windows && del {drive}:\Windows\{driver} && del {drive}:\Windows\sha512_sum' + '\n'

    @staticmethod
    def format_windows_bravedriver_download(url, driver):
        drive = get_drive_letter()
        return fr'curl -SL {url} -o {drive}:\Windows\{driver} && tar -xzvf {drive}:\Windows\{driver} --strip-components=1 -O > {drive}:\Windows\bravedriver.exe && del {drive}:\Windows\{driver} && del {drive}:\Windows\sha512_sum' + '\n'


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
        bravedriver_download_instructions  = '(Your Brave browser version should match the first numbers before the decimal place of the bravedriver version below. Note that there is currently no dedicated bravedriver, so this package substitutes the chromium operadriver.)'
        edgedriver_download_instructions   = '(Your Edge browser version should match the first numbers before the decimal place of the msedgedriver version below)'

        if   user_driver == 'firefox':  print(geckodriver_download_instructions)
        elif user_driver == 'opera':    print(operadriver_download_instructions)
        elif user_driver == 'safari':   print('This is an MacOS specific driver.')
        elif user_driver == 'chrome':   print(chromedriver_download_instructions)
        elif user_driver == 'brave':    print(bravedriver_download_instructions)
        elif user_driver == 'edge':     print(edgedriver_download_instructions)

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

    file_already_exists = 'This error indicates that a file of this name already exists in the current directory. If you want to overwrite this file, run the create_list_for method again with the optional parameter "write_format" set to "w"'
    file_already_exists_rerun_usage = 'Example usage:\n lc.create_list_for(write_format="w")\n'

    show_driver_options = 'To use a different driver, specify the driver in the driver argument during the ListCreator instantiation. For example:' + \
        "\n    lc = ListCreator(driver='firefox')" + \
        "\n    lc = ListCreator(driver='opera')" + \
        "\n    lc = ListCreator(driver='safari')" + \
        "\n    lc = ListCreator(driver='chrome')" + \
        "\n    lc = ListCreator(driver='brave')" + \
        "\n    lc = ListCreator(driver='edge')"



class ScriptMessage(Common):
    '''
    This class contains messages that relevant for the package it is being run as a module using the -m option from the CLI.
    '''


    not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt setting TO FLAG.\nThis program will now exit...'

    running_default_driver = '\nNo driver flag used, so running program using the Firefox driver.'

    input_message = "What is the name of the YouTube channel you want to generate the list for?\n\nIf you're unsure, click on the channel and look at the URL.\nIt should be in the format:\nhttps://www.youtube.com/user/YourChannelName\nOR\nhttps://www.youtube.com/channel/YourChannelName\n\nSubstitute what you see for YourChannelName and type it in below:\n"

    show_driver_options = 'To use a different driver, specify the driver in the driver flag. For example:'
