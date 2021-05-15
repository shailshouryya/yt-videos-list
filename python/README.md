# Python Quick Start

#### See the [releases](https://github.com/Shail-Shouryya/yt-videos-list/releases) page to see new additions/modifications for each release!

<details>
  <summary><b>See sister <a href="https://github.com/Shail-Shouryya/YouTube-Channels">YouTube-Channels</a> repository for a list of interesting channels!</b></summary></h3>

- The `YouTube-Channels` sister repository is a separate repository that uses this package to create a list of videos uploaded by every channel supported by the repository.
- The sister repository will update the lists of videos once a week.
- NOTE: In order to minimize the size of the sister repo, the repo contains the list of videos in ONLY the `csv` format, and not in `txt` or `md` format.
</details>

<p align="center">
  <a href="https://github.com/Shail-Shouryya/yt-videos-list/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Shail-Shouryya/yt-videos-list?color=yellow&labelColor=black"></a>
  <a href="https://docs.python.org/3/index.html">    <img src="https://img.shields.io/badge/python-3.6%2B-blue?labelColor=black"/></a>
  <a href="https://www.python.org/dev/peps/pep-0008"><img src="https://img.shields.io/badge/code%20style-PEP8-yellow.svg?labelColor=black"/></a>
  <a href="https://github.com/Shail-Shouryya/yt-videos-list/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Shail-Shouryya/yt-videos-list?color=blue&labelColor=black"></a>
  <a href="https://github.com/Shail-Shouryya/yt-videos-list/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/Shail-Shouryya/yt-videos-list?color=yellow&labelColor=black"></a>
  <br>
  <a href="https://badge.fury.io/py/yt-videos-list"><img src="https://badge.fury.io/py/yt-videos-list.svg" alt="PyPI version" height="20"></a>
  <br>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/yt-videos-list?labelColor=black&label=PyPI%20-%20Wheel"></a>
  <a href="https://pypi.org/project/yt-videos-list/#files/"><img alt="PyPI - Format" src="https://img.shields.io/pypi/format/yt-videos-list?labelColor=black&label=PyPI%20-%20Format"></a>
  <a href="https://pypi.org/project/yt-videos-list/#history/"><img alt="PyPI - Status" src="https://img.shields.io/pypi/status/yt-videos-list?labelColor=black&label=PyPI%20-%20Status"></a>
  <br>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/yt-videos-list?labelColor=black&label=PyPI%20-%20Implementation"></a>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/yt-videos-list?labelColor=black&label=PyPI%20-%20Python%20Version"></a>
  <br>
  <a href="https://codebeat.co/projects/github-com-shail-shouryya-yt_videos_list-master"><img src="https://codebeat.co/badges/46b103ed-da79-4893-96af-ce95c9149532" alt="codebeat badge"/></a>
</p>

<details>
  <summary><b>Python 3.6+ setup (required if not already installed)</b></summary>

This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)), and so requires Python 3.6+.

