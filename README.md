# General Overview


This package provides a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that channel's videos. Follow the link to the API in the language you want to work in from the ***API guides*** section below.

#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!

# API guides
### [python](./python/README.md)

# Other Information

<details>
  <summary><b>Interesting information about YouTube</b></summary>

There are two types of YouTube channels: one type is a `user` channel and the other is a `channel` channel.
- `/user/` channel type:
  - sentdex: https://www.youtube.com/user/sentdex
  - Disney: https://www.youtube.com/user/disneysshows
  - Marvel: https://www.youtube.com/user/MARVEL
  - Apple: https://www.youtube.com/user/Apple
- `/channel/` channel type:
  - Tasty: https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q
  - Billie Eilish: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ
  - Gordon Ramsay: https://www.youtube.com/channel/UCIEv3lZ_tNXHzL3ox-_uUGQ
  - PBS Space Time: https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g
- `/c/` shorthand channel type (new, human readable URL that (usually) consistently provides just the name of the channel) - for easy comparison, all examples below correspond to the 4 `user/` and 4 `channel/` channel types listed above using this new URL formatting:
  - sentdex: https://www.youtube.com/c/sentdex/
  - Disney: https://www.youtube.com/c/Disney/
  - Marvel: https://www.youtube.com/c/marvel/
  - Apple: https://www.youtube.com/user/Apple/ (looks like Apple isn't using the new formatting yet)
  - Tasty: https://www.youtube.com/c/buzzfeedtasty/
  - Billie Eilish: https://www.youtube.com/c/BillieEilish/
  - Gordon Ramsay: https://www.youtube.com/user/gordonramsay/ (looks like Gordon Ramsay switched to the `user/` format instead of `c/`)
  - PBS Space Time: https://www.youtube.com/c/pbsspacetime/
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

Currently supported operating systems include MacOS, Linux32, Linux64, Windows32, and Windows64. Currently supported drivers include Firefox, Opera, Safari (MacOS), Chrome, Brave, and Edge (Windows).

This package provides built-in support for common errors and exceptions, along with helpful hints, including
  - checking to see if the file to be created already exists
  - checking to see if the user explicitly specified a driver to use, and in case they didn't specify a driver, running the program using Firefox as default and showing the user the available driver options in the terminal output
    - explicitly specifying driver using
      - `ListCreator(driver='firefox')`
      - `ListCreator(driver='opera')`
      - `ListCreator(driver='safari')`
      - `ListCreator(driver='chrome')`
      - `ListCreator(driver='brave')`
      - `ListCreator(driver='edge')`
  - running the program in headless mode if using the geckodriver (Firefox) or chromedriver
    - `ListCreator(headless=True)`
  - checking to see if the user has the correct Selenium dependency installed
    - installs and shows the user the commands they can run to install the correct dependency if the user has an incorrect dependency (or hasn't downloaded the dependency at all)
      - program checks the operating system of the user's machine and returns a `curl` command piped into a `tar` command to download the correct dependecy into a directory the program can access without having to add the executable to PATH manually
      - user still needs to pick the correct command to run by following the directions (if autoamted download doesn't complete)
  - checking to see if the result of the scraping returns anything, and prompts the user to verify the `url` argument if nothing is found

</details>

If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thanks!
