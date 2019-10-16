from yt_videos_list.output import Common, ModuleMessage, ScriptMessage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import csv
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

def scrollToBottom (channel, channelType, seleniumInstance, scrollPauseTime):
    start = time.perf_counter()
    driver = seleniumInstance
    
    baseUrl = 'https://www.youtube.com'
    videos = 'videos'
    url = baseUrl + '/' + channelType + '/' + channel + '/' + videos 
    
    driver.get(url)
    elemsCount = driver.execute_script(
    "return document.querySelectorAll('ytd-grid-video-renderer').length"
    )
    
    while True:
        driver.execute_script("window.scrollBy(0, 50000);")
        time.sleep(scrollPauseTime)
        newElemsCount = driver.execute_script(
        "return document.querySelectorAll('ytd-grid-video-renderer').length"
        )
        print (f'Found {newElemsCount} videos...')
    
        if newElemsCount == elemsCount:
            # wait 0.6 seconds and check again to verify you really did reach the end of the page, and there wasn't a buffer loading period
            print (cMessage.noNewVideosFound)
            time.sleep(0.6)
            newElemsCount = driver.execute_script(
            "return document.querySelectorAll('ytd-grid-video-renderer').length"
            )
            if newElemsCount == elemsCount:
                print('Reached end of page!')
                break
        elemsCount = newElemsCount
        
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end = time.perf_counter()
    functionTime = end - start - 0.6 # subtract 0.6 to account for the extra waiting time to verify end of page
    print(f'It took {functionTime} to find all {len(elements)} videos from {url}\n')
    return elements

def writeToTxt (listOfVideos, channel, fileName, writeFormat):
    if writeFormat == 0:
        return
    
    start = time.perf_counter()
    with open(f'{fileName}VideosList.txt', writeFormat) as f:
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
        
def saveToMemWriteToTxt (listOfVideos, channel, fileName, writeFormat):
    if writeFormat == 0:
        return
    
    start = time.perf_counter()
    with open(f'{fileName}VideosList.txt', writeFormat) as fm:
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

def writeToCsv (listOfVideos, channel, fileName, writeFormat):
    if writeFormat == 0:
        return
    
    start = time.perf_counter()
    with open(f'{fileName}VideosList.csv', writeFormat) as csvfile:
        print (f'Opened {csvfile.name}, writing video information to file....')
        fieldnames = ['Index', 'Watched?', 'Video Title', 'Video URL', 'Watch again later?', 'Notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for index, element in enumerate(listOfVideos, 1):
            writer.writerow(
            {'Index': f'{index}', 'Watched?': '', 'Video Title': f'{element.get_attribute("title")}', 'Video URL': f'{element.get_attribute("href")}', 'Watch again later?': '', 'Notes': ''})
            if index % 250 == 0:
                print(f'{index} videos written to {csvfile.name}...')
        print (f'Finished writing to {csvfile.name}')
        print (f'{index} videos written to {csvfile.name}')
        print (f'Closing {csvfile.name}\n')
        end = time.perf_counter()
        functionTime = end - start
        print(f'It took {functionTime} to write all {index} videos to {csvfile.name}\n')
