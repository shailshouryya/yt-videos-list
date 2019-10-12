from yt_videos_list import program
from yt_videos_list.output import Common, ModuleMessage, ScriptMessage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def run(channelName, channelType, fileName, csv, csvWriteFormat, txt, txtWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, executionType):
    mMessage = ModuleMessage()
    cMessage = Common()
    channelName = channelName.strip().strip('/')
    channelType = channelType.strip().strip('/')
    
    def determineFileName(fileName):
        if fileName is not None:
            return fileName
        else:
            return channelName.strip('/')
    
    file_name = determineFileName(fileName)
    
    if csv is True and csvWriteFormat == 'x':
        csvWriteFormat = program.updateWriteFormat(file_name, 'csv')

    if txt is True and txtWriteFormat == 'x':
        txtWriteFormat = program.updateWriteFormat(file_name, 'txt')
        
    if docx is True and docxWriteFormat == 'x' is True:
        docxWriteFormat = program.updateWriteFormat(file_name, 'docx')
        
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
            program.writeToCsv(videosList, channelName, file_name, csvWriteFormat)
        if txt is True:
            program.writeToTxt(videosList, channelName, file_name, txtWriteFormat)
                # saveToMemWriteToTxt(videosList, channelName, file_name, writeFormat) # slightly slower than writing to disk directly
                
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
