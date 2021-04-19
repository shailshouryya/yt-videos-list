from . import logic
def cli():
 '''
 Provides optional arguments for user increased visibility. Note that using some of the arguments may slow down run time and program may take slightly longer to execute.
 '''
 '''
 first argument should be channel/user name
 -c --channel_type sets channel_type to 'channel'
 -o --overwrite overwrite file if a file of the same name already exists in the output directory
 --version shows version number and exits
 --csv writes to csv file
 --txt writes to txt file
 --markdown writes to word dox (not yet available)
 --driver=Firefox sets selenium driver type to Firefox
 --driver=Opera sets selenium driver type to Opera
 --driver=Safari sets selenium driver type to Safari
 --driver=Chrome sets selenium driver type to Chrome
 -v --verbose print every 10 videos written to file
 -i --invisible opens a headless instance of the selenium driver to run the program in the background
 -q --quiet suppresses program updates, only prints to stdout when scrolling is complete files are opened and closed, and any errors that may occur
 -h --help display information on usage and functionality
 -p --pause change pause time between scrolls, set to 0.8s by default
 -r --reverse reverse the indexing so oldest video starts at 1 and most recent video has highest index
 '''
 url = f'youtube.com/user/schafer5'
 file_name = None
 log_silently = False
 txt = True
 csv = True
 markdown = False
 reverse_chronological = False
 headless = False
 scroll_pause_time = 0.8
 driver = None
 return (url, file_name, log_silently, txt, csv, markdown, reverse_chronological, headless, scroll_pause_time, driver)
def create_list_for():
 _execution_type = 'script'
 cli_settings = cli()
 logic.execute(*cli_settings, _execution_type)
