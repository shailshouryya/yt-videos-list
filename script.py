

def script():
    channelName = input(eMessage.inputMessage)    
#     if -i --invisible: open selenium in headless mode
#     options = Options()
#     options.headless = True
#     driver = webdriver.Firefox(options=options)
#     else open selenium instance
    driver = webdriver.Firefox()
#     if -p --pause=# scrollPauseTime = #
#     else scrollPauseTime = 0.8
    scrollPauseTime = 0.8
#     if -c --channelType is channel set channelType = 'channel'
#     else channelType = 'user'
    channelType = 'user' # hardcoded until CLI added
    with driver:
        videosList = scrollToBottom(channelName, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (eMessage.noVideosFound)
            print (eMessage.checkChannelType)
            return
#         if cli -o --overwrite write_format = 'w'
#         else write_format = 'x'
        write_format = 'w'
        writeToTxt(videosList, channelName, write_format)
        writeToCsv(videosList, channelName, write_format)
    run(channelName, channelType, csv, csvWriteFormat, txt, txtWriteFormat, docx, docxWriteFormat, headless, scrollPauseTime, _executionType='script')