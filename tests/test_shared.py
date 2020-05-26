import os
import shutil
import hashlib

from yt_videos_list import ListCreator


def delete_schafer5_file_if_exists():
    schafer5 = 'CoreySchafer_videos_list'
    if os.path.exists(f'{schafer5}.txt'):
        os.remove(f'{schafer5}.txt')
    if os.path.exists(f'{schafer5}.csv'):
        os.remove(f'{schafer5}.csv')


def create_test_cases(browsers):
    return [
        ListCreator(driver=browser, chronological=chrono)
        for browser in browsers
        for chrono in [False, True]
    ]


def run_test_case(platform, list_creator):
    if platform == 'windows': path_slash = '\\'
    else:                     path_slash = '/'
    schafer5_url = 'youtube.com/user/schafer5'
    delete_schafer5_file_if_exists()
    list_creator.create_list_for(schafer5_url)
    if getattr(list_creator, 'chronological'): verify_update(list_creator, schafer5_url, f'tests{path_slash}partial_schafer5_chronological',     f'tests{path_slash}full_schafer5_chronological')
    else:                                      verify_update(list_creator, schafer5_url, f'tests{path_slash}partial_schafer5_non_chronological', f'tests{path_slash}full_schafer5_non_chronological')


def verify_update(driver, schafer5_url, test_file, full_file):
    shutil.copy(f'{test_file}.txt', 'CoreySchafer_videos_list.txt')
    shutil.copy(f'{test_file}.csv', 'CoreySchafer_videos_list.csv')
    driver.create_list_for(schafer5_url)
    # verify calling the create_list_for() method updates the partial file properly
    with open('CoreySchafer_videos_list.txt', 'r') as test_txt, open('CoreySchafer_videos_list.csv', 'r') as test_csv:
        current_txt = hashlib.sha256(test_txt.read().encode('utf-8')).hexdigest()
        current_csv = hashlib.sha256(test_csv.read().encode('utf-8')).hexdigest()
    with open(f'{full_file}.txt', 'r') as full_txt, open(f'{full_file}.csv', 'r') as full_csv:
        verified_txt = hashlib.sha256(full_txt.read().encode('utf-8')).hexdigest()
        verified_csv = hashlib.sha256(full_csv.read().encode('utf-8')).hexdigest()
    if current_txt != verified_txt: print(f'❌ ERROR! The updated txt file does NOT match the {full_file}.txt file!')
    else:                           print(f'✅ The updated txt file matches the {full_file}.txt file :)')
    if current_csv != verified_csv: print(f'❌ ERROR! The updated csv file does NOT match the {full_file}.csv file!')
    else:                           print(f'✅ The updated csv file matches the {full_file}.csv file :)')
