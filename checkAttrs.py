from selenium import webdriver
from pprint import pprint
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/user/sentdex/videos')

element = driver.find_element_by_xpath('//*[@id="video-title"]')
attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
pprint(attrs)
