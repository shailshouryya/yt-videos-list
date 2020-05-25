import os
import hashlib
import platform
os.system('pip install .')

from yt_videos_list                       import ListCreator
from yt_videos_list.download.windows_info import get_drive_letter
from test_shared                          import delete_schafer5_file_if_exists



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

def verify_update(driver, schafer5_url, test_file, full_file):
    os.rename(f'{test_file}.txt', 'CoreySchafer_videos_list.txt')
    os.rename(f'{test_file}.csv', 'CoreySchafer_videos_list.csv')
    driver.create_list_for(schafer5_url)
    # verify calling the create_list_for() method updates the partial file properly
    with open('CoreySchafer_videos_list.txt', 'r') as test_txt, open('CoreySchafer_videos_list.csv', 'r') as test_csv:
        current_txt = hashlib.sha256(test_txt.read().encode('utf-8')).hexdigest()
        current_csv = hashlib.sha256(test_csv.read().encode('utf-8')).hexdigest()
    with open(f'{full_file}.txt', 'r') as full_txt, open(f'{full_file}.csv', 'r') as full_csv:
        verified_txt = hashlib.sha256(full_txt.read().encode('utf-8')).hexdigest()
        verified_csv = hashlib.sha256(full_csv.read().encode('utf-8')).hexdigest()
    if current_txt != verified_txt: print(f'The updated txt file does NOT match the {full_file}.txt file!')
    else:                           print(f'The updated txt file matches the {full_file}.txt file :)')
    if current_csv != verified_csv: print(f'The updated csv file does NOT match the {full_file}.csv file!')
    else:                           print(f'The updated csv file matches the {full_file}.csv file :)')


def main():
    test_cases = [
        ListCreator(driver='firefox'),
        ListCreator(driver='opera'),
        ListCreator(driver='chrome'),
        ListCreator(driver='brave')
    ]


    remove_dependencies()
    schafer5_url = 'youtube.com/user/schafer5'
    for test_case in test_cases:
        delete_schafer5_file_if_exists()
        test_case.create_list_for(schafer5_url)
        if getattr(test_case, 'chronological'): verify_update(test_case, schafer5_url, 'tests/partial_schafer5_chronological',     'tests/full_schafer5_chronological')
        else:                                   verify_update(test_case, schafer5_url, 'tests/partial_schafer5_non_chronological', 'tests/full_schafer5_non_chronological')


# add these later
# lc_firefox.headless = True
# lc_opera.headless = True
# lc_safari.headless = True
# lc_chrome.headless = True


if __name__ == '__main__':
    main()
