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
    schafer5 = 'schafer5VideosList'
    if os.path.exists(f'{schafer5}.txt'):
        os.remove(f'{schafer5}.txt')
    if os.path.exists(f'{schafer5}.csv'):
        os.remove(f'{schafer5}.csv')

def main():
    test_cases = [
        ListCreator(driver='firefox'),
        ListCreator(driver='opera'),
        ListCreator(driver='chrome'),
        ListCreator(driver='brave'),
        ListCreator(driver='edge'),
        ListCreator(driver='safari')
    ]


    remove_dependencies()
    schafer5_url = 'youtube.com/user/schafer5'
    for test_case in test_cases:
        delete_schafer5_file_if_exists()
        test_case.create_list_for(schafer5_url)

# add these later
# lc_firefox.headless = True
# lc_opera.headless = True
# lc_safari.headless = True
# lc_chrome.headless = True


if __name__ == '__main__':
    main()
