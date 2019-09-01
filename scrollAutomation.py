from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pprint import pprint
import csv

def scrollToBottom(url):
    start = time.perf_counter()
    driver.get(channelVideosUrl)
    SCROLL_PAUSE_TIME = 0.8
    
    elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
    while True:
        driver.execute_script("window.scrollBy(0, 50000);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
        print (f'Found {new_elemsCount} videos...')
    
        if new_elemsCount == elemsCount:
            # wait 2 seconds and check again to verify you really did reach the end of the page, and there wasn't a buffer loading period
            time.sleep(2)
            if new_elemsCount == elemsCount:
                print('Reached end of page!')
                break
        elemsCount = new_elemsCount
        
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    end = time.perf_counter()
    functionTime = end - start - 2 # subtract 2 to account for the extra waiting time to verify end of page
    print(f'It took {functionTime} to extract all {len(elements)} videos from {channelVideosUrl}\n')
    return elements

def writeToTxt(listOfVideos):
    with open('{}VideosList.txt'.format(userName.strip('/')), 'w+') as f:
        print (f'Opened {f.name}, writing video information to file....')
        for index, element in enumerate(listOfVideos, 1):
            f.write(f'title: {element.get_attribute("title")}\n')
            f.write(f'href: {element.get_attribute("href")}\n')
            f.write('*'*75 + '\n')
            if index % 250 == 0:
                print (f'{index} videos written to {f.name}...')
        print (f'Finished writing to {f.name}')
        print (f'{index} videos written to {f.name}')
        print (f'Closing {f.name}\n')

def writeToCsv (listOfVideos):
    with open('{}VideosList.csv'.format(userName.strip('/')), 'w+') as csvfile:
        print (f'Opened {csvfile.name}, writing video information to file....')
        fieldnames = ['Index', 'Watched?', 'Video Title', "Video URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for index, element in enumerate(listOfVideos, 1):
            writer.writerow({'Index': f'{index}', 'Watched?': '', 'Video Title': f'{element.get_attribute("title")}', 'Video URL': f'{element.get_attribute("href")}'})
            if index % 250 == 0:
                print(f'{index} videos written to {csvfile.name}...')
        
        print (f'Finished writing to {csvfile.name}')
        print (f'{index} videos written to {csvfile.name}')
        print (f'Closing {csvfile.name}\n')
        
if __name__ == '__main__':
    programStart = time.perf_counter()
    
    baseUrl = 'https://www.youtube.com'
    user = 'user/'
    userName = 'sentdex/'
    videos = 'videos'
    channelVideosUrl = baseUrl + '/' + user + userName + videos
    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    with driver:
        videosList = scrollToBottom(channelVideosUrl)
        writeToTxt(videosList)
        writeToCsv(videosList)
    
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.')