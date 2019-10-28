# https://www.softwaretestingmaterial.com/how-to-locate-element-by-xpath-locator/
# https://stackoverflow.com/questions/27307131/selenium-webdriver-how-do-i-find-all-of-an-elements-attributes
# https://pythonbasics.org/selenium_scroll_down/ # does not work on YouTube since scrollHeight returns 0


from selenium import webdriver
from pprint import pprint
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/user/sentdex/videos')

element = driver.find_element_by_xpath('//*[@id="video-title"]') # CHANGE THIS LINE TO TEST ON DIFFERENT PAGE
attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
pprint(attrs)
