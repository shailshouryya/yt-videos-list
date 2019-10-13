class Common:
    '''
    This class contains messages that are common to both the pyYT_videos_list and execute modules.
    '''
    noVideosFound = 'No videos were found for the channel you provided. Are you sure you typed in the channel name correctly?\n'
    
    noNewVideosFound = 'No new videos were found since the last scroll. Waiting another 0.6 seconds to see if more videos can be loaded....'
    
    invalidResponse = 'The response you entered was invalid.'
    
    @staticmethod
    def fileAlreadyExistsWarning(filename):
        print (f'\nWARNING! A file with the name {filename} already exists in the current directory.')

    @staticmethod
    def fileAlreadyExistsPrompt(filename):
        print (f'If you wish to proceed and overwrite {filename}, type "proceed", otherwise move the file to a different directory on your computer before typing "continue"\n')
        print (f'If you wish to skip the creation of {filename}, type "skip"')

class ModuleMessage(Common):

    runInHeadless = '\nAdvanced usage: you can run this program in headless mode with the optional "headless" parameter set to True to speed up execution slightly:'
    
    runInHeadlessExample = "    LG = ListGenerator(headless=True)\n\n\n"
    
    checkChannelType = 'If you did type the name in correctly, perhaps the channelType is set incorrectly. Try setting channelType to "channel" in the generate_list() method call if you set channelType to "user" for this run, or try running the method with channelType set to "user" if you ran this method with channelType set to "channel" for this run\n'
    
    fileAlreadyExists = 'This error indicates that a file of this name already exists in the current directory. If you want to overwrite this file, run the generate_list method again with the optional parameter "writeFormat" set to "w"'
    
    fileAlreadyExistsRerunUsage = 'Example usage:\n LG.generate_list(writeFormat="w")\n'
    
class ScriptMessage(Common):
    inputMessage = "What is the name of the YouTube channel you want to generate the list for?" + "\n\n" + "If you're unsure, click on the channel and look at the URL." + "\n" + "It should be in the format:" + "\n" + "https://www.youtube.com/user/YourChannelName" + "\n" + "OR" + "\n" + "https://www.youtube.com/channel/YourChannelName" + "\n\n" + "Substitute what you see for YourChannelName and type it in below (NOTE: if your url looks like the second option, you need to run this script with the -c or --channel flag):\n"
    
    checkChannelType = 'If you did type the name in correctly, perhaps the channelType is set incorrectly. Try using the -c or --channelType flag for this script if you didn\'t do it when running this script, or try running the script without the -c or --channelType flag if you DID include that flag when running this script.'
