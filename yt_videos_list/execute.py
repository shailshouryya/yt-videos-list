from yt_videos_list import program
from yt_videos_list.output import Common, ModuleMessage, ScriptMessage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def run(channel, channelType, fileName, txt, txtWriteFormat, csv, csvWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime, executionType):
    mMessage = ModuleMessage()
    cMessage = Common()
    channel = channel.strip().strip('/')
    channelType = channelType.strip().strip('/')
    
    def determineFileName(fileName):
        if fileName is not None:
            return fileName
        else:
            return channel.strip('/')
    
    file_name = determineFileName(fileName)
    
    if txt is True and txtWriteFormat == 'x':
        txtWriteFormat = program.verifyWriteFormat(file_name, 'txt')
    
    if csv is True and csvWriteFormat == 'x':
        csvWriteFormat = program.verifyWriteFormat(file_name, 'csv')
    
    if docx is True and docxWriteFormat == 'x' is True:
        docxWriteFormat = program.verifyWriteFormat(file_name, 'docx')
        
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
        videosList = program.scrollToBottom(channel, channelType, driver, scrollPauseTime)
        if len(videosList) == 0:
            print (cMessage.noVideosFound)
            print (mMessage.checkChannelType) if executionType == 'module' else print (sMessage.checkChannelType)
            return
        if txt is True:
            program.writeToTxt(videosList, channel, file_name, txtWriteFormat)
                # saveToMemWriteToTxt(videosList, channel, file_name, writeFormat) # slightly slower than writing to disk directly
        if csv is True:
            program.writeToCsv(videosList, channel, file_name, csvWriteFormat)
        
    programEnd = time.perf_counter()
    totalTime = programEnd - programStart
    print(f'This program took {totalTime} seconds to complete.\n')
