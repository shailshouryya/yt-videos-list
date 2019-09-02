from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pprint import pprint
import csv



def scrollToBottom (user_name, seleniumInstance, scroll_pause_time=0.8):
    start = time.perf_counter()
    driver = seleniumInstance
    
    userName = user_name
    baseUrl = 'https://www.youtube.com'
    user = 'user/'
    videos = 'videos'
    url = baseUrl + '/' + user + userName + videos 
    
    driver.get(url)
    SCROLL_PAUSE_TIME = scroll_pause_time
    
    elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
    while True:
        driver.execute_script("window.scrollBy(0, 50000);")
#         time.sleep(SCROLL_PAUSE_TIME)
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
    print(f'It took {functionTime} to find all {len(elements)} videos from {url}\n')
    return elements

def writeToTxt (listOfVideos, userName, writeFormat='w'):
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

def main():
    programStart = time.perf_counter()

    user_name = 'sentdex/'
    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    with driver:
        videosList = scrollToBottom(user_name, driver)
        writeToTxt(videosList, user_name)
        writeToCsv(videosList, user_name)
    
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.')

if __name__ == '__main__':
    main()