import os
import platform
os.system('pip install .')

from yt_videos_list.windows import get_drive_letter
from yt_videos_list import ListCreator


PLATFORM = platform.system().lower()

def remove_dependencies():
    if PLATFORM == 'windows':
        drive = get_drive_letter()
        if os.path.exists(rf'{drive}:\Windows\geckodriver.exe'):
            os.remove(rf'{drive}:\Windows\geckodriver.exe')
        if os.path.exists(rf'{drive}:\Windows\operadriver.exe'):
            os.remove(rf'{drive}:\Windows\operadriver.exe')
        if os.path.exists(rf'{drive}:\Windows\chromedriver.exe'):
            os.remove(rf'{drive}:\Windows\chromedriver.exe')
        if os.path.exists(rf'{drive}:\Windows\bravedriver.exe'):
            os.remove(rf'{drive}:\Windows\bravedriver.exe')
    else:
        if os.path.exists(r'/usr/local/bin/geckodriver'):
            os.remove(r'/usr/local/bin/geckodriver')
        if os.path.exists(r'/usr/local/bin/operadriver'):
            os.remove(r'/usr/local/bin/operadriver')
        if os.path.exists(r'/usr/local/bin/chromedriver'):
            os.remove(r'/usr/local/bin/chromedriver')
        if os.path.exists(r'/usr/local/bin/bravedriver'):
            os.remove(r'/usr/local/bin/bravedriver')


def delete_schafer5_file_if_exists():
    if os.path.exists('schafer5VideosList.txt'):
        os.remove('schafer5VideosList.txt')
    if os.path.exists('schafer5VideosList.csv'):
        os.remove('schafer5VideosList.csv')

def main():
    lc_firefox = ListCreator(driver='firefox')
    lc_opera   = ListCreator(driver='opera')
    lc_safari  = ListCreator(driver='safari')
    lc_chrome  = ListCreator(driver='chrome')
    lc_brave   = ListCreator(driver='brave')

    remove_dependencies()
    delete_schafer5_file_if_exists()
    lc_firefox.create_list_for('youtube.com/user/schafer5')
    delete_schafer5_file_if_exists()
    lc_opera.create_list_for  ('youtube.com/user/schafer5')
    if PLATFORM == 'darwin':
        delete_schafer5_file_if_exists()
        lc_safari.create_list_for ('youtube.com/user/schafer5')
    delete_schafer5_file_if_exists()
    lc_chrome.create_list_for ('youtube.com/user/schafer5')
    delete_schafer5_file_if_exists()
    lc_brave.create_list_for ('youtube.com/user/schafer5')

# add these later
# lc_firefox.headless = True
# lc_opera.headless = True
# lc_safari.headless = True
# lc_chrome.headless = True


if __name__ == '__main__':
    main()
