# Python Quick Start
<details>
  <summary><b>Python 3.6+ setup (required if not already installed)</b></summary>

This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)), and so requires Python 3.6+.

If you have an older version of Python, you can download Python 3.8.2 (follow links below) and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.
- [macOS 64-bit installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg)
- [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe)
- [Windows x86 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)
- [Gzipped source tarball](https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz) (most useful for Linux)
</details>

<details>
  <summary><b>Permissions for first run</b></summary>

  This is required to make sure you can download and install the required Selenium binary dependencies.
  <details>
  <summary><b>On Windows: makes sure you open <code>Command Prompt</code> or <code>Powershell</code> (both work) in "Run as Administrator" mode</b></summary>

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
```
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
lc.create_list_for(url='https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ')


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
#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!
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
            csv=True,
            txt=True,
            md=True,
            reverse_chronological=True,
            headless=False,
            scroll_pause_time=0.8,
            driver='Firefox'
            )
```
There are a number of optional arguments you can specify during the instantiation of the ListCreator object. The preceding arguments are run by default, but in case you want more flexibility, you can specify the:
- `driver` argument:
  - Firefox (default)
  - Opera
  - Safari
  - Chrome
  - Brave
  - Edge (Windows only)
    - `driver='firefox'`
    - `driver='opera'`
    - `driver='safari'`
    - `driver='chrome'`
    - `driver='brave'`
    - `driver='edge'`
- `csv`, `txt`, `md` file type argument:
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
  <summary><b>Usage Statistics</b></summary>

- [PePy](https://pepy.tech/project/yt-videos-list)
- [PyPi Stats](https://pypistats.org/packages/yt-videos-list)
</details>

#### [Back to main page](https://github.com/Shail-Shouryya/yt_videos_list/)
If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thanks!
