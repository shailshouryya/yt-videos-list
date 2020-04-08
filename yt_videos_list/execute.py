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
    def determine_file_name():
        if fileName is not None:
            return fileName
        else:
            return channel

    def verify_write_format(fileType, writeFormat, fileName, fileExtension):
        def new_write_format():
                userResponse = input()
                if 'proceed' in userResponse.strip().lower():
                    return 'w'
                elif 'skip' in userResponse.strip().lower():
                    return 0
                else:
                    print ('\n' + commonMessage.invalidResponse)
                    commonMessage.display_file_already_exists_prompt(filename)
                    return new_write_format()

        if fileType is True and writeFormat == 'x':
            filename   = f'{fileName}VideosList.{fileExtension}'
            fileExists = True if os.path.isfile(f'./{filename}') else False
            if fileExists is True:
                commonMessage.display_file_already_exists_warning(filename)
                commonMessage.display_file_already_exists_prompt(filename)
                return new_write_format()
            return 'x'
        else:
            return writeFormat

    def check_driver():
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

    def open_user_driver():
        if headless is False: # opens Selenium browsing instance
            driver = seleniumdriver()
            if executionType == 'module':
                print (moduleMessage.runInHeadless)
                print (moduleMessage.runInHeadlessExample)
        else: # headless is True
            if userDriver == 'firefox':
                options = selenium.webdriver.firefox.options.Options()
                options.headless = True
                driver = seleniumdriver(options=options)
            elif userDriver == 'chrome':
                # options = selenium.webdriver.chrome.options.Options()
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = seleniumdriver(chrome_options=options)
            elif userDriver == 'opera':
                # Opera driver MRO: WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
                # options = selenium.webdriver.chrome.options.Options()
                # options.headless = True
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                driver = seleniumdriver(options=options)
                print (commonMessage.unsupportedOperaHeadless)
            elif userDriver == 'safari':
                driver = seleniumdriver()
                print (commonMessage.unsupportedSafariHeadless)
        return driver

    def determine_user_os():
        if platform.system().lower().startswith('darwin'):
            return 'macos'
        elif platform.system().lower().startswith('linux'):
            return 'linux'
        elif platform.system().lower().startswith('windows'):
            return 'windows'
        else:
            print (commonMessage.unsupportedOS)
            sys.exit()

    def show_user_how_to_setuo_selenium():
        if userDriver != 'safari':
            commonMessage.tell_user_to_download_driver(userDriver)
        commonMessage.display_dependency_setup_instructions(userDriver, userOS)

    def check_user_input():
        nonlocal channel, channelType, fileName, txtWriteFormat, csvWriteFormat, docxWriteFormat, userDriver
        channel     = channel.strip().strip('/')
        channelType = channelType.strip().strip('/')
        baseUrl     = 'https://www.youtube.com'
        videos      = 'videos'
        url         = f'{baseUrl}/{channelType}/{channel}/{videos}'

        fileName = determine_file_name()
        txtWriteFormat  = verify_write_format(txt,  txtWriteFormat,  fileName, 'txt')
        csvWriteFormat  = verify_write_format(csv,  csvWriteFormat,  fileName, 'csv')
        docxWriteFormat = verify_write_format(docx, docxWriteFormat, fileName, 'docx')

        if (txtWriteFormat == 0 and csvWriteFormat == 0) or (txt is False and csv is False):
            print (commonMessage.notWritingToAnyFiles)
            print (moduleMessage.notWritingToAnyFilesHint) if executionType == 'module' else print (scriptMessage.notWritingToAnyFilesHint)
            return # the files already exist and the user doesn't want to overwrite either of them

        if userDriver is None:
            print (moduleMessage.runningDefaultDriver) if executionType == 'module' else print (scriptMessage.runningDefaultDriver)
            print (moduleMessage.showDriverOptions)    if executionType == 'module' else print (scriptMessage.showDriverOptions)
            userDriver = 'firefox'
        seleniumdriver = check_driver()
        if seleniumdriver == 'invalid':
            return
        return url, seleniumdriver




    url, seleniumdriver = check_user_input()
    programStart = time.perf_counter()
    try:
        driver = open_user_driver()
    except selenium.common.exceptions.WebDriverException as e:
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        commonMessage.display_selenium_dependency_error(e)
        userOS = determine_user_os()
        try:
            globals()[f'selenium_{userOS}'].download(userDriver)
            sys.exit() # skip this try block for now until the logic to install the correct Selenium driver based on the user's OS and specified driver is added
            driver = open_user_driver()
        except: # could not download the correct Selenium driver based on the user's OS and specified driver
            show_user_how_to_setuo_selenium()
            return
    with driver:
        videosList = program.scroll_to_bottom(url, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (commonMessage.noVideosFound)
            print (moduleMessage.checkChannelType) if executionType == 'module' else print (scriptMessage.checkChannelType)
            return
        if txt is True and txtWriteFormat != 0:
            program.write_to_txt(videosList, fileName, txtWriteFormat, chronological)
            # save_to_mem_write_to_txt(videosList, fileName, writeFormat) # slightly slower than writing to disk directly
        if csv is True and csvWriteFormat != 0:
            program.write_to_csv(videosList, fileName, csvWriteFormat, chronological)
    programEnd = time.perf_counter()
    totalTime  = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
