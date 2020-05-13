from yt_videos_list import ListCreator

from test_shared import delete_schafer5_file_if_exists


def main():
    schafer5_url = 'youtube.com/user/schafer5'
    delete_schafer5_file_if_exists()
    ListCreator(driver='edge').create_list_for(schafer5_url)


if __name__ == '__main__':
    main()
