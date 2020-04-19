# Technical specifications for the yt_videos_list package

This python3 package supports multi-platform, mutli-driver use and is currently under active development.

Currently supported operating systems include MacOS, Linux32, Linux64, Windows32, and Windows64. Currently supported drivers include Firefox, Opera, Safari, and Chrome.

This package provides built-in support for common errors and exceptions, along with helpful hints, including
  - checking to see if the file to be created already exists
    - if it already exists, a message prompts the user to either move/rename the existing file or continue with the write to overwrite the existing file
    - proper way to do so would be to specify the write format for the output file as `csv_write_format='w'` or `txt_write_format='w'` or `docx_write_format='w'`
  - checking to see if the user explicitly specified a driver, and running the program using Firefox and showing the user the available driver options in the terminal output in case they didn't specify a driver
    - explicitly specify driver using
      - `ListCreator(driver='firefox')`
      - `ListCreator(driver='opera')`
      - `ListCreator(driver='safari')`
      - `ListCreator(driver='chrome')`
  - checking to see if the user ran the program in headless mode, and showing the user how to do so in the terminal output if they so wish
    - `ListCreator(headless=True)`
  - checking to see if the user has the correct Selenium dependency installed for the driver they want to run the program in, and showing the user the commands they can run to install the correct dependency if the user has an incorrect dependency (or hasn't downloaded the dependency at all)
    - program checks the operating system of the user's machine and returns a `curl` command piped into a `tar` command to download the correct dependecy into a directory the program can access without having to add the executable to PATH manually
    - user still needs to pick the correct command to run by following the directions
  - checking to see if the result of the scraping returns results, and prompts the user to verify the name/string they provided for `channel` and the `channel_type` they specified
    - if the name/string is correct, the `channel_type` was likely specified incorrectly, so change it to `user` or `channel` (whichever one was not specified the first time)

## Overview of the package structure
### `__init__.py`

### `__main__.py`

### `execute.py`

### `notifications.py`

### `program.py`

### `script.py`
