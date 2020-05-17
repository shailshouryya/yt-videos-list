from . import create_file
from .notifications import Common


COMMON_MESSAGE = Common()

def determine_action(url, driver, scroll_pause_time, chronological, file_name, txt, txt_write_format, csv, csv_write_format):
    videos_list = create_file.scroll_to_bottom(url, driver, scroll_pause_time)
    if len(videos_list) == 0:
        print(COMMON_MESSAGE.no_videos_found)
        return
    if txt is True: create_file.write_to_txt(videos_list, file_name, txt_write_format, chronological)
    if csv is True: create_file.write_to_csv(videos_list, file_name, csv_write_format, chronological)
