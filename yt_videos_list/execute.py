from yt_videos_list import program
from yt_videos_list.output import Common, ModuleMessage, ScriptMessage
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

cMessage = Common()
sMessage = ScriptMessage()

def checkFileExists(filename):
    if os.path.isfile(f'./{filename}'):
        return True
    return False

def verifyWriteFormat(fileName, fileType):
    filename = f'{fileName}VideosList.{fileType}'
    fileExists = checkFileExists(filename)

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
    if userBrowser is None or 'firefox' in userBrowser:
        if userBrowser is None:
            print (cMessage.runningDefaultBrowser)
            print (cMessage.showBrowserOptions)
        return webdriver.Firefox
    if 'chrome' in userBrowser:
        return webdriver.Chrome
    elif 'opera' in userBrowser:
        return webdriver.Opera
    elif 'safari' in userBrowser:
        return webdriver.Safari

def run(channel, channelType, fileName, txt, txtWriteFormat, csv, csvWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, userBrowser, executionType):
    mMessage = ModuleMessage()
    cMessage = Common()
    channel = channel.strip().strip('/')
    channelType = channelType.strip().strip('/')

    def determineFileName(fileName):
        if fileName is not None:
            return fileName
        else:
            return channel.strip('/')

    file_name = determineFileName(fileName)

    if txt is True and txtWriteFormat == 'x':
        txtWriteFormat = verifyWriteFormat(file_name, 'txt')

    if csv is True and csvWriteFormat == 'x':
        csvWriteFormat = verifyWriteFormat(file_name, 'csv')

    if docx is True and docxWriteFormat == 'x' is True:
        docxWriteFormat = verifyWriteFormat(file_name, 'docx')

    driver = setupBrowser(userBrowser)

    programStart = time.perf_counter()
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
            print ('\nHeadless mode is unsupported in OperaDriver. We are waiting on the Opera dev team to start offering support for headless mode to allow remote automation without opening a browser. We will update this when support is added...\n:)\n\n\n')
        if userBrowser == 'safari':
            driver = driver()
            print ('\nHeadless mode is unsupported in SafariDriver. We are waiting on Apple to start offering support for headless mode to allow remote automation without opening a browser. We will update this when support is added...\n:)\n\n\n')

    with driver:
        videosList = program.scrollToBottom(channel, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (cMessage.noVideosFound)
            print (mMessage.checkChannelType) if executionType == 'module' else print (sMessage.checkChannelType)
            return
        if txt is True:
            program.writeToTxt(videosList, channel, file_name, txtWriteFormat)
                # saveToMemWriteToTxt(videosList, channel, file_name, writeFormat) # slightly slower than writing to disk directly
        if csv is True:
            program.writeToCsv(videosList, channel, file_name, csvWriteFormat)

    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
