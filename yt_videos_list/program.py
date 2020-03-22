from .notifications import Common
from selenium import webdriver
import functools
import time
import csv

commonMessage = Common()


def scrollToBottom (channel, channelType, seleniumInstance, scrollPauseTime):
    def navigateToChannel():
        baseUrl = 'https://www.youtube.com'
        videos = 'videos'
        url = f'{baseUrl}/{channelType}/{channel}/{videos}'
        driver.get(url)
        return url

    def scrollDown(currentElementsCount):
        driver.execute_script('window.scrollBy(0, 50000);')
        time.sleep(scrollPauseTime)
        newElementsCount = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
        print (f'Found {newElementsCount} videos...')
        # if the number of elements after scroll is the same as the number of elements before the scroll
        if newElementsCount == currentElementsCount:
            # wait 0.6 seconds and check again to verify you really did reach the end of the page, and there wasn't a buffer loading period
            print (commonMessage.noNewVideosFound)
            time.sleep(0.6)
            newElementsCount = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
            if newElementsCount == currentElementsCount:
                print('Reached end of page!')
        return newElementsCount

    def saveElementsToList():
        elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
        end = time.perf_counter()
        functionTime = end - start - 0.6 # subtract 0.6 to account for the extra waiting time to verify end of page
        print(f'It took {functionTime} seconds to find all {len(elements)} videos from {url}\n')
        return elements


    seleniumInstance.set_window_size(780, 880)
    start = time.perf_counter()
    driver = seleniumInstance
    url = navigateToChannel()

    currentElementsCount = driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')
    while True:
        newElementsCount = scrollDown(currentElementsCount)
        if newElementsCount == currentElementsCount:
            break
        else:
            currentElementsCount = newElementsCount
    return saveElementsToList()


def timeWriterFunction(writerFunction):
    @functools.wraps(writerFunction)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()

        ########### check the name of the file and how many videos were written ###########
        filename, videosWritten = writerFunction(*args, **kwargs)

        end = time.perf_counter()
        functionTime = end - start

        print (f'Finished writing to {filename}')
        print (f'{videosWritten} videos written to {filename}')
        print (f'Closing {filename}\n')
        print(f'It took {functionTime} to write all {videosWritten} videos to {filename}\n')
    return wrapper_timer


@timeWriterFunction
def writeToTxt (listOfVideos, channel, fileName, writeFormat, chronological):
    with open(f'{fileName}VideosList.txt', writeFormat) as txtFile:
        print (f'Opened {txtFile.name}, writing video information to file....')
        spacing = '\n' + ' '*12 # newline followed by 12 spaces on the next line to pad the start of the line

        ####################################################
        ########## iterate through list of videos ##########
        ####################################################

        for videoNumber, seleniumElement in enumerate(listOfVideos, 1) if chronological is False else enumerate(listOfVideos[::-1], 1):
            txtFile.write(f'videoNumber:{spacing}{videoNumber}\n')
            txtFile.write(f'Watched?{spacing}\n')
            txtFile.write(f'Video Title:{spacing}{seleniumElement.get_attribute("title")}\n')
            txtFile.write(f'Video URL:{spacing}{seleniumElement.get_attribute("href")}\n')
            txtFile.write(f'Watch again later?{spacing}\n')
            txtFile.write(f'Notes:{spacing}\n')
            ################################################################
            ########## add asterisks as separators between videos ##########
            ################################################################
            txtFile.write('*'*75 + '\n')
            if videoNumber % 250 == 0:
                print (f'{videoNumber} videos written to {txtFile.name}...')
    return txtFile.name, videoNumber


@timeWriterFunction
def saveToMemWriteToTxt (listOfVideos, channel, fileName, writeFormat, chronological):
    # this takes a little bit longer than the writeToCsv() function
    with open(f'{fileName}VideosList.txt', writeFormat) as fm:
        print (f'Opened {fm.name}, writing video information to file....')
        text = ''
        spacing = '\n' + ' '*12 # newline followed by 12 spaces on the next line to pad the start of the line

        ####################################################
        ########## iterate through list of videos ##########
        ####################################################

        for videoNumber, seleniumElement in enumerate(listOfVideos, 1) if chronological is False else enumerate(listOfVideos[::-1], 1):
            text += f'videoNumber:{spacing}{videoNumber}\n'
            text += f'Watched?{spacing}\n'
            text += f'Video Title:{spacing}{seleniumElement.get_attribute("title")}\n'
            text += f'Video URL:{spacing}{seleniumElement.get_attribute("href")}\n'
            text += f'Watch again later?{spacing}\n'
            text += f'Notes:{spacing}\n'
            ################################################################
            ########## add asterisks as separators between videos ##########
            ################################################################
            text += '*'*75 + '\n'
            if videoNumber % 250 == 0:
                print (f'{videoNumber} videos saved to memory...')
        ####################################################
        ######### finished writing info to memory ##########
        ####################################################
        print (f'Finished saving video information to memory')
        fm.write(text)
    return fm.name, videoNumber


@timeWriterFunction
def writeToCsv (listOfVideos, channel, fileName, writeFormat, chronological):
    with open(f'{fileName}VideosList.csv', writeFormat) as csvFile:
        print (f'Opened {csvFile.name}, writing video information to file....')
        fieldnames = ['videoNumber', 'Watched?', 'Video Title', 'Video URL', 'Watch again later?', 'Notes']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()

        ####################################################
        ########## iterate through list of videos ##########
        ####################################################

        for videoNumber, seleniumElement in enumerate(listOfVideos, 1) if chronological is False else enumerate(listOfVideos[::-1], 1):
            writer.writerow(
            {'videoNumber': f'{videoNumber}', 'Watched?': '', 'Video Title': f'{seleniumElement.get_attribute("title")}', 'Video URL': f'{seleniumElement.get_attribute("href")}', 'Watch again later?': '', 'Notes': ''})
            if videoNumber % 250 == 0:
                print(f'{videoNumber} videos written to {csvFile.name}...')
    return csvFile.name, videoNumber
