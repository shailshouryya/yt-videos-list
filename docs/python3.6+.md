# For more control
---
**NOTE** that you can also access all the information below in the `python3` interpreter by entering
```python
from yt_videos_list import ListCreator`
help(ListCreator)
```

---
```python
ListCreator(csv=True, txt=True, reverse_chronological=True,
            headless=False, scroll_pause_time=0.8,
            driver='Firefox')
```
There are a number of optional arguments you can specify during the instantiation of the ListCreator object. The preceding arguments are run by default, but in case you want more flexibility, you can specify the:

- `driver` argument:
  - Firefox (default)
  - Opera
  - Safari
  - Chrome
  - Brave
  - Edge
    - `driver='firefox'`
    - `driver='opera'`
    - `driver='safari'`
    - `driver='chrome'`
    - `driver='brave'`
    - `driver='edge'`
- `csv`, `txt` file type argument:
  - `True` (default) - create a file for the specified type
  - `False` - do not create a file for the specified type.
    - `txt=True`  (default) OR `txt=False`
    - `csv=True`  (default) OR `csv=False`
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

## [Back to python3.6+ main page](../python3.6+/README.md)
