try:
    from yt_videos_list import execute
except:
    import script

class ListGenerator:
    def __init__(self, txt=True, txtWriteFormat='x', csv=True, csvWriteFormat='x', docx=False, docxWriteFormat='x', chronological=True, headless=False, scrollPauseTime=0.8):
        '''
        Creates a list generator object with no required arguments.
        Example usage:
            LG = ListGenerator()
        
        ###########################################################
        OPTIONAL: specify the settings you want to use by substituing the desired values for the default arguments.
        An overview is given directly below this, but for a full working example scroll to the bottom.
        
        Options for the file type arguments are True (default) - create a file for the specified type - or False - do not create a file for the specified type.
        txt=True  (default) OR txt=False 
        csv=True  (default) OR csv=False
        docx=True (unsupported) OR docx=False
        
        Options for the write formats are: 'x' (default) - does not overwrite an existing file with the same name - or 'w' - if an existing file with the same name exists, it will be overwritten.
        NOTE: if you specify the file type argument to be False, you don't need to touch this - the program will automatically skip this step.
        txtWriteFormat='x'  (default) OR txtWriteFormat='w'
        csvWriteFormat='x'  (default) OR csvWriteFormat='w'
        docsWriteFormat='x' (unsupported) OR docxWriteFormat='w'
        
        Options for the chronological argument are True (this is the only chronological option currently supported right now :D) - write the files in order from oldest videos to most recent - or False (currently UNSUPPORTED!) - write the files in order from most recent to oldest.
        chronological=True (default) OR chronological=False
        
        Options for the headless option are False (default) - run the browser with an open Selenium instance for viewing - or False - run the browser in "invisible" mode.
        headless=False (default) OR headless=True
        
        Options for the scrollPauseTime argument are any float values greater than 0 (default 0.8).
        The value you provide will be how long the program waits before trying to scroll the videos list page down for the channel you want to scrape.
        For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
        scrollPauseTime=0.8 (default)
        CAUTION: reducing this value too much will result in the programming not capturing all the videos, so be careful! Experiment :)
        
        ###########################################################
        WORKING EXAMPLES:
        For a ListGenerator object that creates csv files but no txt or docx files in headless mode with a 1 second pause between scrolls:
        LG = ListGenerator(txt=True, txtWriteFormat='x', csv=False, csvWriteFormat=0, docx=False, docxWriteFormat=0, chronological=True, headless=True, scrollPauseTime=1.0)
        
        The same could also be done by specifying only the arguments that change from the default, but notice how this is less explicit and can become confusing if you forget what the default arguments are:
        LG = ListGenerator(txt=False, docx=False, headless=True, scrollPauseTime=1.0)
        
        It is up to you as the user to decide how you want to instantiate the ListGenerator object.
        If you choose the shorthand version, make sure you remember the default arguments!
        
        
        PRO TIP: whichever way you decide to instantiate your object, if you use custom settings, name your ListGenerator instance to reflect what you changed.
        E.g. For the previous case instead of naming your instance "LG", name it "headlessCsvLG" or "headless_csv_LG" - or something along those lines.
        
        For a ListGenerator object that creates a txt and csv file, but the program overwrites an existing txt file of the same name but does not overwrite an existing csv file of the same name, with all other arguments unmodified:
        LG = ListGenerator(txtWriteFormat='w')
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
