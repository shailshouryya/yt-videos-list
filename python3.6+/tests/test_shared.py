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


def delete_file(filepath, extension):
    if os.path.exists(f'{filepath}.{extension}'):
        os.remove(f'{filepath}.{extension}')

def delete_all_schafer5_files():
    schafer5 = 'CoreySchafer_videos_list'
    delete_file(schafer5, 'txt')
    delete_file(schafer5, 'csv')
    delete_file(schafer5, 'md' )


def run_test_case(list_creator):
    path_slash = determine_path_slash()
    schafer5_url = 'youtube.com/user/schafer5'
    delete_all_schafer5_files()
    list_creator.create_list_for(schafer5_url)
    if getattr(list_creator, 'reverse_chronological'): verify_update(list_creator, schafer5_url, f'tests{path_slash}partial_schafer5_reverse_chronological', f'tests{path_slash}full_schafer5_reverse_chronological')
    else:                                              verify_update(list_creator, schafer5_url, f'tests{path_slash}partial_schafer5_chronological',     f'tests{path_slash}full_schafer5_chronological')


def verify_update(driver, schafer5_url, test_file, full_file):
    variations = [use_partial_csv_only, use_partial_txt_only, use_partial_md_only, use_partial_csv_txt_and_md]
    for variation in variations:
        print(f'\nTESTING list_creator with list_creator.reverse_chronological set to {vars(driver)["reverse_chronological"]}')
        variation(test_file)
        driver.create_list_for(schafer5_url)
        # verify calling the create_list_for() method updates the partial file properly
        compare_test_files_to_reference_files(full_file)


def use_partial_txt_only(test_file):
    print('TESTING with a pre-existing txt file only (no pre-existing csv or md file)....')
    delete_all_schafer5_files()
    create_partial_file(test_file, 'txt')

def use_partial_csv_only(test_file):
    print('TESTING with a pre-existing csv file only (no pre-existing txt or md file)....')
    delete_all_schafer5_files()
    create_partial_file(test_file, 'csv')

def use_partial_md_only(test_file):
    print('TESTING with a pre-existing md file only (no pre-existing txt or csv file)....')
    delete_all_schafer5_files()
    create_partial_file(test_file, 'md')

def use_partial_csv_txt_and_md(test_file):
    print('TESTING with pre-existing txt, csv, and md files....')
    create_partial_file(test_file, 'txt')
    create_partial_file(test_file, 'csv')
    create_partial_file(test_file, 'md' )

def create_partial_file(test_file, extension):
    shutil.copy(f'{test_file}.{extension}', f'CoreySchafer_videos_list.{extension}')


def compare_test_files_to_reference_files(full_file):
    with open('CoreySchafer_videos_list.txt', 'r') as test_txt, open('CoreySchafer_videos_list.csv', 'r') as test_csv, open('CoreySchafer_videos_list.md', 'r') as test_md:
        current_txt = hashlib.sha256(test_txt.read().encode('utf-8')).hexdigest()
        current_csv = hashlib.sha256(test_csv.read().encode('utf-8')).hexdigest()
        current_md  = hashlib.sha256(test_md.read().encode ('utf-8')).hexdigest()
    with open(f'{full_file}.txt', 'r') as full_txt, open(f'{full_file}.csv', 'r') as full_csv, open(f'{full_file}.md', 'r') as full_md:
        verified_txt = hashlib.sha256(full_txt.read().encode('utf-8')).hexdigest()
        verified_csv = hashlib.sha256(full_csv.read().encode('utf-8')).hexdigest()
        verified_md  = hashlib.sha256(full_md.read().encode ('utf-8')).hexdigest()
    if current_txt != verified_txt: print(f'❌ ERROR! The updated txt file does NOT match the {full_file}.txt file!')
    else:                           print(f'✅ The updated txt file matches the {full_file}.txt file :)')
    if current_csv != verified_csv: print(f'❌ ERROR! The updated csv file does NOT match the {full_file}.csv file!')
    else:                           print(f'✅ The updated csv file matches the {full_file}.csv file :)')
    if current_md  != verified_md:  print(f'❌ ERROR! The updated md  file does NOT match the {full_file}.md file!')
    else:                           print(f'✅ The updated md  file matches the {full_file}.md file :)')
