import os
import shutil
import hashlib

from yt_videos_list                       import ListCreator
from yt_videos_list.download.user_os_info import determine_user_os


def determine_path_slash():
    if determine_user_os() == 'windows': return '\\'
    else:                                return '/'


def create_test_cases(browsers):
    return [
        ListCreator(driver=browser, reverse_chronological=is_reverse_chronological)
        for browser in browsers
        for is_reverse_chronological in [True, False]
    ]


def delete_txt(filepath):
    if os.path.exists(f'{filepath}.txt'):
        os.remove(f'{filepath}.txt')

def delete_csv(filepath):
    if os.path.exists(f'{filepath}.csv'):
        os.remove(f'{filepath}.csv')

def delete_all_schafer5_files():
    schafer5 = 'CoreySchafer_videos_list'
    delete_txt(schafer5)
    delete_csv(schafer5)


def run_test_case(list_creator):
    path_slash = determine_path_slash()
    schafer5_url = 'youtube.com/user/schafer5'
    delete_all_schafer5_files()
    list_creator.create_list_for(schafer5_url)
    if getattr(list_creator, 'reverse_chronological'): verify_update(list_creator, schafer5_url, f'tests{path_slash}partial_schafer5_reverse_chronological', f'tests{path_slash}full_schafer5_reverse_chronological')
    else:                                              verify_update(list_creator, schafer5_url, f'tests{path_slash}partial_schafer5_chronological',     f'tests{path_slash}full_schafer5_chronological')


def verify_update(driver, schafer5_url, test_file, full_file):
    variations = [use_partial_csv_only, use_partial_txt_only, use_partial_csv_and_txt]
    for variation in variations:
        print(f'\nTESTING list_creator with list_creator.reverse_chronological set to {vars(driver)["reverse_chronological"]}')
        variation(test_file)
        driver.create_list_for(schafer5_url)
        # verify calling the create_list_for() method updates the partial file properly
        compare_test_files_to_reference_files(full_file)


def use_partial_txt_only(test_file):
    print('TESTING with a pre-existing txt file only (no pre-existing csv file)....')
    delete_all_schafer5_files()
    create_partial_txt(test_file)

def use_partial_csv_only(test_file):
    print('TESTING with a pre-existing csv file only (no pre-existing txt file)....')
    delete_all_schafer5_files()
    create_partial_csv(test_file)

def use_partial_csv_and_txt(test_file):
    print('TESTING with both pre-existing txt and csv files....')
    create_partial_txt(test_file)
    create_partial_csv(test_file)


def create_partial_txt(test_file):
    shutil.copy(f'{test_file}.txt', 'CoreySchafer_videos_list.txt')

def create_partial_csv(test_file):
    shutil.copy(f'{test_file}.csv', 'CoreySchafer_videos_list.csv')


def compare_test_files_to_reference_files(full_file):
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
