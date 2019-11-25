class Common:
    '''
    This class contains messages that are common to both the pyYT_videos_list and execute modules.
    '''
    noVideosFound = 'No videos were found for the channel you provided. Are you sure you typed in the channel name correctly?\n'
    noNewVideosFound = 'No new videos were found since the last scroll. Waiting another 0.6 seconds to see if more videos can be loaded....'
    invalidResponse = 'The response you entered was invalid.'

    runningDefaultBrowser = '\nNo browser specified during ListGenerator instantiation, running program using the Firefox browser.'
    showBrowserOptions = "To use a different browser, specify the browser in the browser argument during the ListGenerator instantiation. For example:" + \
        "\n    LG = ListGenerator(browser='opera')" + \
        "\n    LG = ListGenerator(browser='safari')" + \
        "\n    LG = ListGenerator(browser='chrome')" + \
        "\n    LG = ListGenerator(browser='firefox')"

    geckodriverInfo  = '# For more information about the geckodriver, please visit https://github.com/mozilla/geckodriver\n'
    operadriverInfo  = '# For more information about the operadriver, please visit https://github.com/operasoftware/operachromiumdriver\n'
    chromedriverInfo = '# For more information about the chromedriver, please visit https://sites.google.com/a/chromium.org/chromedriver/home\n'

    geckodriverDownloadInstructions = '(The given command downloads a geckodriver version that is compatible with Firefox versions ≥ 60. To see more information about the differences compared to older versions, please visit https://github.com/mozilla/geckodriver/releases)\n'
    operadriverDownloadInstructions = '(Your Opera browser version should match the "supports Opera ## release" below)\n'
    chromedriverDownloadInstructions = '(Your Chrome browser version should match the first numbers before the decimal place of the chromedriver version below)\n'

    terminalCopyPasteDirections = 'Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T from an active terminal session), and paste the command you just copied. Once you\'ve done that, you should be able to come back to this session and rerun the last command without an error!'

    browsersForOS = {
        'firefox': {
            'macos': [
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin',
                f'{terminalCopyPasteDirections}'
            ],
            'linux': [

                f'{terminalCopyPasteDirections}'
            ],
            'windows': [
                'In progress!'
            ]
        },
        'opera': {
            'macos' : [
                '# mac64 Operadriver 78.0.3904.87 (supports Opera Stable 65)'
                '# mac64 Operadriver '
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin --strip-components=1 && rm /usr/local/bin/sha512_sum',
                '# mac64 Operadriver ',

                '# mac64 Operadriver ',
                '# mac64 Operadriver ',
                '# mac64 Operadriver ',
                '# mac64 Operadriver ',
                '# mac64 Operadriver ',
                '# mac64 Operadriver ',
                '# mac64 Operadriver ',
                f'{operadriverInfo}',
                f'{terminalCopyPasteDirections}'

            ],
            'linux': [
                '# linux64 Operadriver 78.0.3904.87 (supports Opera Stable 65)',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                '# linux64 Operadriver',
                f'{operadriverInfo}'
                f'{terminalCopyPasteDirections}'
            ],
            'windows': [
                'In progress!',
                '# windows64 Operadriver 78.0.3904.87 (supports Opera Stable 65)',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows64 Operadriver',
                '# windows32 Operadriver 78.0.3904.87 (supports Opera Stable 65)',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                '# windows32 Operadriver',
                f'{operadriverInfo}'
            ]
        },
        'safari': {
            'macos' : [
                f'{terminalCopyPasteDirections}'
            ],
            'linux': [
                f'{terminalCopyPasteDirections}'
            ],
            'windows': [
                'Not supported!'
            ]
        },
        'chrome': {
            'macos' : [
                f'{chromedriverDownloadInstructions}',
                '# mac64 Chromedriver 79.0.3945.36:',
                'curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 78.0.3904.105',
                'curl -SL https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 77.0.3865.40',
                'curl -SL https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 76.0.3809.126',
                'curl -SL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 75.0.3770.140',
                'curl -SL https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 74.0.3729.6',
                'curl -SL https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 73.0.3683.68',
                'curl -SL https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# mac64 Chromedriver 2.46 (Supports Chrome v71-73)',
                'curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n',
                f'{chromedriverInfo}',
                f'{terminalCopyPasteDirections}'
            ],
            'linux': [
                f'{chromedriverDownloadInstructions}',
                '# linux64 Chromedriver 79.0.3945.36:',
                'curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 78.0.3904.105:',
                'curl -SL https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 77.0.3865.40',
                'curl -SL https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 76.0.3809.126',
                'curl -SL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 75.0.3770.140',
                'curl -SL https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 74.0.3729.6',
                'curl -SL https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 73.0.3683.68',
                'curl -SL https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                '# linux64 Chromedriver 2.46 (Supports Chrome v71-73)',
                'curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip | tar -xzvf - -C /usr/local/bin \n',
                f'{chromedriverInfo}',
                f'{terminalCopyPasteDirections}'
            ],
            'windows': [
                'In progress!',
                f'{chromedriverDownloadInstructions}',
                '# win32 Chromedriver 79.0.3945.36:',
                'https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip \n',
                '# win32 Chromedriver 78.0.3904.105:',
                'https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip \n',
                '# win32 Chromedriver 77.0.3865.40',
                'https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_win32.zip \n',
                '# win32 Chromedriver 76.0.3809.126',
                'https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip \n'
                '# win32 Chromedriver 75.0.3770.140',
                'https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_win32.zip \n'
                '# win32 Chromedriver 74.0.3729.6',
                'https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_win32.zip \n'
                '# win32 Chromedriver 73.0.3683.68',
                'https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_win32.zip \n'
                '# win32 Chromedriver 2.46 (Supports Chrome v71-73)',
                'https://chromedriver.storage.googleapis.com/2.46/chromedriver_win32.zip \n',
                f'{chromedriverInfo}'
            ]
        }
    }

    @staticmethod
    def tellUserToDownloadBrowser(userBrowser):
        print (f"\nIt looks like you don't have the correct selenium dependency set up to run this program using the remote {userBrowser}driver.\nThe version of your {userBrowser.title()} browser - usually found by going to {userBrowser.title()} -> \"About browser\" within a {userBrowser.title()} window - should match the comment for the corresponding command.\nPlease download it using the relevant command:")

    @staticmethod
    def fileAlreadyExistsWarning(filename):
        print (f'\nWARNING! A file with the name {filename} already exists in the current directory.')

    @staticmethod
    def fileAlreadyExistsPrompt(filename):
        print (f'If you wish to proceed and overwrite {filename}, type "proceed", otherwise move the file to a different directory on your computer OR rename the file before typing "proceed"')
        print (f'If you wish to skip the creation of {filename}, type "skip"')

