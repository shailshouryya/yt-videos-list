# https://pythonbasics.org/selenium_scroll_down/ # does not work on YouTube since scrollHeight returns 0

from selenium import webdriver
import time
import timeit

driver = webdriver.Firefox()
with driver:
    driver.get('https://www.youtube.com/user/sentdex/videos')

    SCROLL_PAUSE_TIME = 2
    elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")

    while True:
        driver.execute_script("window.scrollBy(0, 50000);")
        time.sleep(SCROLL_PAUSE_TIME)
        start = time.clock()
        new_elemsCount = driver.execute_script("return document.querySelectorAll('ytd-grid-video-renderer').length")
        end = time.clock()
#         print(timeit.Timer('driver.execute_script("return document.querySelectorAll(/"ytd-grid-video-renderer/").length")'))
        print(end - start)
        print (new_elemsCount)
        if new_elemsCount == elemsCount:
            print('Reached end of page!')
            break
        elemsCount = new_elemsCount
    
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    # with open('')
#     for element in elements:
#         print(f'class: {element.get_attribute("class")}')
#         print(f'href: {element.get_attribute("href")}')
#         print(f'title: {element.get_attribute("title")}')
