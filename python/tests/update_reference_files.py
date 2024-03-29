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
    update_expected_chronological_test_output()
    update_expected_reverse_chronological_test_output()
    move_reference_files_to_tests()


def update_expected_chronological_test_output():
    '''
    Updates the full, chronological txt, csv, md
    reference files for the
    youtube.com/user/schafer5 channel (the
    reference channel for testing).
    '''
    ListCreator(reverse_chronological=False, video_id_only=False).create_list_for('youtube.com/user/schafer5', file_name='full_CoreySchafer_chronological_videos_list')
    ListCreator(reverse_chronological=False, video_id_only=True ).create_list_for('youtube.com/user/schafer5', file_name='full_CoreySchafer_chronological_video_ids_list')


def update_expected_reverse_chronological_test_output():
    '''
    Updates the full, reverse chronological
    txt, csv, md reference files for the
    youtube.com/user/schafer5 channel (the
    reference channel for testing).
    '''
    # reverse_chronological is already True by default, just included here to be explicit
    ListCreator(reverse_chronological=True, video_id_only=False).create_list_for('youtube.com/user/schafer5', file_name='full_CoreySchafer_reverse_chronological_videos_list')
    ListCreator(reverse_chronological=True, video_id_only=True ).create_list_for('youtube.com/user/schafer5', file_name='full_CoreySchafer_reverse_chronological_video_ids_list')


def move_reference_files_to_tests():
    '''
    Moves the updated reference files from the current path
    (yt_videos_list/python/) into the testing directory path
    (yt_videos_list/python/tests/).
    '''
    path_slash = determine_path_slash()
    file_names = [
        'full_CoreySchafer_chronological_videos_list',
        'full_CoreySchafer_chronological_video_ids_list',
        'full_CoreySchafer_reverse_chronological_videos_list',
        'full_CoreySchafer_reverse_chronological_video_ids_list',
    ]
    for file_name in file_names:
        for extension in ['csv', 'txt', 'md']:
            os.replace(f'{file_name}.{extension}', f'tests{path_slash}reference_files{path_slash}{file_name}.{extension}')


if __name__ == '__main__':
    main()
