import os

from yt_videos_list import ListCreator
from test_shared import determine_path_slash


def update_schafer5_chronological():
    ListCreator(reverse_chronological=False).create_list_for('youtube.com/user/schafer5', file_name='full_schafer5_chronological')


def update_schafer5_non_chronological():
    ListCreator(reverse_chronological=True).create_list_for('youtube.com/user/schafer5', file_name='full_schafer5_non_chronological') # reverse_chronological is already True by default, just included here to be explicit


def move_reference_files_to_tests():
    path_slash = determine_path_slash()
    os.replace('full_schafer5_chronological.txt', f'tests{path_slash}full_schafer5_chronological.txt')
    os.replace('full_schafer5_chronological.csv', f'tests{path_slash}full_schafer5_chronological.csv')
    os.replace('full_schafer5_non_chronological.txt', f'tests{path_slash}full_schafer5_non_chronological.txt')
    os.replace('full_schafer5_non_chronological.csv', f'tests{path_slash}full_schafer5_non_chronological.csv')


def main():
    update_schafer5_chronological()
    update_schafer5_non_chronological()
    move_reference_files_to_tests()


if __name__ == '__main__':
    main()
