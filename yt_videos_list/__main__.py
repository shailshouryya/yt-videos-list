try:
    from yt_videos_list import execute
except:
    import script

class ListGenerator:
    def __init__(self, txt=True, txtWriteFormat='x', csv=True, csvWriteFormat='x', docx=False, docxWriteFormat='x', chronological=True, headless=False, scrollPauseTime=0.8,):
        '''
        Creates a list generator object with one required positional argument (channel) and one optional argument (channelType). The channelType is set to "user" by default, but if the YouTube channel you are looking at is a "channel" instead of "user" - you will need to change the default channelType parameter to "channel"
        Example usage:
            LG = ListGenerator('theChannelYouWantToScrape')
            OR
            LG = ListGenerator('theChannelYouWantToScrape', 'channel')
        '''
        self.txt = txt
        self.txtWriteFormat = txtWriteFormat
        self.csv = csv
        self.csvWriteFormat = csvWriteFormat
        self.docx = docx
        self.docxWriteFormat = docxWriteFormat
        self.chronological = chronological
        self.headless = headless
        self.scrollPauseTime = scrollPauseTime
    
    def generate_list(self, channel, channelType, fileName=None, _executionType='module'):
        '''
        The generate_list method has been designed to make a CSV and text file by default, open an automated browsing instance, wait 0.5 seconds between scrolls when collecting video information from the provided channel for the ListGenerator instance, and open the designated CSV/text/docx file in exclusive creation mode - meaning the write operation fails if the file already exists.
    
        If you do not want to write to specific file types, include the optional parameter in the method call and set it equal to false. For instance:
            LG.generate_list(csv=False)
            LG.generate_list(txt=False)
        
        This function opens an instance of Selenium to allow you to easily see if it is not including all the videos for the channel you provided and allows you to see if the browsing instance is ending prematurely (could be due to long buffer period, low bandwidth, etc.), but if you DON'T want to open the automated browsing instance and prefer to run the program in headless mode, run the method with the optional argument "headless" set to True:
            LG.generate_list(headless=True)
            
        If the browsing instance is actually ending prematurely because the browser does not find any new videos loaded in the default pause time of 0.7 seconds, try increasing the scrollPauseTime to a progressively larger number until the automated browsing instance captures all the videos for the channel you provided (probably most helpful if used with headless disabled):
            LG.generate_list(headless=False, scrollPauseTime=1.1)
            
        If you want to overwrite an existing file of the same name, run the method with writeFormat set to 'w':
            LG.generate_list(writeFormat='w')
            
        NOTE! You can use a combination of the optional parameters (or all the optional parameters at once) in the method call, you do not need to use them one at a time. The reason it is shown one at a time here in the documentation is to highlight what each parameter does.
        '''
        execute.run(channel, channelType, fileName, self.txt, self.txtWriteFormat, self.csv, self.csvWriteFormat, self.docx, self.docxWriteFormat, self.chronological, self.headless, self.scrollPauseTime, _executionType)

def main():
    script.run()
        
if __name__ == '__main__':
    main()
