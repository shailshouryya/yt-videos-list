class Common:
    '''
    This class contains messages that are common regardless of whether the package is being run as a module using the -m option from the CLI or as a module from within the Python interpreter (or another Python script).
    '''


    not_writing_to_any_files = '\nBased on your provided settings, yt_videos_list will not be writing to either a csv file or a txt file.'

    no_videos_found = 'No videos were found for the channel you provided. Are you sure you typed in the channel name correctly?\n'
    no_new_videos_found = 'No new videos were found since the last scroll. Waiting another 0.6 seconds to see if more videos can be loaded....'
    invalid_response = 'The response you entered was invalid.'

    invalid_driver = 'The driver you specified is invalid. Please try rerunning the last command after specifying a valid driver. Supported drivers include:\n   Firefox\n   Opera\n   Safari\n   Chrome'

    unsupported_opera_headless = '\nHeadless mode is unsupported in OperaDriver. We are waiting on the Opera dev team to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_safari_headless = '\nHeadless mode is unsupported in SafariDriver. We are waiting on Apple to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupported_os = 'The system you are using is not yet supported. Please create an issue at https://github.com/Shail-Shouryya/yt_videos_list/issues\nThanks!'

    driver_downloads_for_os = {
        'firefox': {
            'macos': [
                '# macos geckodriver (Firefoxdriver) v0.26.0',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin/ \n'
            ],
            'linux': [
                '# linux64 geckodriver (Firefoxdriver) v0.26.0',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux32 geckodriver (Firefoxdriver) v0.26.0',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz | tar -xzvf - -C /usr/local/bin/ \n'
            ],
            'windows': [
                'In progress!',
                '# windows64 geckodriver (Firefoxdriver) v0.26.0',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip -o C:\yt_videos_list_TEMP\geckodriver && tar -xzvf C:\yt_videos_list_TEMP\geckodriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# windows32 geckodriver (Firefoxdriver) v0.26.0',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win32.zip -o C:\yt_videos_list_TEMP\geckodriver && tar -xzvf C:\yt_videos_list_TEMP\geckodriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n'
            ]
        },
        'opera': {
            'macos' : [
                '# mac64 Operadriver 81.0.4044.113 (supports Opera Stable 68 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.81.0.4044.113/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 80.0.3987.100 (supports Opera Stable 67 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.80.0.3987.100/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 79.0.3945.79 (supports Opera Stable 66 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.79.0.3945.79/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.78.0.3904.87/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.76.0.3809.132/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.75.0.3770.100/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 2.45 (supports Opera 60 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.45/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 2.42 (supports Opera 58 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.42/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 2.41 (supports Opera 57 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.41/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 2.40 (supports Opera 56 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.40/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 2.38 (supports Opera 55 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.38/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# mac64 Operadriver 2.37 (supports Opera 54 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.37/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n'
            ],
            'linux': [
                '# linux64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.78.0.3904.87/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.76.0.3809.132/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 75.0.3770.100 (supports Opera 62) release',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.75.0.3770.100/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 2.45 (supports Opera 60 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.45/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 2.42 (supports Opera 58 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.42/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 2.41 (supports Opera 57) release',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.41/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 2.40 (supports Opera 56 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.40/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 2.38 (supports Opera 55 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.38/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ &--strip-components=1 && rm /usr/local/bin/sha512_sum \n',
                '# linux64 Operadriver 2.37 (supports Opera 54 release)',
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.37/operadriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum \n'
            ],
            'windows': [
                'In progress!',
                '# windows64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.78.0.3904.87/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.76.0.3809.132/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.75.0.3770.100/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 2.45 (supports Opera 60 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.45/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 2.42 (supports Opera 58 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.42/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 2.41 (supports Opera 57 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.41/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 2.40 (supports Opera 56 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.40/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 2.38 (supports Opera 55 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.38/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows64 Operadriver 2.37 (supports Opera 54 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.37/operadriver_win64.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n\n',
                '# windows32 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.78.0.3904.87/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 77.0.3865.120 (supports Opera 64 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 76.0.3809.132 (supports Opera 63 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.76.0.3809.132/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 75.0.3770.100 (supports Opera 62 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.75.0.3770.100/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 2.45 (supports Opera 60) release',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.45/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 2.42 (supports Opera 58 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.42/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 2.41 (supports Opera 57 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.41/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 2.40 (supports Opera 56 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.40/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 2.38 (supports Opera 55 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.38/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n',
                '# windows32 Operadriver 2.37 (supports Opera 54 release)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.37/operadriver_win32.zip -o C:\yt_videos_list_TEMP\operadriver && tar -xzvf C:\yt_videos_list_TEMP\operadriver -C C:\Windows\ --strip-components=1 && rmdir /q /s C:\yt_videos_list_TEMP && del C:\Windows\sha512_sum \n'
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
                '# mac64 Chromedriver 79.0.3945.36',
                'curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 78.0.3904.105',
                'curl -SL https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 77.0.3865.40',
                'curl -SL https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 76.0.3809.126',
                'curl -SL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 75.0.3770.140',
                'curl -SL https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 74.0.3729.6',
                'curl -SL https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 73.0.3683.68',
                'curl -SL https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# mac64 Chromedriver 2.46 (Supports Chrome v71-73)',
                'curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/ \n'
            ],
            'linux': [
                '# linux64 Chromedriver 79.0.3945.36',
                'curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 78.0.3904.105',
                'curl -SL https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 77.0.3865.40',
                'curl -SL https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 76.0.3809.126',
                'curl -SL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 75.0.3770.140',
                'curl -SL https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 74.0.3729.6',
                'curl -SL https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 73.0.3683.68',
                'curl -SL https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n',
                '# linux64 Chromedriver 2.46 (Supports Chrome v71-73)',
                'curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin/ \n'
            ],
            'windows': [
                'In progress!',
                '# win32 Chromedriver 79.0.3945.36',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# win32 Chromedriver 78.0.3904.105',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# win32 Chromedriver 77.0.3865.40',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# win32 Chromedriver 76.0.3809.126',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# win32 Chromedriver 75.0.3770.140',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# win32 Chromedriver 74.0.3729.6',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',\
                '# win32 Chromedriver 73.0.3683.68',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n',
                '# win32 Chromedriver 2.46 (Supports Chrome v71-73)',
                r'mkdir C:\yt_videos_list_TEMP\ && curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_win32.zip -o C:\yt_videos_list_TEMP\chromedriver && tar -xzvf C:\yt_videos_list_TEMP\chromedriver -C C:\Windows\ && rmdir /q /s C:\yt_videos_list_TEMP \n'
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
    def display_dependency_setup_instructions(cls, user_driver, user_os):
        terminal_copy_paste_directions = 'Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T (or CTRL+N or CTRL+D depending on your keyboard/OS) from an active terminal session), and paste the command you just copied. Once you\'ve done that, you should be able to come back to this session and rerun the last command without an error!\n\n'

        if user_os != 'windows' and user_driver != 'safari':
            print(terminal_copy_paste_directions)

        geckodriver_download_instructions = '(The given command downloads a geckodriver ("Firefoxdriver") version that is compatible with Firefox versions ≥ 60. To see more information about the differences compared to older versions, please visit https://github.com/mozilla/geckodriver/releases)'
        operadriver_download_instructions = '(Your Opera browser version should match the "supports Opera ## release" below)'
        chromedriver_download_instructions = '(Your Chrome browser version should match the first numbers before the decimal place of the chromedriver version below)'

        print(geckodriver_download_instructions) if user_driver == 'firefox' else print(operadriver_download_instructions) if user_driver == 'opera' else print(chromedriver_download_instructions) if user_driver == 'chrome' else print('This is an OS specific driver.')

        for driver_version_download in cls.driver_downloads_for_os[user_driver][user_os]:
            print(driver_version_download)

        def display_more_dependency_information(user_driver):
            print(f'\n\n# For more information about the {cls.more_driver_info[user_driver][0]}, please visit\n{cls.more_driver_info[user_driver][1]}\n{cls.more_driver_info[user_driver][2]}      (all supported versions)\n\nNOTE! You must also have the {cls.more_driver_info[user_driver][3]} browser installed to use this. If you don\'t have it installed, install it from\n{cls.more_driver_info[user_driver][4]}')

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


    not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt setting to True.\nThis program will now exit...'

    running_default_driver = '\nNo driver specified during ListCreator instantiation, so running program using the Firefox driver.'
    run_in_headless_hint = '\nAdvanced usage: you can run this program in headless mode with the optional "headless" parameter set to True to speed up execution slightly:'
    run_in_headless_example = '    lc = ListCreator(headless=True)\n\n\n'

    check_channel_type = 'If you did type the name in correctly, perhaps the channel_type is set incorrectly. Try setting channel_type to "channel" in the create_list_for() method call if you set channel_type to "user" for this run, or try running the method with channel_type set to "user" if you ran this method with channel_type set to "channel" for this run.\n'

    file_already_exists = 'This error indicates that a file of this name already exists in the current directory. If you want to overwrite this file, run the create_list_for method again with the optional parameter "write_format" set to "w"'
    file_already_exists_rerun_usage = 'Example usage:\n lc.create_list_for(write_format="w")\n'

    show_driver_options = 'To use a different driver, specify the driver in the driver argument during the ListCreator instantiation. For example:' + \
        "\n    lc = ListCreator(driver='opera')" + \
        "\n    lc = ListCreator(driver='safari')" + \
        "\n    lc = ListCreator(driver='chrome')" + \
        "\n    lc = ListCreator(driver='firefox')"



class ScriptMessage(Common):
    '''
    This class contains messages that relevant for the package it is being run as a module using the -m option from the CLI.
    '''


    not_writing_to_any_files_hint = 'If you want to run this program, please change the csv OR txt setting TO FLAG.\nThis program will now exit...'

    running_default_driver = '\nNo driver flag used, so running program using the Firefox driver.'

    input_message = "What is the name of the YouTube channel you want to generate the list for?\n\nIf you're unsure, click on the channel and look at the URL.\nIt should be in the format:\nhttps://www.youtube.com/user/YourChannelName\nOR\nhttps://www.youtube.com/channel/YourChannelName\n\nSubstitute what you see for YourChannelName and type it in below (NOTE: if your url looks like the second option, you need to run this script with the -c or --channel flag):\n"

    check_channel_type = 'If you did type the name in correctly, perhaps the channel_type is set incorrectly. Try using the -c or --channel_type flag for this script if you didn\'t do it when running this script, or try running the script without the -c or --channel_type flag if you DID include that flag when running this script.'

    show_driver_options = 'To use a different driver, specify the driver in the driver flag. For example:'
