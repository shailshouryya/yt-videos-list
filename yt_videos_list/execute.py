from . import program
from . import selenium_macos, selenium_windows, selenium_linux
from .notifications import Common, ModuleMessage, ScriptMessage
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import platform
import time
import os

commonMessage = Common()
moduleMessage = ModuleMessage()
scriptMessage = ScriptMessage()

def logic(channel, channelType, fileName, txt, txtWriteFormat, csv, csvWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, userDriver, executionType):
    #################################################################
    #################### define helper functions ####################
    #################################################################

    def determineFileName():
        if fileName is not None:
            return fileName
        else:
            return channel

    def verifyWriteFormat(fileType, writeFormat, fileName, fileExtension):
        if fileType is True and writeFormat == 'x':
            filename = f'{fileName}VideosList.{fileExtension}'
            fileExists = True if os.path.isfile(f'./{filename}') else False

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
            if userdriver == 'firefox':
                options = selenium.webdriver.firefox.options.Options()
                options.headless = True
                driver = userdriver(options=options)
            if userdriver == 'chrome':
                # options = selenium.webdriver.chrome.options.Options()
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = userdriver(chrome_options=options)
            if userdriver == 'opera':
                # Opera driver MRO: WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
                # options = selenium.webdriver.chrome.options.Options()
                # options.headless = True
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = userdriver(options=options)
                print (commonMessage.unsupportedOperaHeadless)
            if userdriver == 'safari':
                driver = userdriver()
                print (commonMessage.unsupportedSafariHeadless)
        return driver

    def showUserHowToSetupSeleniumFor(userDriver, userOS):
        if userDriver != 'safari':
            commonMessage.tellUserToDownloadDriver(userDriver)
        commonMessage.displayDependencySetupInstructions(userDriver, userOS)

    #################################################################
    #################### start running the logic ####################
    #################################################################

    channel = channel.strip().strip('/')
    channelType = channelType.strip().strip('/')
    fileName = determineFileName()
    txtWriteFormat = verifyWriteFormat(txt, txtWriteFormat, fileName, 'txt')
    csvWriteFormat = verifyWriteFormat(csv, csvWriteFormat, fileName, 'csv')
    docxWriteFormat = verifyWriteFormat(docx, docxWriteFormat, fileName, 'docx')

    if userDriver is None:
        print (moduleMessage.runningDefaultDriver) if executionType == 'module' else print (scriptMessage.runningDefaultDriver)
        print (moduleMessage.showDriverOptions) if executionType == 'module' else print (scriptMessage.showDriverOptions)
        userDriver = 'firefox'
    userdriver = checkDriver() # NOTE the selenium webdriver object is referred to as userdriver, NOT userDriver; userDriver is used to check the user input as userdriver refers to the webdriver object
    if userdriver == 'invalid':
        return

    programStart = time.perf_counter()
    try:
        driver = openUserDriver()
    except selenium.common.exceptions.WebDriverException as e:
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        commonMessage.seleniumDependencyError(e)
        if platform.system().lower().startswith('darwin'):
            userOS = 'macos'
        elif platform.system().lower().startswith('windows'):
            userOS = 'windows'
        elif platform.system().lower().startswith('linux'):
            userOS = 'linux'
        else:
            print (commonMessage.unsupportedOS)
            return

        try:
            globals()[f'selenium_{userOS}'].download(userDriver)
            sys.exit() # skip this try block for now until the logic to install the correct Selenium driver based on the user's OS and specified driver is added
        except: # could not download the correct Selenium driver based on the user's OS and specified driver
            showUserHowToSetupSeleniumFor(userDriver, userOS)
        return

    with driver:
        videosList = program.scrollToBottom(channel, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (commonMessage.noVideosFound)
            print (moduleMessage.checkChannelType) if executionType == 'module' else print (scriptMessage.checkChannelType)
            return
        if txt is True:
            program.writeToTxt(videosList, channel, fileName, txtWriteFormat, chronological)
            # saveToMemWriteToTxt(videosList, channel, fileName, writeFormat) # slightly slower than writing to disk directly
        if csv is True:
            program.writeToCsv(videosList, channel, fileName, csvWriteFormat, chronological)

    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
