from . import execute

'''
version: 0.2.15
author: Shail-Shouryya
development_status: 4 - Beta
intended_audience: Developers, Hobbyists
license:  OSI Approved :: Apache License 2.0
ideal_python_version: Python 3.7
source: https://github.com/Shail-Shouryya/yt_videos_list
'''
__version__ = '0.2.16'
__author__ = 'Shail-Shouryya'
__development_status__ = '4 - Beta'
__intended_audience__ = 'Developers, Hobbyists'
__license__ =  'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.7'
__source__ = 'https://github.com/Shail-Shouryya/yt_videos_list'

class ListGenerator:
    def __init__(self, txt=True, txtWriteFormat='x', csv=True, csvWriteFormat='x', docx=False, docxWriteFormat='x', chronological=False, headless=False, scrollPauseTime=0.8, driver=None):
        '''
        The ListGenerator class creates a list generator instance with no required arguments.
        Example usage:
            LG = ListGenerator()

        ###########################################################
        OPTIONAL: specify the settings you want to use by substituing the desired values for the default arguments.
        An overview is given directly below this, but for a full working example scroll to the bottom.

        Options for the `driver` argument are
          * Firefox (default)
          * Chrome
          * Opera
          * Safari

        Options for the file type arguments (`csv`, `txt`) are
          * True (default) - create a file for the specified type
          * False - does NOT create a file for the specified type.
             -> txt=True  (default) OR txt=False
             -> csv=True  (default) OR csv=False

        Options for the write format arguments (`csvWriteFormat`, `txtWriteFormat`) are
          * 'x' (default) - does NOT overwrite an existing file with the same name
          * 'w'           - does overwrite an existing file with the same name
          NOTE: if you specify the file type argument to be False, you don't need to touch this - the program will automatically skip this step.
             -> txtWriteFormat='x'  (default) OR txtWriteFormat='w'
             -> csvWriteFormat='x'  (default) OR csvWriteFormat='w'

        Options for the `chronological` argument are
          * False (default) - write the files in order from most recent video to the oldest video
          * True            - write the files in order from oldest video to the most recent video
             -> chronological=False (default) OR chronological=True

        Options for the `headless` argument are
          * False (default) - run the driver with an open Selenium instance for viewing
          * True            - run the driver without an open Selenium instance for viewing (runs in "invisible" mode)
             -> headless=False (default) OR headless=True

        Options for the `scrollPauseTime argument` are any float values greater than 0 (defaults to 0.8).
          * The value you provide will be how long (in seconds) the program waits before trying to scroll the videos list page down for the channel you want to scrape.
          * For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
             -> scrollPauseTime=0.8 (default)
          * CAUTION: reducing this value too much will result in the programming not capturing all the videos, so be careful! Experiment :)


        WORKING EXAMPLES:
        ###########################################################
        For a ListGenerator object that creates a csv file but not a txt file in chronological order in headless mode with a 1 second pause between scrolls:
        LG = ListGenerator(txt=True, txtWriteFormat='x', csv=False, csvWriteFormat=0, chronological=True, headless=True, scrollPauseTime=1.0)
        ###########################################################

        ###########################################################
        The same could also be done by specifying only the arguments that change from the default, but notice how this is less explicit and can become confusing if you forget what the default arguments are:
        LG = ListGenerator(txt=False, headless=True, scrollPauseTime=1.0)
        ###########################################################

        -----------------------------------------------------------
        It is up to you as the user to decide how you want to instantiate the ListGenerator object.
        If you choose the shorthand version, make sure you remember the default arguments!
        -----------------------------------------------------------
        PRO TIP: whichever way you decide to instantiate your object, if you use custom settings, name your ListGenerator instance to reflect what you changed.
        E.g. For the previous case instead of naming your instance "LG", name it "headlessCsvLG" or "headless_csv_LG" - or something along those lines.
        -----------------------------------------------------------

        ###########################################################
        For a ListGenerator object that creates a txt and csv file and overwrites an existing txt file of the same name but does not overwrite an existing csv file of the same name (with all other arguments unmodified):
        LG = ListGenerator(txtWriteFormat='w')
        ###########################################################
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
        self.driver = None if driver is None else driver.lower()

    def generate_list(self, channel, channelType, fileName=None):
        '''
        The generate_list method creates a list using the arguments specified during the instantiation of ListGenerator object.
        You need to specify the channel and channelType.
        You can also provide an optional fileName argument, but the fileName argument is not required.
        '''
        _executionType='module'
        execute.logic(channel, channelType, fileName, self.txt, self.txtWriteFormat, self.csv, self.csvWriteFormat, self.docx, self.docxWriteFormat, self.chronological, self.headless, self.scrollPauseTime, self.driver, _executionType)
