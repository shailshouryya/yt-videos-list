from . import program
from .notifications import Common, ModuleMessage, ScriptMessage
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import platform
import time
import os

cMessage = Common()
sMessage = ScriptMessage()

def verifyWriteFormat(fileName, fileType):
    filename = f'{fileName}VideosList.{fileType}'
    fileExists = True if os.path.isfile(f'./{filename}') else False

    def newWriteFormat():
        userResponse = input()
        if 'proceed' in userResponse.strip().lower():
            return 'w'
        elif 'skip' in userResponse.strip().lower():
            return 0
        else:
            print ('\n' + cMessage.invalidResponse)
            cMessage.fileAlreadyExistsPrompt(filename)
            return newWriteFormat()

    if fileExists is True:
        cMessage.fileAlreadyExistsWarning(filename)
        cMessage.fileAlreadyExistsPrompt(filename)
        return newWriteFormat()
    return 'x'

def setupBrowser(userBrowser):
    if 'firefox' in userBrowser:
        return webdriver.Firefox
    elif 'chrome' in userBrowser:
        return webdriver.Chrome
    elif 'opera' in userBrowser:
        return webdriver.Opera
    elif 'safari' in userBrowser:
        return webdriver.Safari
    else:
        print (cMessage.invalidBrowser)
        return 'invalid'

def logic(channel, channelType, fileName, txt, txtWriteFormat, csv, csvWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, userBrowser, executionType):
    mMessage = ModuleMessage()
    cMessage = Common()
    channel = channel.strip().strip('/')
    channelType = channelType.strip().strip('/')

    def determineFileName(fileName):
        if fileName is not None:
            return fileName
        else:
            return channel

    fileName = determineFileName(fileName)

    if txt is True and txtWriteFormat == 'x':
        txtWriteFormat = verifyWriteFormat(fileName, 'txt')

    if csv is True and csvWriteFormat == 'x':
        csvWriteFormat = verifyWriteFormat(fileName, 'csv')

    if docx is True and docxWriteFormat == 'x' is True:
        docxWriteFormat = verifyWriteFormat(fileName, 'docx')

    if userBrowser is None:
        print (cMessage.runningDefaultBrowser)
        print (cMessage.showBrowserOptions)
        userBrowser = 'firefox'

    driver = setupBrowser(userBrowser)
    if driver == 'invalid':
        return

    programStart = time.perf_counter()
    try:
        if headless is False: # opens Selenium browsing instance
            driver = driver()
            if executionType == 'module':
                print (mMessage.runInHeadless)
                print (mMessage.runInHeadlessExample)
        else: # headless is True
            if userBrowser == 'firefox':
                options = selenium.webdriver.firefox.options.Options()
                options.headless = True
                driver = driver(options=options)
            if userBrowser == 'chrome':
                # options = selenium.webdriver.chrome.options.Options()
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = driver(chrome_options=options)
            if userBrowser == 'opera':
                # Opera driver MRO: WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
                # options = selenium.webdriver.chrome.options.Options()
                # options.headless = True
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = driver(options=options)
                print (cMessage.unsupportedOperaHeadless)
            if userBrowser == 'safari':
                driver = driver()
                print (cMessage.unsupportedSafariHeadless)
    except selenium.common.exceptions.WebDriverException as e:
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        cMessage.seleniumDependencyError(e)
        if platform.system().lower().startswith('darwin'):
            userOS = 'macos'
        elif platform.system().lower().startswith('windows'):
            userOS = 'windows'
        elif platform.system().lower().startswith('linux'):
            userOS = 'linux'
        else:
            print (cMessage.unsupportedOS)

        if userBrowser != 'safari':
            cMessage.tellUserToDownloadBrowser(userBrowser)
        for browserVersionDownload in cMessage.browsersForOS[userBrowser][userOS]:
            print (browserVersionDownload)
        return

    with driver:
        videosList = program.scrollToBottom(channel, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (cMessage.noVideosFound)
            print (mMessage.checkChannelType) if executionType == 'module' else print (sMessage.checkChannelType)
            return
        if txt is True:
            program.writeToTxt(videosList, channel, fileName, txtWriteFormat, chronological)
            # saveToMemWriteToTxt(videosList, channel, fileName, writeFormat) # slightly slower than writing to disk directly
        if csv is True:
            program.writeToCsv(videosList, channel, fileName, csvWriteFormat, chronological)

    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
