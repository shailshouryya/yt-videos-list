# Automate creation of videos lists for YouTube channels
**TABLE OF CONTENTS**
<br>[Quick Start](./README.md#Quick-Start)
<br>[Running the package from the python interpreter](./README.md#Running-the-package-from-the-python-interpreter)
<br>[For more control](./README.md#For-more-control)
<br>[General Overview](./README.md#General-Overview)
<br>[Future Features](./README.md#Future-Features)
<br>[Technical Specifications](./README.md#Technical-Specifications)


## Quick Start
This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)) and as such requires Python 3.6+. If you have an older version of Python, you can download the Python 3.8.2 [macOS 64-bit installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg), [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe), [Windows x86 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe), or the [Gzipped source tarball](https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz) (most useful for Linux) and follow the instructions to set up Python for your machine.

It's recommend to install the latest version if you don't have existing projects that are dependent on a specific older version of Python, but if you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want. Once you do that, enter the following in your command line:
```shell
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U yt-videos-list
```

### Running the package from the python interpreter
```shell
python3
```
```python
from yt_videos_list import ListCreator
lc = ListCreator()

# "user" channel_type (example uses Corey Schafer):
lc.create_list_for(url='https://www.youtube.com/user/schafer5')

# "channel" channel_type (example uses freeCodeCamp) along with the optional file_name argument:
lc.create_list_for(url='https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ', file_name='freeCodeCamp_orgVideosList')

# see the new files that were just created:
import os
# MacOS and Linux users:
os.system('ls -lt | head')
# Windows users:
os.system('dir /O-D | find "VideosList"')

# for more information on using the module:
help(lc)
```
**NOTE**: You do need to have the Selenium driver installed to run this package - and the first time you run this package the automated downloader should install everything you need, but in case it doesn't refer to the link below and/or file an [issue here](https://github.com/Shail-Shouryya/yt_videos_list/issues). The Selenium drivers are all pretty similar but differ in subtle ways, so play around with them and see what's different:)
#### Copy paste the code block that's relevant for the OS of your machine for the Selenium driver(s) you want from **[here](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/extra/README.md)**
**NOTE** that you also need the corresponding browser installed to properly run the selenium driver.
- To download the most recent version of the browser, go to the page for:
  - [Firefox](https://www.mozilla.org/en-US/firefox/new/)
  - [Opera](https://www.opera.com/)
  - [Chrome](https://www.google.com/chrome/)

### Running the package from the CLI as a script using -m (coming in `yt-videos-list 2.0`!)
```shell
python3 -m yt_videos_list
```


## For more control
---
**NOTE** that you can also access all the information below in the `python3` interpreter by entering
<br>`from yt_videos_list import ListCreator`
<br>`help(ListCreator)`

---
```python
ListCreator(csv=True, csv_write_format='x', txt=True, txt_write_format='x',
              chronological=False,
              headless=False, scroll_pause_time=0.8, driver='Firefox')
```
There are a number of optional arguments you can specify during the instantiation of the ListCreator object. The preceding arguments are run by default, but in case you want more flexibility, you can specify the:

- `driver` argument:
  - Firefox (default)
  - Opera
  - Safari
  - Chrome
    - `driver='firefox'`
    - `driver='opera'`
    - `driver='safari'`
    - `driver='chrome'`
- `csv`, `txt` file type argument:
  - `True` (default) - create a file for the specified type
  - `False` - do not create a file for the specified type.
    - `txt=True`  (default) OR `txt=False`
    - `csv=True`  (default) OR `csv=False`
- `csv_write_format`, `txt_write_format` write format argument
  - `'x'` (default) - does not overwrite an existing file with the same name
  - `'w'` - if an existing file with the same name exists, it will be overwritten
  - NOTE: if you specify the file type argument to be False, you don't need to touch this - the program will automatically skip this step.
    - `txt_write_format='x'`  (default) OR `txt_write_format='w'`
    - `csv_write_format='x'`  (default) OR `csv_write_format='w'`
- `chronological` argument:
  - `False` (default) - write the files in order from most recent video to the oldest video
  - `True` - write the files in order from oldest video to the most recent video
    - `chronological=False` (default) OR `chronological=True`
- `headless` argument:
  - `False` (default) - run the driver with an open Selenium instance for viewing
  - `True` - run the driver in "invisible" mode.
    - `headless=False` (default) OR `headless=True`
- `scroll_pause_time` argument:
  - any float values greater than `0` (default `0.8`).
    - The value you provide will be how long the program waits before trying to scroll the videos list page down for the channel you want to scrape. For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
  - `scroll_pause_time=0.8` (default)
  - CAUTION: reducing this value too much will result in the program not capturing all the videos, so be careful! Experiment :)


## General Overview
This package is intended to provide a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that user's channel videos. There are two types of YouTube channels: one type is a `user` channel and the other is a `channel` channel.
- Examples of the `user` channel type:
  - Disney: https://www.youtube.com/user/disneysshows
  - sentdex: https://www.youtube.com/user/sentdex
  - Marvel: https://www.youtube.com/user/MARVEL
  - Apple: https://www.youtube.com/user/Apple
- Examples of the `channel` channel type:
  - Tasty: https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q
  - Billie Eilish: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ
  - Gordon Ramsay: https://www.youtube.com/channel/UCIEv3lZ_tNXHzL3ox-_uUGQ
  - PBS Space Time: https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g

To scrape the video titles along with the link to the video, you need to run the `lc.create_list_for(url)` method on the ListCreator object you just created with `lc = ListCreator()`. By default, the name of the file produced will be `channel`VideosList.ext where the `.ext` will be `.csv` or `.txt `, depending on the type of file(s) that you specified.


### [Future Features](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/extra/futureFeatures.md)


## Technical Specifications
Please see [/extra/technicalSpecifications.md](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/extra/technicalSpecifications.md)
