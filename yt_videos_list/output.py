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

    browsersForOS = {
        'firefox': {
            'macos': [
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin',
                'curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin',
            ],
            'linux': [

            ],
            'windows': [
                'In progress!'
            ]
        },
        'opera': {
            'macos' : [
                'curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_mac64.zip | tar -xzvf - -C /usr/local/bin --strip-components=1 && rm /usr/local/bin/sha512_sum'

            ],
            'linux': [

            ],
            'windows': [
                'In progress!'
            ]
        },
        'safari': {
            'macos' : [

            ],
            'linux': [

            ],
            'windows': [
                'Not supported!'
            ]
        },
        'chrome': {
            'macos' : [
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
                'curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin \n'
            ],
            'linux': [
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
            ],
            'windows': [
                'In progress!',
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
                'https://chromedriver.storage.googleapis.com/2.46/chromedriver_win32.zip \n'


            ]
        }
    }

    @staticmethod
    def tellUserToDownloadBrowser(userBrowser):
        print (f"It looks like you don't have the selenium dependencies set up to run this program using the remote {userBrowser}driver.\nThe version of your {userBrowser} browser - usually found by going to {userBrowser.title()} -> \"About browser\" within a {userBrowser} window - should match the first numbers before the decimal place of the {userBrowser}driver.\nPlease download it using the relevant command:\n")

    @staticmethod
    def fileAlreadyExistsWarning(filename):
        print (f'\nWARNING! A file with the name {filename} already exists in the current directory.')

    @staticmethod
    def fileAlreadyExistsPrompt(filename):
        print (f'If you wish to proceed and overwrite {filename}, type "proceed", otherwise move the file to a different directory on your computer before typing "proceed"')
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
