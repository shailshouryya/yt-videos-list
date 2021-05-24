'''
YouTube bot to make a YouTube videos list (including all video titles and
URLs uploaded by a channel) with end-to-end web scraping - no API tokens required.
🌟 Star this repo if you found it useful! 🌟
https://github.com/Shail-Shouryya/yt-videos-list
'''

from . import logic


__version__              = '0.5.8'
__author__               = 'Shail-Shouryya'
__email__                = 'yt.videos.list@gmail.com'
__development_status__   = '4 - Beta'
__intended_audience__    = 'Developers, Hobbyists'
__license__              = 'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__               = 'https://github.com/Shail-Shouryya/yt-videos-list/tree/main/python'


class ListCreator:
    '''
    The ListCreator class creates a ListCreator instance with no required arguments.
    Example usage:
        lc = ListCreator()


    #############################################################################################################

    If you ALREADY scraped a channel and the channel uploaded a new video, simply rerun this
    program on that channel and this package updates your files to include the newer video(s)!


    OPTIONAL: Specify the settings you want to use by substituing the desired values for the default arguments.
    An overview is given directly below this, but for a full working example scroll to the bottom.

    Options for the `driver` argument are
      * Firefox (default)
      * Opera
      * Safari (MacOS only)
      * Chrome
      * Brave
      * Edge (Windows only)
        -> driver='firefox'
        -> driver='opera'
        -> driver='safari'
        -> driver='chrome'
        -> driver='brave'
        -> driver='edge'

    Options for the `cookie_consent` argument are
      * `False` (default) - block all cookie options if prompted by YouTube (at consent.youtube.com)
      * `True`            - accept all cookie options if prompted by YouTube (also at consent.youtube.com)
          -> `cookie_consent=False` (default) OR `cookie_consent=True`

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
      * CAUTION: reducing this value too much will result in the program not capturing all the videos,
        so be careful! Experiment :)
      * The value you provide will be how long (in seconds) the program waits before
        trying to scroll the videos list page down for the channel you want to scrape.
      * For fast internet connections, you may want to reduce the value,
        and for slow connections you may want to increase the value.
          -> scroll_pause_time=0.8 (default)



    #####################################################################################################

    WORKING EXAMPLES:

    Minimalist (ListCreator object creates a csv, txt, and md file in reverse chronological order -
    meaning the most recently uploaded videos are at the top of the file):

    lc = ListCreator()


    Minimalist but with a different driver:
    -> lc = ListCreator(driver='firefox') # default, argument not required
    -> lc = ListCreator(driver='opera')
    -> lc = ListCreator(driver='safari')
    -> lc = ListCreator(driver='chrome')
    -> lc = ListCreator(driver='brave')
    -> lc = ListCreator(driver='edge')


    Minimalist in headless ("invisible") mode (NOTE: currently only supported by firefox and chrome):
    -> lc = ListCreator(headless=True)                    # runs firefox in headless mode
    -> lc = ListCreator(driver='chrome', headless=True)   # runs chrome  in headless mode


    Minimalist with reverse chronological order (ListCreator object creates a csv, txt, and md file with
    oldest videos at the top of the file instead of the most recently uploaded videos at the top):
    -> lc = ListCreator(reverse_chronological=False)

    -----------------------------------------------------------------------------------------------------

    Minimalist with longer pauses (useful for slow internet):
    -> lc - ListCreator(scroll_pause_time=1.2)

    Minimalist with shorter pauses (useful for fast internet):
    -> lc - ListCreator(scroll_pause_time=0.7)

    -----------------------------------------------------------------------------------------------------

    Only creating a csv file with everything else set to default:
    -> lc = ListCreator(txt=False, md=False)

    =====================================================
    | If you found this interesting or useful,          |
    | ** please consider STARRING this repo at **       |
    | https://github.com/Shail-Shouryya/yt-videos-list  |
    | so other people can more easily find and use this.|
    | Thank you!!                                       |
    =====================================================
    '''
    def __init__(self, txt=True, csv=True, md=True, reverse_chronological=True, headless=False, scroll_pause_time=0.8, driver=None, cookie_consent=False):
        '''
        Initializes an instance of ListCreator by setting the attributes of the instance to the provided arguments,
        and setting any attributes not provided as the default parameter value.
        '''
        self.txt                   = txt
        self.csv                   = csv
        self.markdown              = md
        self.reverse_chronological = reverse_chronological
        self.headless              = headless
        self.scroll_pause_time     = scroll_pause_time
        self.driver                = None if driver is None else driver.lower()
        self.cookie_consent        = cookie_consent


    def __repr__(self):
        '''
        Returns an unambiguous representation of the current instace that can be used to recreate the same exact object.
        This is useful for internal use and making developer debugging easier.
        '''
        return f'{self.__class__.__name__}(txt={self.txt}, csv={self.csv}, md={self.markdown}, reverse_chronological={self.reverse_chronological}, headless={self.headless}, scroll_pause_time={self.scroll_pause_time}, driver={self.driver}, cookie_consent={self.cookie_consent})'


    def __str__(self):
        '''
        Returns an easy to read representation of the current instance.
        This is useful for typical users to see the attributes of the current instance and is ideal for human consumption.
        '''
        return f'''{self.__class__.__name__}() object created with attributes
        txt                   = {self.txt}
        csv                   = {self.csv}
        md                    = {self.markdown}
        reverse_chronological = {self.reverse_chronological}
        headless              = {self.headless}
        scroll_pause_time     = {self.scroll_pause_time}
        driver                = {self.driver}
        self.cookie_consent   = {self.cookie_consent}

        To recreate object, use:
        {self.__class__.__name__}(txt={self.txt}, csv={self.csv}, md={self.markdown}, reverse_chronological={self.reverse_chronological}, headless={self.headless}, scroll_pause_time={self.scroll_pause_time}, driver={self.driver}, cookie_consent={self.cookie_consent})
        '''


    def create_list_for(self, url=None, log_silently=False, file_name=None):
        '''
        The create_list_for() method creates a list using the arguments specified during instantiation of the ListCreator object.
        You need to specify just the url to the channel you want to scrape.

        Set `log_silently` to `True` to mute program logging to the console. The program will log the prgram status and any
        program information to only the log file for the channel being scraped (this is useful when scraping multiple channels at
        once with multi-threading). By default, the program logs to both the log file for the channel being scraped AND the console.

        You can also provide an optional file_name argument, but this is NOT recommended -
        the program finds the name of the channel automatically and if you rename the file,
        the file won't be automatically updated if the channel uploads a new video and you run this on that channel
        UNLESS you provide the same **exact** name every time you rerun this.
        '''
        _execution_type     = 'module'
        instance_attributes = (self.txt, self.csv, self.markdown, self.reverse_chronological, self.headless, self.scroll_pause_time, self.driver, self.cookie_consent)
        return logic.execute(url, file_name, log_silently, *instance_attributes, _execution_type)