If you have an older version of Python, you can download Python 3.9.1 (follow links below) and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.
- [macOS 64-bit installer](https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg)
- [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)
- [Windows x86 executable installer](https://www.python.org/ftp/python/3.9.1/python-3.9.1.exe)
- [Gzipped source tarball](https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz) (most useful for Linux)
</details>

<details>
  <summary><b>Permissions for first run</b></summary>

  This is required to make sure you can download and install the required Selenium binary dependencies.
  <details>
  <summary><b>On Windows: make sure you open <code>Command Prompt</code> or <code>Powershell</code> (both work) in "Run as Administrator" mode</b></summary>

  - shortcut: <kbd>⊞ Win</kbd> + <kbd>X</kbd> + <kbd>A</kbd>
  </details>
  <details>
    <summary><b>On Unix based machines (MacOS, Linux): make sure you have read and write access to <code>/usr/local/bin/</code></b></summary>

  - if you're not sure, open terminal and run `sudo chown $USER /usr/local/bin/`
  </details>
<br>
</details>

<details>
  <summary><b>Installing the package</b></summary>

After you install Python 3.6+ and ensure you have the required permissions as needed, enter the following in your command line:
```shell
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U yt-videos-list     # MacOS/Linux
pip  install -U yt-videos-list     # Windows


# if that doesn't work:

python3 -m pip install -U yt-videos-list     # MacOS/Linux
python  -m pip install -U yt-videos-list     # Windows
```
</details>

<details>
  <summary><b>If you're on Windows: make sure you <i>always</i> open <code>Command Prompt</code> or <code>Powershell</code> (both work) in "Run as Administrator" mode!</b></summary>

  - shortcut: <kbd>⊞ Win</kbd> + <kbd>X</kbd> + <kbd>A</kbd>
  - this allows `yt_videos_list` to update selenium webdriver binaries to be compatible with newer browser versions as browsers are updated (e.g. your Firefox browser updates from version 77 to version 82)
    - to see the commands being run, see the `yt_videos_list/docs/dependencies.json` file
</details>

<details>
  <summary><b>Running the package from the python interpreter</b></summary>

```shell
python3     # MacOS/Linux
python      # Windows
```
```python
from yt_videos_list import ListCreator


my_driver = 'firefox' # SUBSTITUTE DRIVER YOU WANT (options below)
lc = ListCreator(driver=my_driver, scroll_pause_time=0.8)


lc.create_list_for(url='https://www.youtube.com/user/schafer5')
lc.create_list_for(url='https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ', log_silently=True)
# Set `log_silently` to `True` to mute program logging to the console.
# The program will log the prgram status and any program information
# to only the log file for the channel being scraped
# (this is useful when scraping multiple channels at once with multi-threading).
# By default, the program logs to both the log file for the channel being scraped AND the console.


# see the new files that were just created:
import os
os.system('ls -lt | head')                      # MacOS/Linux
os.system('dir /O-D | find "_videos_list"')     # Windows

# for more information on using the module:
help(lc)
```
- `driver` options include:
  - `'firefox'`
  - `'opera'`
  - `'safari'` (MacOS only)
  - `'chrome'`
  - `'brave'`
  - `'edge'` (Windows only!)
- increase `scroll_pause_time` for laggy internet and decrease `scroll_pause_time` for fast internet
</details>

#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!

<details>
  <summary><b>Scraping multiple channels from a file simultaneously with multi-threading</b></summary>

Add the url to every channel you want to extract information from in a `txt` file with every url placed on a new line.

<details>
  <summary><b>e.g. <code>channels.txt</code></b></summary>

```
https://www.youtube.com/channel/UCSHZKyawb77ixDdsGog4iWA
https://www.youtube.com/c/WorldScienceFestival/playlists
https://www.youtube.com/c/RSAConference/videos
https://www.youtube.com/channel/UCtC8aQzdEHAmuw8YvtH1CcQ/videos
https://www.youtube.com/channel/UCQSrdt0-Iu8qVEiJyzhrfdQ/videos
https://www.youtube.com/user/TEDxTalks/videos
https://www.youtube.com/user/TEDxYouth
https://www.youtube.com/user/TEDPrizeChannel/videos
https://www.youtube.com/user/TEDInstitute/videos
https://www.youtube.com/user/TEDPartners/channels
https://www.youtube.com/c/TheVerge/channels
https://www.youtube.com/c/mitocw/channels
https://www.youtube.com/c/stanford/channels
https://www.youtube.com/c/khanacademy/channels
https://www.youtube.com/c/TEDEdStudentTalks/channels
https://www.youtube.com/c/TED/channels
https://www.youtube.com/c/TEDFellow/videos
https://www.youtube.com/c/tedededucatortalks/videos
https://www.youtube.com/c/TEDTranslators/videos
https://www.youtube.com/c/TEDEspanol/videos
https://www.youtube.com/teded/featured
https://www.youtube.com/c/IBMSecurity/channels
https://www.youtube.com/user/symantec/channels
https://www.youtube.com/c/QuantamagazineOrgNews/videos
https://www.youtube.com/c/Splunkofficial/channels
```
</details>
Enter the python interpreter:

```
python3     # MacOS/Linux
python      # Windows
```
```python
import time
import threading   # python standard library built-in package, no download necessary
from yt_videos_list import ListCreator

my_driver = 'firefox'
lc = ListCreator(driver=my_driver, scroll_pause_time=0.8)

number_of_threads         = 4 # CHANGE TO DESIRED NUMBER OF CONCURRENT THREADS
path_to_channel_urls_file = 'channels.txt'

with open(path_to_channel_urls_file, 'r', encoding='utf-8') as file:
    for url in file:
        while threading.active_count() == number_of_threads + 1: # add 1 since main thread counts as a thread
            time.sleep(5) # wait 5 seconds before checking to see if a previously running thread completed
        thread = threading.Thread(target=lc.create_list_for, args=(url, True))
        thread.start()
    thread.join() # After we iterate through every line in the file, we call the join() method
    # on the last thread so python doesn't exit the multi-threaded environment pre-maturely
    # This is ESSENTIAL, otherwise threading might stop randomly on the last channel in the
    # channels.txt file before the program finishes writing all the channel information to the files!
```
- See [Thread about multi-threading with yt_videos_list](https://github.com/Shail-Shouryya/yt-videos-list/discussions/11) for more information!

</details>

<details>
  <summary><b>Explicitly downloading all Selenium dependencies</b></summary>

Ideal if you use Selenium for other projects 😎
- Make sure you already have the `yt-videos-list` package installed (follow directions above for getting set up), then run the following:
```shell
pip3 install -U yt-videos-list # MacOS/Linux: ensure latest package
python3                        # MacOS/Linux: enter python interpreter
pip install -U yt-videos-list  # Windows:     ensure latest package
python                         # Windows:     enter python interpreter
```
```python
from yt_videos_list.download import selenium_webdriver_dependencies
selenium_webdriver_dependencies.download_all()
```
That's all! 🤓
</details>

<details>
  <summary><b>More API information</b></summary>

---
**NOTE** that you can also access all the information below from the Python interpreter by entering
```python
import yt_videos_list
help(yt_videos_list)
```

---
```python
# default options for the ListCreator object

ListCreator(
  txt=True,
  csv=True,
  md=True,
  reverse_chronological=True,
  headless=False,
  scroll_pause_time=0.8,
  driver='firefox'
  )
```
There are a number of optional arguments you can specify during the instantiation of the ListCreator object. The preceding arguments are run by default, but in case you want more flexibility, you can specify the:
- `driver` argument:
  - Firefox (default)
  - Opera
  - Safari (MacOS only)
  - Chrome
  - Brave
  - Edge (Windows only)
    - `driver='firefox'`
    - `driver='opera'`
    - `driver='safari'`
    - `driver='chrome'`
    - `driver='brave'`
    - `driver='edge'`
- `cookie_consent` argument:
  - `False` (default) - block all cookie options if prompted by YouTube (at consent.youtube.com)
  - `True` - accept all cookie options if prompted by YouTube (also at consent.youtube.com)
    - `cookie_consent=False` (default) OR `cookie_consent=True`
-  `txt`, `csv`, `md` file type argument:
  - `True` (default) - create a file for the specified type
  - `False` - do not create a file for the specified type.
    - `txt=True`  (default) OR `txt=False`
    - `csv=True`  (default) OR `csv=False`
    - ` md=True`  (default) OR ` md=False`
- `reverse_chronological` argument:
  - `True` (default) - write the files in order from most recent video to the oldest video
  - `False` - write the files in order from oldest video to the most recent video
    - `reverse_chronological=True` (default) OR `reverse_chronological=False`
- `headless` argument:
  - `False` (default) - run the driver with an open Selenium instance for viewing
  - `True` - run the driver in "invisible" mode.
    - `headless=False` (default) OR `headless=True`
- `scroll_pause_time` argument:
  - any float values greater than `0` (default `0.8`).
    - The value you provide will be how long the program waits before trying to scroll the videos list page down for the channel you want to scrape. For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
  - `scroll_pause_time=0.8` (default)
  - CAUTION: reducing this value too much will result in the program not capturing all the videos, so be careful! Experiment :)
</details>

<details>
<summary><b>Cloning and running locally</b></summary>

To clone the repository and install the most updated version of the package that may not yet be available on the latest release through [PyPI](pypi.org/project/yt-videos-list/), run:
```
git clone https://github.com/Shail-Shouryya/yt-videos-list.git

cd yt_videos_list/python # MacOS/Linux
pip3 install .           # MacOS/Linux
# if that doesn't work:
python3 -m pip install . # MacOS/Linux

cd yt_videos_list\python # Windows
pip install .            # Windows
# if that doesn't work:
python -m pip install .  # Windows
```
To make your own changes to the `yt_videos_list` python package and run the changes locally:
```
# make changes to the codebase in the
# ===> /dev <=== directory
python3 minifier.py           # MacOS/Linux
pip3 install .                # MacOS/Linux

python minifier.py            # Windows
pip install .                 # Windows
```
NOTE that the changes you make to the codebase SHOULD BE MADE in the `yt_videos_list/python/dev` directory!!
  - the code in the `yt_videos_list/python/yt-videos-list` directory is minified with
    - leading indents stipped to the minimum (1 space for each nested scope)
    - whitespace for padding (e.g. extra spaces to align variable assignments) stripped
    - comments stripped
  - as a result, the code in the `yt_videos_list/python/yt-videos-list` directory is NOT human readable, and the `yt_videos_list/python/dev` directory should be used for development instead!
    - the `minifier.py` module performs all the code preprocessing and packages the code from `yt_videos_list/python/dev` into the final version seen in the `yt_videos_list/python/yt-videos-list` directory
    - so running `minifier.py` ***before*** installing the local package with `pip install .` (Windows) or `pip3 install .` is essential!
</details>

<details>
<summary><b>Running tests</b></summary>

The tests use the custom `ThreadWithResult` subclass of `threading.Thread` provided by the `save-thread-result` package, so make sure you install that module using
```
pip3 install -U save-thread-result     # MacOS/Linux
pip  install -U save-thread-result     # Windows

# if that doesn't work:

python3 -m pip install -U save-thread-result     # MacOS/Linux
python  -m pip install -U save-thread-result     # Windows
```

Then, make sure you're in the `yt_videos_list/python` directory, then run:
```
tests\run_tests.bat     # Windows
####       Any shell on   MacOS/Linux
bash tests/run_tests.sh # this works
csh  tests/run_tests.sh # this works
dash tests/run_tests.sh # this works
ksh  tests/run_tests.sh # this also works
tcsh tests/run_tests.sh # this works too
zsh  tests/run_tests.sh # this works as well
# you can try other shells and
# they should work too, since
# there's no special syntax in
# the run_tests.sh file
```
</details>

<details>
<summary><b>Stargazers Over Time</b></summary>

[![Stargazers over time](https://starchart.cc/Shail-Shouryya/yt-videos-list.svg)](https://starchart.cc/Shail-Shouryya/yt-videos-list)
</details>

<details>
  <summary><b>Usage Statistics</b></summary>

- [PePy](https://pepy.tech/project/yt-videos-list)
- [PyPi Stats](https://pypistats.org/packages/yt-videos-list)
</details>
<p>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Daily Downloads" src="https://img.shields.io/pypi/dd/yt-videos-list?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29" width="275"></a>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Weekly Downloads" src="https://img.shields.io/pypi/dw/yt-videos-list?labelColor=black&color=yellow&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Monthly Downloads" src="https://img.shields.io/pypi/dm/yt-videos-list?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <br>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Weekly Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=week&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads/week%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Monthly Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=month&units=international_system&left_color=black&right_color=blue&left_text=PePY%20Downloads/month%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Total Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=total&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads%20Total%20%28includes%20mirrors%29" width="275"></a>
  <br>
</p>

#### [Back to main page](https://github.com/Shail-Shouryya/yt-videos-list/)
If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thanks!
