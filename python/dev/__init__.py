from .              import execute
from .notifications import Common, ModuleMessage


'''
version:              0.4.7
author:               Shail-Shouryya
email:                yt.videos.list@gmail.com
development_status:   4 - Beta
intended_audience:    Developers, Hobbyists
license:              OSI Approved :: Apache License 2.0
ideal_python_version: Python 3.6+
source:               https://github.com/Shail-Shouryya/yt_videos_list
'''


__version__              = '0.4.7'
__author__               = 'Shail-Shouryya'
__email__                = 'yt.videos.list@gmail.com'
__development_status__   = '4 - Beta'
__intended_audience__    = 'Developers, Hobbyists'
__license__              = 'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__               = 'https://github.com/Shail-Shouryya/yt_videos_list'


class ListCreator:
    def __init__(self, txt=True, csv=True, md=True, reverse_chronological=True, headless=False, scroll_pause_time=0.8, driver=None):
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
          * Edge (Windows only)
            -> driver='firefox'
            -> driver='opera'
            -> driver='safari'
            -> driver='chrome'
            -> driver='brave'
            -> driver='edge'

        Options for the file type arguments (`csv`, `txt`, `md`) are
          * True (default) - create a file for the specified type
          * False - does NOT create a file for the specified type
             -> txt=True  (default) OR txt=False
             -> csv=True  (default) OR csv=False
             ->  md=True  (default) OR  md=False

        Options for the `reverse_chronological` argument are
          * True (default) - write the files in order from most recent video to the oldest video
          * False          - write the files in order from oldest video to the most recent video
             -> reverse_chronological=True (default) OR reverse_chronological=False

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
        Minimalist (ListCreator object creates a csv, txt, and md file in reverse chronological order - meaning the most recently uploaded videos are at the top of the file):
        lc = ListCreator()


        Minimalist with reverse chronological order (ListCreator object creates a csv, txt, and md file with oldest videos at the top of the file instead of the most recently uploaded videos at the top)
        lc = ListCreator(reverse_chronological=False)
        ###########################################################


        ###########################################################
        Minimalist with greater pauses (useful for slow internet):
        lc = ListCreator(scroll_pause_time=1.2)

        Minimalist with shorter pauses (useful for fast internet):
        lc = ListCreator(scroll_pause_time=0.7)
        ###########################################################


        ###########################################################
        Only creating a csv file with everything else set to default:
        lc = ListCreator(txt=False, md=False)
        ###########################################################


        -----------------------------------------------------------
        SWE PRO TIP: however you decide to instantiate your object, if you use custom settings, name your ListCreator instance to reflect what you changed.
        E.g. For the last case, instead of naming your instance "lc", name it "CsvOnlyLc" or "csv_only_lc" - or something along those lines.
        -----------------------------------------------------------

        ===========================================================
        If you found this interesting or useful, ** please consider STARRING this repo at https://github.com/Shail-Shouryya/yt_videos_list ** so other people can more easily find and use this. Thank you!!
        ===========================================================
        '''


        self.txt                   = txt
        self.csv                   = csv
        self.markdown              = md
        self.reverse_chronological = reverse_chronological
        self.headless              = headless
        self.scroll_pause_time     = scroll_pause_time
        self.driver                = None if driver is None else driver.lower()


    def __repr__(self):
        return f'{self.__class__.__name__}(txt={self.txt}, csv={self.csv}, md={self.markdown}, reverse_chronological={self.reverse_chronological}, headless={self.headless}, scroll_pause_time={self.scroll_pause_time}, driver={self.driver})'


    def __str__(self):
        return f'''{self.__class__.__name__}() object created with attributes
        txt                   = {self.txt}
        csv                   = {self.csv}
        md                    = {self.markdown}
        reverse_chronological = {self.reverse_chronological}
        headless              = {self.headless}
        scroll_pause_time     = {self.scroll_pause_time}
        driver                = {self.driver}

        To recreate object, use:
        {self.__class__.__name__}(txt={self.txt}, csv={self.csv}, md={self.markdown}, reverse_chronological={self.reverse_chronological}, headless={self.headless}, scroll_pause_time={self.scroll_pause_time}, driver={self.driver}
        '''


    def create_list_for(self, url=None, file_name=None, channel=None, channel_type=None):
        '''
        The create_list_for() method creates a list using the arguments specified during instantiation of the ListCreator object.
        You need to specify just the url to the channel you want to scrape.

        You can also provide an optional file_name argument, but this is NOT recommended - the program finds the name of the channel automatically and if you rename the file the file won't be automatically updated if the channel uploads a new video and you run this on that channel UNLESS you provide the same **exact** name every time you rerun this.
        NOTE that the "channel" and "channel_type" arguments are now deprecated, and remain for legacy purposes.
        '''


        if url is not None:
            channel_info = url.split('youtube.com/')[1]
            channel_type = channel_info.split('/')[0]
            channel      = channel_info.split('/')[1]
        if channel is None or channel_type is None:
            raise RuntimeError(Common().missing_url + ModuleMessage().url_argument_usage)

        _execution_type = 'module'
        instance_attributes = (self.txt, self.csv, self.markdown, self.reverse_chronological, self.headless, self.scroll_pause_time, self.driver)

        execute.logic(channel, channel_type, file_name, *instance_attributes, _execution_type)
