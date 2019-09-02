from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pprint import pprint
import csv

def cli():
    '''
    Provides optional arguments for user increased visibility. Note that using some of the arguments may slow down run time and program may take slightly longer to execute.
    '''
    '''
    
    first argument should be channel/user name
    -c --channelType sets channelType to "channel"
    -o --overwrite overwrite file if a file of the same name already exists in the output directory
    --version shows version number and exits
    --csv writes to csv file
    --txt writes to txt file
    --docx writes to word dox (not yet available)
    -v --verbose print every 10 videos written to file
    -i --invisible opens a headless instance of the selenium browser to run the program in the background
    -q --quiet suppresses program updates, only prints to stdout when scrolling is complete files are opened and closed, and any errors that may occur
    -h --help display information on usage and functionality
    -p --pause change pause time between scrolls, set to 0.8s by default
    -r --reverse reverse the indexing so oldest video starts at 1 and most recent video has highest index
    '''
    pass

def scrollToBottom (channelName, channelType, seleniumInstance, scroll_pause_time):
    start = time.perf_counter()
    driver = seleniumInstance
    
    baseUrl = 'https://www.youtube.com'
    channelType = channelType.strip().strip('/')
    channelName = channelName.strip().strip('/')
    videos = 'videos'
    url = baseUrl + '/' + channelType + '/' + channelName + '/' + videos 
    
    driver.get(url)
    SCROLL_PAUSE_TIME = scroll_pause_time
    
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

    channelName = input("What is the name of the YouTube channel you want to generate the list for?" + "\n\n" + "If you're unsure, click on the channel and look at the URL." + "\n" + "It should be in the format:" + "\n" + "https://www.youtube.com/user/YourChannelName" + "\n" + "OR" + "\n" + "https://www.youtube.com/channel/YourChannelName" + "\n\n" + "Substitute what you see for YourChannelName and type it in below (NOTE: if your url looks like the second option, you need to run this script with the -c or --channel flag):\n")
    programStart = time.perf_counter()
    
#     if -i --invisible: open selenium in headless mode
#     options = Options()
#     options.headless = True
#     driver = webdriver.Firefox(options=options)
#     else open selenium instance
    driver = webdriver.Firefox()
#     if -p --pause=# scroll_pause_time = #
#     else scroll_pause_time = 0.8
    scroll_pause_time = 0.8
#     if -c --channelType is channel set channelType = 'channel'
#     else channelType = 'user'
    channelType = 'user' # hardcoded until CLI added
    with driver:
        videosList = scrollToBottom(channelName, channelType, driver, scroll_pause_time)
        if len(videosList) == 0:
            print ('No videos were found for the channel you provided. Are you sure you typed in the channel name correctly?\n')
            print ('If you did type the name in correctly, perhaps the channelType is set incorrectly. Try using the -c or --channelType flag for this script if you didn\'t do it when running this script, or try running the script without the -c or --channelType flag if you DID include that flag when running this script.')
            return
#         if cli -o --overwrite write_format = 'w'
#         else write_format = 'x'
        write_format = 'w'
        writeToTxt(videosList, channelName, write_format)
        writeToCsv(videosList, channelName, write_format)
    
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.')

if __name__ == '__main__':
    main()