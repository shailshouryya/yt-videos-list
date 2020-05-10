from . import execute
from .notifications import Common, ModuleMessage


'''
version:              0.3.7
author:               Shail-Shouryya
development_status:   4 - Beta
intended_audience:    Developers, Hobbyists
license:              OSI Approved :: Apache License 2.0
ideal_python_version: Python 3.6+
source:               https://github.com/Shail-Shouryya/yt_videos_list
'''


__version__              = '0.3.7'
__author__               = 'Shail-Shouryya'
__development_status__   = '4 - Beta'
__intended_audience__    = 'Developers, Hobbyists'
__license__              =  'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__               = 'https://github.com/Shail-Shouryya/yt_videos_list'


class ListCreator:
    def __init__(self, txt=True, txt_write_format='x', csv=True, csv_write_format='x', docx=False, docx_write_format='x', chronological=False, headless=False, scroll_pause_time=0.8, driver=None):
        '''
        The ListCreator class creates a ListCreator instance with no required arguments.
        Example usage:
            lc = ListCreator()

        ###########################################################
        OPTIONAL: Specify the settings you want to use by substituing the desired values for the default arguments.
        An overview is given directly below this, but for a full working example scroll to the bottom.

        Options for the `driver` argument are
          * Firefox (default)
          * Opera
          * Safari
          * Chrome
          * Brave
            -> driver='firefox'
            -> driver='opera'
            -> driver='safari'
            -> driver='chrome'
            -> driver='brave'

        Options for the file type arguments (`csv`, `txt`) are
          * True (default) - create a file for the specified type
          * False - does NOT create a file for the specified type
             -> txt=True  (default) OR txt=False
             -> csv=True  (default) OR csv=False

        Options for the write format arguments (`csv_write_format`, `txt_write_format`) are
          * 'x' (default) - does NOT overwrite an existing file with the same name
          * 'w'           - does overwrite an existing file with the same name
          NOTE: if you specify the file type argument to be False, you don't need to touch this - the program will automatically skip this step.
             -> txt_write_format='x'  (default) OR txt_write_format='w'
             -> csv_write_format='x'  (default) OR csv_write_format='w'

        Options for the `chronological` argument are
          * False (default) - write the files in order from most recent video to the oldest video
          * True            - write the files in order from oldest video to the most recent video
             -> chronological=False (default) OR chronological=True

        Options for the `headless` argument are
          * False (default) - run the driver with an open Selenium instance for viewing
          * True            - run the driver without an open Selenium instance for viewing (runs in "invisible" mode)
             -> headless=False (default) OR headless=True

        Options for the `scroll_pause_time argument` are any float values greater than 0 (defaults to 0.8)
          * The value you provide will be how long (in seconds) the program waits before trying to scroll the videos list page down for the channel you want to scrape.
          * For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
             -> scroll_pause_time=0.8 (default)
          * CAUTION: reducing this value too much will result in the program not capturing all the videos, so be careful! Experiment :)


        WORKING EXAMPLES:
        ###########################################################
        For a ListCreator object that creates a csv file but not a txt file in chronological order in headless mode with a 1 second pause between scrolls:
        lc = ListCreator(txt=True, txt_write_format='x', csv=False, csv_write_format=0, chronological=True, headless=True, scroll_pause_time=1.0)
        ###########################################################

        ###########################################################
        The same could also be done by specifying only the arguments that change from the default, but notice how this is less explicit and can become confusing if you forget what the default arguments are:
        lc = ListCreator(txt=False, headless=True, scroll_pause_time=1.0)
        ###########################################################

        -----------------------------------------------------------
        It is up to you as the user to decide how you want to instantiate the ListCreator object.
        If you choose the shorthand version, make sure you remember the default arguments!
        -----------------------------------------------------------
        PRO TIP: whichever way you decide to instantiate your object, if you use custom settings, name your ListCreator instance to reflect what you changed.
        E.g. For the previous case instead of naming your instance "lc", name it "headlessCsvlc" or "headless_csv_lc" - or something along those lines.
        -----------------------------------------------------------

        ###########################################################
        For a ListCreator object that creates a txt and csv file and overwrites an existing txt file of the same name but does not overwrite an existing csv file of the same name (with all other arguments unmodified):
        lc = ListCreator(txt_write_format='w')
        ###########################################################
        '''


        self.txt               = txt
        self.txt_write_format  = txt_write_format
        self.csv               = csv
        self.csv_write_format  = csv_write_format
        self.docx              = docx
        self.docx_write_format = docx_write_format
        self.chronological     = chronological
        self.headless          = headless
        self.scroll_pause_time = scroll_pause_time
        self.driver            = None if driver is None else driver.lower()


    def create_list_for(self, url=None, file_name=None, channel=None, channel_type=None):
        '''
        NOTE that the "channel" and "channel_type" arguments are now deprecated, and remain for legacy purposes.
        The create_list_for() method creates a list using the arguments specified during instantiation of the ListCreator object.
        You need to specify the url to the channel you want to scrape.
        You can also provide an optional file_name argument, but the file_name argument is not required.
        '''


        if url is not None:
            channel_info = url.split('youtube.com/')[1]
            channel_type = channel_info.split('/')[0]
            channel      = channel_info.split('/')[1]
        if channel is None or channel_type is None:
            raise TypeError(Common().missing_url + ModuleMessage().url_argument_usage)

        _execution_type = 'module'
        instance_attributes = (self.txt, self.txt_write_format, self.csv, self.csv_write_format, self.docx, self.docx_write_format, self.chronological, self.headless, self.scroll_pause_time, self.driver)

        execute.logic(channel, channel_type, file_name, *instance_attributes, _execution_type)
