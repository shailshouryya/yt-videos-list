'''
Test module for testing all drivers currently
supported by the `yt_videos_list` package AND
compatible across operating systems.
'''
import os

from determine import determine_user_os
if __name__ == '__main__':
    USER_OS          = determine_user_os()
    if USER_OS == 'windows':
        FORMATTED_PIP    = 'pip'
        FORMATTED_PYTHON = 'python'
    else:
        FORMATTED_PIP    = 'pip3'
        FORMATTED_PYTHON = 'python3'
    os.system(f'{FORMATTED_PYTHON} minifier.py')
    os.system(f'{FORMATTED_PIP}    install .')


from test_shared                          import run_tests_for


from yt_videos_list.download.windows_info import get_drive_letter



def remove_dependencies():
    '''
    Removes all currently installed selenium
    webdriver binaries from system path to simulate
    a clean install of the package. Removing
    dependencies before running the package ensures
    no gaps exist during the build step, and simulates
    a new user downloading the package and running it
    for the first time.
    '''
    if determine_user_os() == 'windows':
        drive = get_drive_letter()
        geckodriver_path  = rf'{drive}:\Windows\geckodriver.exe'
        operadriver_path  = rf'{drive}:\Windows\operadriver.exe'
        chromedriver_path = rf'{drive}:\Windows\chromedriver.exe'
        bravedriver_path  = rf'{drive}:\Windows\bravedriver.exe'
        msedgedriver_path = rf'{drive}:\Windows\msedgedriver.exe'
    else:
        geckodriver_path  = r'/usr/local/bin/geckodriver'
        operadriver_path  = r'/usr/local/bin/operadriver'
        chromedriver_path = r'/usr/local/bin/chromedriver'
        bravedriver_path  = r'/usr/local/bin/bravedriver'
        msedgedriver_path = r'/usr/local/bin/msedgedriver'
    if os.path.exists(geckodriver_path):  os.remove(geckodriver_path)
    if os.path.exists(operadriver_path):  os.remove(operadriver_path)
    if os.path.exists(chromedriver_path): os.remove(chromedriver_path)
    if os.path.exists(bravedriver_path):  os.remove(bravedriver_path)
    if os.path.exists(msedgedriver_path): os.remove(msedgedriver_path)


def main():
    '''
    Removes all currently installed selenium
    webdriver binaries, then calls the `run_tests_for()`
    function from the `tests/test_shared.py` module.
    The `run_tests_for()` function is the starting point
    for all logic required to run integration tests for
    the `yt_videos_list` package, and uses helper
    funcations to carry out specific tasks.
    '''
    remove_dependencies()
    browsers   = ['firefox', 'opera', 'chrome', 'brave']
    run_tests_for(browsers)


# add these later
# lc_firefox.headless = True
# lc_opera.headless = True
# lc_safari.headless = True
# lc_chrome.headless = True


if __name__ == '__main__':
    main()
