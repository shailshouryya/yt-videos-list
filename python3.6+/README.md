# python3.6+ Quick Start
<details>
  <summary><b>Python 3.6+ setup (required if not already installed)</b></summary>

This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)) and as such requires Python 3.6+. If you have an older version of Python, you can download the Python 3.8.2 [macOS 64-bit installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg), [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe), [Windows x86 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe), or the [Gzipped source tarball](https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz) (most useful for Linux) and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.

</details>
If this is your first time running this:
##### On Windows: makes sure you "Run as Administrator"
  - shortcut: <mark>⊞ Win</mark> + <mark>X</mark> + <mark>A</mark>
##### On Unix based machines (MacOS, Linux), make sure you have read and write access to `/usr/local/bin/`
  - if not sure, run `sudo chown $USER /usr/local/bin/` in terminal

After you install Python 3.6+ (if needed), enter the following in your command line:

```shell
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U yt-videos-list     # MacOS/Linux
pip install -U yt-videos-list      # Windows
```

### Running the package from the python interpreter
```shell
python3     # MacOS/Linux
python      # Windows
```
```python
from yt_videos_list import ListCreator


my_driver = 'firefox' # SUBSTITUTE THE DRIVER YOU WANT
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
- options for `my_driver` include:
  - `my_driver = 'firefox'`
  - `my_driver = 'opera'`
  - `my_driver = 'safari'`
  - `my_driver = 'chrome'`
  - `my_driver = 'brave'`
  - `my_driver = 'edge'` (Windows only!)
- increase `scroll_pause_time` for laggy internet and decrease `scroll_pause_time` for fast internet
#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!

## [More API information](../docs/python3.6+.md#For-more-control)
## Usage Statistics
<details>

- [PePy](https://pepy.tech/project/yt-videos-list)
- [PyPi Stats](https://pypistats.org/packages/yt-videos-list)

</details>

## [Back to main page](../README.md)
### If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thank you!!
