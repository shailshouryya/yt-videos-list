# https://pythonbasics.org/selenium_scroll_down/ # does not work on YouTube since scrollHeight returns 0

from selenium import webdriver
import time
import timeit
from pprint import pprint
import csv

baseUrl = 'https://www.youtube.com'
user = 'user/'
userName = 'sentdex/'
videos = 'videos'
channelVideosUrl = baseUrl + '/' + user + userName + videos

driver = webdriver.Firefox()
with driver:
    driver.get(channelVideosUrl)
    SCROLL_PAUSE_TIME = 1
    
    # # to check the attributes you want to extract
    # element = driver.find_element_by_xpath('//*[@id="video-title"]') # CHANGE THIS LINE TO TEST ON DIFFERENT PAGE
    # attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    # pprint(attrs)


    elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
    while True:
        driver.execute_script("window.scrollBy(0, 50000);")
        time.sleep(SCROLL_PAUSE_TIME)
        # start = time.clock()
        # DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
        start = time.perf_counter()
        new_elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
        end = time.perf_counter()
        print(end - start)
        print (new_elemsCount)
        
        if new_elemsCount == elemsCount:
            print('Reached end of page!')
            break
        elemsCount = new_elemsCount
    
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')

    with open('{}VideosList.txt'.format(userName.strip('/')), 'w+') as f:
        counter = 0
        for element in elements:
            f.write(f'title: {element.get_attribute("title")}\n')
            f.write(f'href: {element.get_attribute("href")}\n')
            f.write('*'*75 + '\n')
            counter += 1
            if counter % 10 == 0:
                print (f'{counter} videos written to {f.name}...')
        print(f'Finished writing to {f.name}')
        print (f'{counter} videos written to {f.name}')
        print (f'Closing {f.name}')

    with open('{}VideosList.csv'.format(userName.strip('/')), 'w+') as csvfile:
        fieldnames = ['Index', 'Watched?', 'Video Title', "Video URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, element in enumerate(elements, 1):
            writer.writerow({'Index': f'{index}', 'Watched?': '', 'Video Title': f'{element.get_attribute("title")}', 'Video URL': f'{element.get_attribute("href")}'})
            if index % 10 == 0:
                print(f'{index} videos written to {csvfile.name}...')
        print ('Finished writing to {}VideosList.csv'.format(userName.strip('/')))
        print (f'{counter} videos written to {csvfile.name}')
        print ('Closing {}VideosList.csv'.format(userName.strip('/')))