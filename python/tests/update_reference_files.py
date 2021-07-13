'''
Test module for updating reference files
used for `yt_videos_list` integration testing.
Only the "full_"... files are updated, since the
partial reference files are used as the starting
point during integration testing to verify the
final output at the end of the integration test
matches the corresponding full reference file.
'''
import os

from determine      import determine_path_slash

from yt_videos_list import ListCreator


def main():
    '''
    Updates the full, chronological AND reverse chronological
    txt, csv, md reference files for the
    youtube.com/user/schafer5 channel (the reference channel
    for testing) before moving the updated files into the
    testing directory path (yt_videos_list/python/tests/).
    '''
    update_schafer5_chronological()
    update_schafer5_non_chronological()
    move_reference_files_to_tests()


def update_schafer5_chronological():
    '''
    Updates the full, chronological txt, csv, md
    reference files for the
    youtube.com/user/schafer5 channel (the
    reference channel for testing).
    '''
    ListCreator(reverse_chronological=False).create_list_for('youtube.com/user/schafer5', file_name='full_schafer5_chronological')


def update_schafer5_non_chronological():
    '''
    Updates the full, reverse chronological
    txt, csv, md reference files for the
    youtube.com/user/schafer5 channel (the
    reference channel for testing).
    '''
    ListCreator(reverse_chronological=True).create_list_for('youtube.com/user/schafer5', file_name='full_schafer5_reverse_chronological') # reverse_chronological is already True by default, just included here to be explicit


def move_reference_files_to_tests():
    '''
    Moves the updated reference files from the current path
    (yt_videos_list/python/) into the testing directory path
    (yt_videos_list/python/tests/).
    '''
    path_slash = determine_path_slash()
    os.replace('full_schafer5_chronological.txt',         f'tests{path_slash}reference_files{path_slash}full_schafer5_chronological.txt')
    os.replace('full_schafer5_chronological.csv',         f'tests{path_slash}reference_files{path_slash}full_schafer5_chronological.csv')
    os.replace('full_schafer5_chronological.md',          f'tests{path_slash}reference_files{path_slash}full_schafer5_chronological.md')
    os.replace('full_schafer5_reverse_chronological.txt', f'tests{path_slash}reference_files{path_slash}full_schafer5_reverse_chronological.txt')
    os.replace('full_schafer5_reverse_chronological.csv', f'tests{path_slash}reference_files{path_slash}full_schafer5_reverse_chronological.csv')
    os.replace('full_schafer5_reverse_chronological.md',  f'tests{path_slash}reference_files{path_slash}full_schafer5_reverse_chronological.md')


if __name__ == '__main__':
    main()
