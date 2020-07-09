# General Overview
This package provides a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that channel's videos. Follow the link to the API in the language you want to work in from the API guides section below.

#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!

# API guides
### [python3](./python3.6+/README.md)

# Other Information
<details>
  <summary><b>Dependencies</b></summary>

**NOTE**: You need to have the Selenium driver installed to run this package
- the first time you run this package the automated downloader should install everything you need, but in case it doesn't, refer to the link below and/or file an [issue here](https://github.com/Shail-Shouryya/yt_videos_list/issues).
  - Manual Selenium downloads **[here](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/docs/dependencies_pseudo_json.txt)**
- The Selenium drivers are all pretty similar but differ in subtle ways, so play around with them and see what's different :)

**NOTE** that you also need the corresponding browser installed to properly run the selenium driver.
- To download the most recent version of the browser, go to the page for:
  - [Firefox](https://www.mozilla.org/en-US/firefox/new/)
  - [Opera](https://www.opera.com/)
  - [Chrome](https://www.google.com/chrome/)
  - [Brave](https://brave.com/)
  - [Edge](https://www.microsoft.com/edge)
</details>

<details>
  <summary><b>Interesting information about YouTube</b></summary>

There are two types of YouTube channels: one type is a `user` channel and the other is a `channel` channel.
- `user` channel type:
  - sentdex: https://www.youtube.com/user/sentdex
  - Disney: https://www.youtube.com/user/disneysshows
  - Marvel: https://www.youtube.com/user/MARVEL
  - Apple: https://www.youtube.com/user/Apple
- `channel` channel type:
  - Tasty: https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q
  - Billie Eilish: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ
  - Gordon Ramsay: https://www.youtube.com/channel/UCIEv3lZ_tNXHzL3ox-_uUGQ
  - PBS Space Time: https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g
</details>

<details>
  <summary><b>Future Features</b></summary>

### Main Features
- [X] take url and scrape the video name and url for every video for that user
- [X] create [txt](https://fileinfo.com/extension/txt), [csv](https://en.wikipedia.org/wiki/Comma-separated_values), [md](https://en.wikipedia.org/wiki/Markdown) files

### Additional Features
- [x] enable custom name for output file
- [x] update previously created file with new videos uploaded since file creation
  - [x] put all urls from file in a (hash) set and check to see if any urls on page (next time program runs on same page) are missing from the (hash) set
- [ ] create web interface
  - [ ] input box for channel url
  - [ ] generate static HTML page with video URLs for output

</details>

<details>
  <summary><b>Technical Specifications</b></summary>

This python3 package supports multi-platform, mutli-driver use and is currently under active development.

Currently supported operating systems include MacOS, Linux32, Linux64, Windows32, and Windows64. Currently supported drivers include Firefox, Opera, Safari, and Chrome.

This package provides built-in support for common errors and exceptions, along with helpful hints, including
  - checking to see if the file to be created already exists
    - if it already exists, a message prompts the user to either move/rename the existing file or continue with the write to overwrite the existing file
    - proper way to do so would be to specify the write format for the output file as `csv_write_format='w'` or `txt_write_format='w'` or `docx_write_format='w'`
  - checking to see if the user explicitly specified a driver, and running the program using Firefox and showing the user the available driver options in the terminal output in case they didn't specify a driver
    - explicitly specifying driver using
      - `ListCreator(driver='firefox')`
      - `ListCreator(driver='opera')`
      - `ListCreator(driver='safari')`
      - `ListCreator(driver='chrome')`
  - checking to see if the user ran the program in headless mode, and showing the user how to do so in the terminal output if they so wish
    - `ListCreator(headless=True)`
  - checking to see if the user has the correct Selenium dependency installed for the driver they want to run the program in, and showing the user the commands they can run to install the correct dependency if the user has an incorrect dependency (or hasn't downloaded the dependency at all)
    - program checks the operating system of the user's machine and returns a `curl` command piped into a `tar` command to download the correct dependecy into a directory the program can access without having to add the executable to PATH manually
    - user still needs to pick the correct command to run by following the directions
  - checking to see if the result of the scraping returns results, and prompts the user to verify the `url` argument if no results are found

### Overview of package structure
#### `__init__.py`

#### `__main__.py`

#### `script.py`

#### `execute.py`

#### `program.py`

#### `file` submodule

#### `download` submodule

#### `notifications.py`



</details>

<details>
  <summary><b>Usage Statistics</b></summary>

- [PePy](https://pepy.tech/project/yt-videos-list)
- [PyPi Stats](https://pypistats.org/packages/yt-videos-list)
</details>

If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thanks!
