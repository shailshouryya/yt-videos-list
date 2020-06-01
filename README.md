# Automate creation of videos lists for YouTube channels
**TABLE OF CONTENTS**
<br>[Quick Start](./README.md#Quick-Start)
<br>[Running the package from the python interpreter](./README.md#Running-the-package-from-the-python-interpreter)
<br>[For more control](./docs_python.md#For-more-control)


## Quick Start
This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)) and as such requires Python 3.6+. If you have an older version of Python, you can download the Python 3.8.2 [macOS 64-bit installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg), [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe), [Windows x86 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe), or the [Gzipped source tarball](https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz) (most useful for Linux) and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.

Once you do that, enter the following in your command line:
```shell
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U yt-videos-list
# no "3" on Windows: pip install -U yt-videos-list
```

### Running the package from the python interpreter
```shell
python3
# no "3" on Windows: python
```
```python
from yt_videos_list import ListCreator

my_driver = 'firefox' # SUBSTITUTE THE DRIVER YOU WANT
lc = ListCreator(driver=my_driver)

# "user" channel_type (example uses Corey Schafer):
lc.create_list_for(url='https://www.youtube.com/user/schafer5')

# "channel" channel_type (example uses freeCodeCamp) along with the optional file_name argument:
lc.create_list_for(url='https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ', file_name='freeCodeCamp_org')

# see the new files that were just created:
import os
# MacOS and Linux users:
os.system('ls -lt | head')
# Windows users:
os.system('dir /O-D | find "_videos_list"')

# for more information on using the module:
help(lc)
```

### Running the package from the CLI as a script using -m (coming in `yt-videos-list 2.0`!)
```shell
python3 -m yt_videos_list
```