class ModuleMessage(Common):

    runInHeadless = '\nAdvanced usage: you can run this program in headless mode with the optional "headless" parameter set to True to speed up execution slightly:'
    runInHeadlessExample = "    LG = ListGenerator(headless=True)\n\n\n"
    checkChannelType = 'If you did type the name in correctly, perhaps the channelType is set incorrectly. Try setting channelType to "channel" in the generate_list() method call if you set channelType to "user" for this run, or try running the method with channelType set to "user" if you ran this method with channelType set to "channel" for this run\n'
    fileAlreadyExists = 'This error indicates that a file of this name already exists in the current directory. If you want to overwrite this file, run the generate_list method again with the optional parameter "writeFormat" set to "w"'
    fileAlreadyExistsRerunUsage = 'Example usage:\n LG.generate_list(writeFormat="w")\n'

class ScriptMessage(Common):
    inputMessage = "What is the name of the YouTube channel you want to generate the list for?" + "\n\n" + "If you're unsure, click on the channel and look at the URL." + "\n" + "It should be in the format:" + "\n" + "https://www.youtube.com/user/YourChannelName" + "\n" + "OR" + "\n" + "https://www.youtube.com/channel/YourChannelName" + "\n\n" + "Substitute what you see for YourChannelName and type it in below (NOTE: if your url looks like the second option, you need to run this script with the -c or --channel flag):\n"

    checkChannelType = 'If you did type the name in correctly, perhaps the channelType is set incorrectly. Try using the -c or --channelType flag for this script if you didn\'t do it when running this script, or try running the script without the -c or --channelType flag if you DID include that flag when running this script.'
