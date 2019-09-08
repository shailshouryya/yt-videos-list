from output import Common, ModuleMessage, ScriptMessage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pprint import pprint
import csv

cMessage = Common()
sMessage = ScriptMessage()

def scrollToBottom (channelName, channelType, seleniumInstance, scrollPauseTime):
    start = time.perf_counter()
    driver = seleniumInstance
    
    baseUrl = 'https://www.youtube.com'
    videos = 'videos'
    url = baseUrl + '/' + channelType + '/' + channelName + '/' + videos 
    
    driver.get(url)
    elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
    
    while True:
        driver.execute_script("window.scrollBy(0, 50000);")
        time.sleep(scrollPauseTime)
        new_elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
        print (f'Found {new_elemsCount} videos...')
    
        if new_elemsCount == elemsCount:
            # wait 0.6 seconds and check again to verify you really did reach the end of the page, and there wasn't a buffer loading period
            print (cMessage.noNoVideosFound)
            time.sleep(0.6)
            new_elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
            if new_elemsCount == elemsCount:
                print('Reached end of page!')
                break
        elemsCount = new_elemsCount
        
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end = time.perf_counter()
    functionTime = end - start - 2 # subtract 2 to account for the extra waiting time to verify end of page
    print(f'It took {functionTime} to find all {len(elements)} videos from {url}\n')
    return elements

def writeToTxt (listOfVideos, userName, writeFormat='w'):
    start = time.perf_counter()
    with open('{}VideosList.txt'.format(userName.strip('/')), writeFormat) as f:
        print (f'Opened {f.name}, writing video information to file....')
        
        spacing = '\n    ' # newline followed by 4 spaces
        for index, element in enumerate(listOfVideos, 1):
            f.write(f'Index:{spacing}{index}\n')
            f.write(f'Watched?{spacing}\n')
            f.write(f'Video Title:{spacing}{element.get_attribute("title")}\n')
            f.write(f'Video URL:{spacing}{element.get_attribute("href")}\n')
            f.write(f'Watch again later?{spacing}\n')
            f.write(f'Notes:{spacing}\n')
            
            f.write('*'*75 + '\n')
            if index % 250 == 0:
                print (f'{index} videos written to {f.name}...')
        print (f'Finished writing to {f.name}')
        print (f'{index} videos written to {f.name}')
        print (f'Closing {f.name}\n')
        
        end = time.perf_counter()
        functionTime = end - start
        print(f'It took {functionTime} to write all {index} videos to {f.name}\n')
        
def saveToMemWriteToTxt (listOfVideos, userName, writeFormat='w'):
    start = time.perf_counter()
    with open('{}VideosList.txt'.format(userName.strip('/')), writeFormat) as fm:
        print (f'Opened {fm.name}, writing video information to file....')
        
        text = ''
        spacing = '\n    ' # newline followed by 4 spaces
        for index, element in enumerate(listOfVideos, 1):
            text += f'Index:{spacing}{index}' + '\n'
            text += f'Watched?{spacing}' + '\n'
            text += f'Video Title:{spacing}{element.get_attribute("title")}' + '\n'
            text += f'Video URL:{spacing}{element.get_attribute("href")}' + '\n'
            text += f'Watch again later?{spacing}' + '\n'
            text += f'Notes:{spacing}' + '\n'
            
            text += '*'*75 + '\n'
            if index % 250 == 0:
                print (f'{index} videos saved to memory...')
        
        print (f'Finished saving video information to memory')
        fm.write(text)
        print (f'{index} videos written to {fm.name}')
        print (f'Closing {fm.name}\n')
        end = time.perf_counter()
        functionTime = end - start
        print(f'It took {functionTime} to write all {index} videos to {fm.name}\n')

def writeToCsv (listOfVideos, userName, writeFormat='w'):
    with open('{}VideosList.csv'.format(userName.strip('/')), writeFormat) as csvfile:
        print (f'Opened {csvfile.name}, writing video information to file....')
        fieldnames = ['Index', 'Watched?', 'Video Title', 'Video URL', 'Watch again later?', 'Notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for index, element in enumerate(listOfVideos, 1):
            writer.writerow({'Index': f'{index}', 'Watched?': '', 'Video Title': f'{element.get_attribute("title")}', 'Video URL': f'{element.get_attribute("href")}', 'Watch again later?': '', 'Notes': ''})
            if index % 250 == 0:
                print(f'{index} videos written to {csvfile.name}...')
        print (f'Finished writing to {csvfile.name}')
        print (f'{index} videos written to {csvfile.name}')
        print (f'Closing {csvfile.name}\n')
        
def run(channelName, channelType, csv, csvWriteFormat, txt, txtWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, executionType):
    mMessage = ModuleMessage()
    channelName = channelName.strip().strip('/')
    channelType = channelType.strip().strip('/')
        
    programStart = time.perf_counter()
    if headless is False: # opens Selenium browsing instance
        driver = webdriver.Firefox()
        if executionType == 'module':
            print (mMessage.runInHeadless)
            print (mMessage.runInHeadlessExample)
    else:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        
    with driver:
        videosList = scrollToBottom(channelName, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (cMessage.noVideosFound)
            print (mMessage.checkChannelType) if executionType == 'module' else print (sMessage.checkChannelType)
            return
        if csv is True:
            try:
                writeToCsv(videosList, channelName, csvWriteFormat)
            except FileExistsError as e:
                print (e)
                print (mMessage.fileAlreadyExists)
                print (mMessage.fileAlreadyExistsRerunUsage)
        if txt is True:
            try:
                writeToTxt(videosList, channelName, txtWriteFormat)
                # saveToMemWriteToTxt(videosList, channelName, writeFormat) # slightly slower than writing to disk directly
            except FileExistsError as e:
                print (e)
                print (mMessage.fileAlreadyExists)
                print (mMessage.fileAlreadyExistsRerunUsage)
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
