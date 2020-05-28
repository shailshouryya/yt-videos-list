import os

from . import file
from .notifications import Common


COMMON_MESSAGE = Common()


def determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name, txt, csv):
    txt_exists = os.path.isfile(f'{file_name}.txt')
    csv_exists = os.path.isfile(f'{file_name}.csv')
    if txt_exists and csv_exists: videos_list = file.update_file.scroll_to_old_videos(url, driver, scroll_pause_time, txt_exists, csv_exists, file_name)
    else:                         videos_list = file.create_file.scroll_to_bottom    (url, driver, scroll_pause_time) # run when either the txt or csv file needs to be created from scratch
    if len(videos_list) == 0:
        print(COMMON_MESSAGE.no_videos_found)
        return

    if txt is True:
        if txt_exists: file.update_file.write_to_txt(videos_list, file_name, reverse_chronological)
        else:          file.create_file.write_to_txt(videos_list, file_name, reverse_chronological)
    if csv is True:
        if csv_exists: file.update_file.write_to_csv(videos_list, file_name, reverse_chronological)
        else:          file.create_file.write_to_csv(videos_list, file_name, reverse_chronological)
