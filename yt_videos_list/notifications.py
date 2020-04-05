class Common:
    '''
    This class contains messages that are common regardless of whether the package is being run as a module using the -m option from the CLI or as a module from within the Python interpreter (or another Python script).
    '''


    notWritingToAnyFiles = '\nBased on your provided settings, yt_videos_list will not be writing to either a csv file or a txt file.'

    noVideosFound = 'No videos were found for the channel you provided. Are you sure you typed in the channel name correctly?\n'
    noNewVideosFound = 'No new videos were found since the last scroll. Waiting another 0.6 seconds to see if more videos can be loaded....'
    invalidResponse = 'The response you entered was invalid.'

    invalidDriver = 'The driver you specified is invalid. Please try rerunning the last command after specifying a valid driver. Supported drivers include:\n   Firefox\n   Opera\n   Safari\n   Chrome'

    unsupportedOperaHeadless = '\nHeadless mode is unsupported in OperaDriver. We are waiting on the Opera dev team to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupportedSafariHeadless = '\nHeadless mode is unsupported in SafariDriver. We are waiting on Apple to start offering support for headless mode to allow remote automation without opening a driver. We will update this when support is added...\n:)\n\n\n'
    unsupportedOS = 'The system you are using is not yet supported. Please create an issue at https://github.com/Shail-Shouryya/yt_videos_list/issues\nThanks!'

    driverDownloadsForOS = {
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

    moreDriverInfo = {
        # 'driver': ['driverName', 'url for more driver info',  'url for driver releases', 'browser name', 'url for browser download']
        'firefox': ['geckodriver',  'https://github.com/mozilla/geckodriver',                    'https://github.com/mozilla/geckodriver/releases',                'Mozilla Firefox', 'https://www.mozilla.org/en-US/firefox/new/'],
        'opera':   ['operadriver',  'https://github.com/operasoftware/operachromiumdriver',      'https://github.com/operasoftware/operachromiumdriver/releases',  'Opera',           'https://www.opera.com/'],
        'chrome':  ['chromedriver', 'https://sites.google.com/a/chromium.org/chromedriver/home', 'https://sites.google.com/a/chromium.org/chromedriver/downloads', 'Chrome',          'https://www.google.com/chrome/']
    }

    @classmethod
    def displayDependencySetupInstructions(cls, userDriver, userOS):
        terminalCopyPasteDirections = 'Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T (or CTRL+N or CTRL+D depending on your keyboard/OS) from an active terminal session), and paste the command you just copied. Once you\'ve done that, you should be able to come back to this session and rerun the last command without an error!\n\n'

        if userOS != 'windows' and userDriver != 'safari':
            print (terminalCopyPasteDirections)

        geckodriverDownloadInstructions = '(The given command downloads a geckodriver ("Firefoxdriver") version that is compatible with Firefox versions ≥ 60. To see more information about the differences compared to older versions, please visit https://github.com/mozilla/geckodriver/releases)'
        operadriverDownloadInstructions = '(Your Opera browser version should match the "supports Opera ## release" below)'
        chromedriverDownloadInstructions = '(Your Chrome browser version should match the first numbers before the decimal place of the chromedriver version below)'

        print (geckodriverDownloadInstructions) if userDriver == 'firefox' else print (operadriverDownloadInstructions) if userDriver == 'opera' else print (chromedriverDownloadInstructions) if userDriver == 'chrome' else print ('This is an OS specific driver.')

        for driverVersionDownload in cls.driverDownloadsForOS[userDriver][userOS]:
            print (driverVersionDownload)

        def displayMoreDependencyInformation(userDriver):
            print (f'\n\n# For more information about the {cls.moreDriverInfo[userDriver][0]}, please visit\n{cls.moreDriverInfo[userDriver][1]}\n{cls.moreDriverInfo[userDriver][2]}      (all supported versions)\n\nNOTE! You must also have the {cls.moreDriverInfo[userDriver][3]} browser installed to use this. If you don\'t have it installed, install it from\n{cls.moreDriverInfo[userDriver][4]}')

        if userDriver != 'safari':
            displayMoreDependencyInformation(userDriver)

    @staticmethod
    def seleniumDependencyError(errorMessage):
        print (f'\n\n\n\n\n\n\nThere was an error while trying to open up the remote selenium instance. The exact error was:\n{errorMessage}\nDon\'t worry though, this is an easy fix!')

    @staticmethod
    def tellUserToDownloadDriver(userDriver):
        print (f'\nIt looks like you don\'t have the correct Selenium dependency set up to run this program using the remote {userDriver}driver.\nThe version of your {userDriver.title()} browser - usually found by going to {userDriver.title()} -> \"About browser\" in the menu bar within a {userDriver.title()} window - should match the comment for the corresponding command.\nPlease download it using the relevant command from the list of commands below.\n')

    @staticmethod
    def fileAlreadyExistsWarning(filename):
        print (f'\nWARNING! A file with the name {filename} already exists in the current directory.')

    @staticmethod
    def fileAlreadyExistsPrompt(filename):
        print (f'If you wish to proceed and overwrite {filename}, type "proceed", otherwise move the file to a different directory on your computer OR rename the file before typing "proceed"')
        print (f'If you wish to skip the creation of {filename}, type "skip"')

class ModuleMessage(Common):
    notWritingToAnyFilesHint = 'If you want to run this program, please change the csv OR txt setting to True.\nThis program will now exit...'

    runningDefaultDriver = '\nNo driver specified during ListCreator instantiation, so running program using the Firefox driver.'
    runInHeadless = '\nAdvanced usage: you can run this program in headless mode with the optional "headless" parameter set to True to speed up execution slightly:'
    runInHeadlessExample = '    LC = ListCreator(headless=True)\n\n\n'

    checkChannelType = 'If you did type the name in correctly, perhaps the channelType is set incorrectly. Try setting channelType to "channel" in the create_list_for() method call if you set channelType to "user" for this run, or try running the method with channelType set to "user" if you ran this method with channelType set to "channel" for this run.\n'

    fileAlreadyExists = 'This error indicates that a file of this name already exists in the current directory. If you want to overwrite this file, run the create_list_for method again with the optional parameter "writeFormat" set to "w"'
    fileAlreadyExistsRerunUsage = 'Example usage:\n LC.create_list_for(writeFormat="w")\n'

    showDriverOptions = 'To use a different driver, specify the driver in the driver argument during the ListCreator instantiation. For example:' + \
        "\n    LC = ListCreator(driver='opera')" + \
        "\n    LC = ListCreator(driver='safari')" + \
        "\n    LC = ListCreator(driver='chrome')" + \
        "\n    LC = ListCreator(driver='firefox')"

class ScriptMessage(Common):
    notWritingToAnyFilesHint = 'If you want to run this program, please change the csv OR txt setting TO FLAG.\nThis program will now exit...'

    runningDefaultDriver = '\nNo driver flag used, so running program using the Firefox driver.'

    inputMessage = "What is the name of the YouTube channel you want to generate the list for?\n\nIf you're unsure, click on the channel and look at the URL.\nIt should be in the format:\nhttps://www.youtube.com/user/YourChannelName\nOR\nhttps://www.youtube.com/channel/YourChannelName\n\nSubstitute what you see for YourChannelName and type it in below (NOTE: if your url looks like the second option, you need to run this script with the -c or --channel flag):\n"

    checkChannelType = 'If you did type the name in correctly, perhaps the channelType is set incorrectly. Try using the -c or --channelType flag for this script if you didn\'t do it when running this script, or try running the script without the -c or --channelType flag if you DID include that flag when running this script.'

    showDriverOptions = 'To use a different driver, specify the driver in the driver flag. For example:'
