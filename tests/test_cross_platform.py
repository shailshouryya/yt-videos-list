import os
import platform
os.system('pip install .')

from yt_videos_list.download.windows_info import get_drive_letter
from test_shared                          import create_test_cases, delete_schafer5_file_if_exists, verify_update



PLATFORM = platform.system().lower()

def remove_dependencies():
    if PLATFORM == 'windows':
        drive = get_drive_letter()
        geckodriver_path  = rf'{drive}:\Windows\geckodriver.exe'
        operadriver_path  = rf'{drive}:\Windows\operadriver.exe'
        chromedriver_path = rf'{drive}:\Windows\chromedriver.exe'
        bravedriver_path  = rf'{drive}:\Windows\bravedriver.exe'
    else:
        geckodriver_path  = r'/usr/local/bin/geckodriver'
        operadriver_path  = r'/usr/local/bin/operadriver'
        chromedriver_path = r'/usr/local/bin/chromedriver'
        bravedriver_path  = r'/usr/local/bin/bravedriver'
    if os.path.exists(geckodriver_path):  os.remove(geckodriver_path)
    if os.path.exists(operadriver_path):  os.remove(operadriver_path)
    if os.path.exists(chromedriver_path): os.remove(chromedriver_path)
    if os.path.exists(bravedriver_path):  os.remove(bravedriver_path)


def main():
    browsers   = ['firefox', 'opera', 'chrome', 'brave']
    test_cases = create_test_cases(browsers)
    if PLATFORM == 'windows': path_slash = '\\'
    else:                     path_slash = '/'


    remove_dependencies()
    schafer5_url = 'youtube.com/user/schafer5'
    for test_case in test_cases:
        delete_schafer5_file_if_exists()
        test_case.create_list_for(schafer5_url)
        if getattr(test_case, 'chronological'): verify_update(test_case, schafer5_url, f'tests{path_slash}partial_schafer5_chronological',     f'tests{path_slash}full_schafer5_chronological')
        else:                                   verify_update(test_case, schafer5_url, f'tests{path_slash}partial_schafer5_non_chronological', f'tests{path_slash}full_schafer5_non_chronological')
        print('Moving on to the next driver...\n' + '⏬ '*11)


# add these later
# lc_firefox.headless = True
# lc_opera.headless = True
# lc_safari.headless = True
# lc_chrome.headless = True


if __name__ == '__main__':
    main()
