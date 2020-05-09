import os

from yt_videos_list import ListCreator


def delete_schafer5_file_if_exists():
    if os.path.exists('schafer5VideosList.txt'):
        os.remove('schafer5VideosList.txt')
    if os.path.exists('schafer5VideosList.csv'):
        os.remove('schafer5VideosList.csv')


lc_firefox = ListCreator(driver='firefox')
lc_opera   = ListCreator(driver='opera')
lc_safari  = ListCreator(driver='safari')
lc_chrome  = ListCreator(driver='chrome')


delete_schafer5_file_if_exists()
lc_firefox.create_list_for('youtube.com/user/schafer5')
delete_schafer5_file_if_exists()
lc_opera.create_list_for  ('youtube.com/user/schafer5')
delete_schafer5_file_if_exists()
lc_safari.create_list_for ('youtube.com/user/schafer5')
delete_schafer5_file_if_exists()
lc_chrome.create_list_for ('youtube.com/user/schafer5')

lc_firefox.headless = True
lc_opera.headless = True
lc_safari.headless = True
lc_chrome.headless = True
