from . import program
from . import selenium_macos, selenium_windows, selenium_linux
from .notifications import Common, ModuleMessage, ScriptMessage
import os, sys, platform
import time
import selenium
from selenium import webdriver

commonMessage = Common()
moduleMessage = ModuleMessage()
scriptMessage = ScriptMessage()

def logic(channel, channelType, fileName, txt, txtWriteFormat, csv, csvWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, userDriver, executionType):
    def determineFileName():
        if fileName is not None:
            return fileName
        else:
            return channel

    def verifyWriteFormat(fileType, writeFormat, fileName, fileExtension):
        def newWriteFormat():
                userResponse = input()
                if 'proceed' in userResponse.strip().lower():
                    return 'w'
                elif 'skip' in userResponse.strip().lower():
                    return 0
                else:
                    print ('\n' + commonMessage.invalidResponse)
                    commonMessage.fileAlreadyExistsPrompt(filename)
                    return newWriteFormat()

        if fileType is True and writeFormat == 'x':
            filename = f'{fileName}VideosList.{fileExtension}'
            fileExists = True if os.path.isfile(f'./{filename}') else False
            if fileExists is True:
                commonMessage.fileAlreadyExistsWarning(filename)
                commonMessage.fileAlreadyExistsPrompt(filename)
                return newWriteFormat()
            return 'x'
        else:
            return writeFormat

    def checkDriver():
        if 'firefox' in userDriver:
            return webdriver.Firefox
        elif 'chrome' in userDriver:
            return webdriver.Chrome
        elif 'opera' in userDriver:
            return webdriver.Opera
        elif 'safari' in userDriver:
            return webdriver.Safari
        else:
            print (commonMessage.invalidDriver)
            return 'invalid'

    def openUserDriver():
        if headless is False: # opens Selenium browsing instance
            driver = userdriver()
            if executionType == 'module':
                print (moduleMessage.runInHeadless)
                print (moduleMessage.runInHeadlessExample)
        else: # headless is True
            if userDriver == 'firefox':
                options = selenium.webdriver.firefox.options.Options()
                options.headless = True
                driver = userdriver(options=options)
            elif userDriver == 'chrome':
                # options = selenium.webdriver.chrome.options.Options()
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = userdriver(chrome_options=options)
            elif userDriver == 'opera':
                # Opera driver MRO: WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
                # options = selenium.webdriver.chrome.options.Options()
                # options.headless = True
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = userdriver(options=options)
                print (commonMessage.unsupportedOperaHeadless)
            elif userDriver == 'safari':
                driver = userdriver()
                print (commonMessage.unsupportedSafariHeadless)
        return driver

    def determineUserOS():
        if platform.system().lower().startswith('darwin'):
            return 'macos'
        elif platform.system().lower().startswith('linux'):
            return 'linux'
        elif platform.system().lower().startswith('windows'):
            return 'windows'
        else:
            print (commonMessage.unsupportedOS)
            sys.exit()

    def showUserHowToSetupSelenium():
        if userDriver != 'safari':
            commonMessage.tellUserToDownloadDriver(userDriver)
        commonMessage.displayDependencySetupInstructions(userDriver, userOS)


    ### check user input ###
    channel = channel.strip().strip('/')
    channelType = channelType.strip().strip('/')
    baseUrl = 'https://www.youtube.com'
    videos = 'videos'
    url = f'{baseUrl}/{channelType}/{channel}/{videos}'

    fileName = determineFileName()
    txtWriteFormat = verifyWriteFormat(txt, txtWriteFormat, fileName, 'txt')
    csvWriteFormat = verifyWriteFormat(csv, csvWriteFormat, fileName, 'csv')
    docxWriteFormat = verifyWriteFormat(docx, docxWriteFormat, fileName, 'docx')

    if (txtWriteFormat == 0 and csvWriteFormat == 0) or (txt is False and csv is False):
        print (commonMessage.notWritingToAnyFiles)
        print (moduleMessage.notWritingToAnyFilesHint) if executionType == 'module' else print (scriptMessage.notWritingToAnyFilesHint)
        return # the files already exist and the user doesn't want to overwrite either of them

    if userDriver is None:
        print (moduleMessage.runningDefaultDriver) if executionType == 'module' else print (scriptMessage.runningDefaultDriver)
        print (moduleMessage.showDriverOptions) if executionType == 'module' else print (scriptMessage.showDriverOptions)
        userDriver = 'firefox'
    userdriver = checkDriver() # NOTE the selenium webdriver object is referred to as userdriver, NOT userDriver; userDriver is used to check the user input while userdriver refers to the webdriver object
    if userdriver == 'invalid':
        return
    ### end user input check ###


    programStart = time.perf_counter()
    try:
        driver = openUserDriver()
    except selenium.common.exceptions.WebDriverException as e:
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        commonMessage.seleniumDependencyError(e)
        userOS = determineUserOS()
        try:
            globals()[f'selenium_{userOS}'].download(userDriver)
            sys.exit() # skip this try block for now until the logic to install the correct Selenium driver based on the user's OS and specified driver is added
            driver = openUserDriver()
        except: # could not download the correct Selenium driver based on the user's OS and specified driver
            showUserHowToSetupSelenium()
            return
    with driver:
        videosList = program.scrollToBottom(url, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (commonMessage.noVideosFound)
            print (moduleMessage.checkChannelType) if executionType == 'module' else print (scriptMessage.checkChannelType)
            return
        if txt is True and txtWriteFormat != 0:
            program.writeToTxt(videosList, fileName, txtWriteFormat, chronological)
            # saveToMemWriteToTxt(videosList, fileName, writeFormat) # slightly slower than writing to disk directly
        if csv is True and csvWriteFormat != 0:
            program.writeToCsv(videosList, fileName, csvWriteFormat, chronological)
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
