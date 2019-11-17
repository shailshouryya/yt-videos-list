import execute
from output import Common, ModuleMessage, ScriptMessage

def cli():
    '''
    Provides optional arguments for user increased visibility. Note that using some of the arguments may slow down run time and program may take slightly longer to execute.
    '''
    '''

    first argument should be channel/user name
    -c --channelType sets channelType to "channel"
    -o --overwrite overwrite file if a file of the same name already exists in the output directory
    --version shows version number and exits
    --csv writes to csv file
    --txt writes to txt file
    --docx writes to word dox (not yet available)
    -v --verbose print every 10 videos written to file
    -i --invisible opens a headless instance of the selenium browser to run the program in the background
    -q --quiet suppresses program updates, only prints to stdout when scrolling is complete files are opened and closed, and any errors that may occur
    -h --help display information on usage and functionality
    -p --pause change pause time between scrolls, set to 0.8s by default
    -r --reverse reverse the indexing so oldest video starts at 1 and most recent video has highest index
    '''
    pass
    return (channel, channelType, fileName, txt, txtWriteFormat, csv, csvWriteFormat, docx, docxWriteFormat, chronological, headless, scrollPauseTime)

def generate_list():
    _executionType = 'script'
    cliSpecifications = cli()
    execute.run(*cliSpecifications, _executionType)
