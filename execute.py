import program
from output import Common, ModuleMessage, ScriptMessage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def run(channelName, channelType, csv, csvWriteFormat, txt, txtWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, executionType):
    mMessage = ModuleMessage()
    channelName = channelName.strip().strip('/')
    channelType = channelType.strip().strip('/')
    
    if csv is True and csvWriteFormat == 'x':
        csvWriteFormat = program.updateWriteFormat(channelName, 'csv')

    if txt is True and txtWriteFormat == 'x':
        txtWriteFormat = program.updateWriteFormat(channelName, 'txt')
        
    if docx is True and docxWriteFormat == 'x' is True:
        docxWriteFormat = program.updateWriteFormat(channelName, 'docx')
        
    programStart = time.perf_counter()
    if headless is False: # opens Selenium browsing instance
        driver = webdriver.Firefox()
        if executionType == 'module':
            print (mMessage.runInHeadless)
            print (mMessage.runInHeadlessExample)
    else:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        
    with driver:
        videosList = program.scrollToBottom(channelName, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (cMessage.noVideosFound)
            print (mMessage.checkChannelType) if executionType == 'module' else print (sMessage.checkChannelType)
            return
        if csv is True:
            program.writeToCsv(videosList, channelName, csvWriteFormat)
        if txt is True:
            program.writeToTxt(videosList, channelName, txtWriteFormat)
                # saveToMemWriteToTxt(videosList, channelName, writeFormat) # slightly slower than writing to disk directly
                
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')