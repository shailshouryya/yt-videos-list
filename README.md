# Automate a YouTube Channel Videos List Creation

## Overview
This repo is intended to provide a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that user's channel videos. The general format for this is `https://www.youtube.com/user/TheChannelYouWantToScrape/videos` OR  
`https://www.youtube.com/channel/TheChannelYouWantToScrape/videos`,  
with `TheChannelYouWantToScrape` replaced with the username of the channel.

## Quick Start
```
git clone git@github.com:Shail-Shouryya/yt_videos_list.git
cd yt_videos_list
```
### Running as a module
```
python3
```
```python
from yt_videos_list import ListGenerator
LG = ListGenerator()
```
There are two types of YouTube channels: one type is a "user" channel and the other is a `channel` channel.
* The url for a `user` channel consists of `youtube.com` followed by `user` followed by the name. For example:
  * sentdex: https://www.youtube.com/user/sentdex
  * Disney: https://www.youtube.com/user/disneysshows
  * Marvel: https://www.youtube.com/user/MARVEL
  * Apple: https://www.youtube.com/user/Apple
* The url for a "channel" channel consists of `youtube.com` followed by `channel` followed by a string of rather unpredictable characters. For example:
  * Billie Eilish's channel url looks like: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ

To scrape the video titles along with the link to the video, you need to run the `generate_list(channelName, channelType)` method on the ListGenerator object you just created, substituting the type of channel for `channelType` argument and the name of the channel for the `channelName` argument. By default, the name of the file produced will be `channelName`VideosList.ext where the `.ext` will be `.csv` or `.txt ` depending on the type of file(s) that you specified. 

`user` channelType (example uses sentdex):
```python
LG.generate_list('sentdex', 'user')
```
`channel` channelType (example uses Billie Eilish):
```python
LG.generate_list('UCiGm_E4ZwYSHV3bcW1pnSeQ', 'channel')
```
In order to get a more descriptive file name, add how you would like to describe the file for the optional argument `fileName`:
```python
LG.generate_list('UCiGm_E4ZwYSHV3bcW1pnSeQ', 'channel', 'BillieEilish')
```
### For more control:
There are a number of optional arguments you can specify during the instantiation of the ListGenerator object. The following arguments are run by default, but in case you want more flexibility, you can specify:
  * The type of file you want: `txt` and `csv` currently available
  * If you want to override an already existing file with the same name: the default setting of `'x'` shows you a warning and asks you if you want to overwrite the file or skip it. If you know you want to overwrite it, set the `WriteFormat` of the file type to `'w'`
  * If you want the list of videos to be sorted by oldest to most recent (default setting set to `True`), otherwise set `chronological=False` to sort the videos by most recent to oldest
  * If you want to see the automated instance of the browser while it runs. Headless is set to `False` by default to give you an idea of what is going on and make it easier to debug in case something happens that you weren't expecting, but if you don't want to see it, set `headless=True`
  * How long you want to wait before scrolling down. The default setting of `scrollPauseTime=0.7` works well with an average internet connection, but if your internet connection is much slower you may want to increase `scrollPauseTime` to a value larger than 0.7, and if your internet connection is very fast you can decrease the scrollPauseTime to a value that is smaller than 0.7
```python
ListGenerator(csv=True, csvWriteFormat='x', txt=True, txtWriteFormat='x', docx=False, docxWriteFormat='x', chronological=True, headless=False, scrollPauseTime=0.7,)
```

### Running as a script (coming soon!)
Enter the directory in which the pyYT_videos_list.py and execute.py exist (they should both be in the same directory to avoid refernce issues), and run the following command from your command line  
```
python3 yt_videos_list
```  
You should see the following:  
```
What is the name of the YouTube channel you want to generate the list for?
If you're unsure, click on the channel and look at the URL.
It should be in the format:
https://www.youtube.com/user/YourChannelName
OR
https://www.youtube.com/channel/YourChannelName
Substitute what you see for YourChannelName and type it in below:
```
Enter the name of the channel or user that you wish to scrape, and the program will do the rest for you!
