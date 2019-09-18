# Automate a YouTube Channel Videos List Creation

## Overview
This repo is intended to provide a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that user's channel videos. The general format for this is `https://www.youtube.com/user/TheChannelYouWantToScrape/videos` OR  
`https://www.youtube.com/channel/TheChannelYouWantToScrape/videos`,  
with `TheChannelYouWantToScrape` replaced with the username of the channel.

## Quick Start
```
git clone git@github.com:Shail-Shouryya/yt_videos_list.git
cd yt_videos_list/src
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

To scrape the video titles along with the link to the video, you need to run the `generate_list(channelName, channelType)` method on the ListGenerator object you just created, substituting the type of channel for `channelType` argument and the name of the channel for the `channelName` argument.

`user` channelType (example uses sentdex):
```python
LG.generate_list('sentdex', 'user')
```
`channel` channelType (example uses Billie Eilish):
```python
LG.generate_list('UCiGm_E4ZwYSHV3bcW1pnSeQ', 'channel')
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

## Program Functionality
## Main Features
- [X] take url and scrape the video name and url for every video for that user  
- [X] create csv
- [ ] get date published (probably not possible without significantly increasing runtime, could get how long ago video was published, but that tends to be unspecific)

## Additional Features
- [ ] create web interface
  - [ ] input box for channel url
- [ ] ouput CSV with custom name
- [ ] generate static HTML page with video URLs
- [ ] update previously generated CSV with new videos uploaded since CSV generation
  - [ ] using some kind of delta sync
