from yt_videos_list import ListCreator

from test_shared import delete_schafer5_file_if_exists


def main():
    test_cases = [
        ListCreator(driver='safari')
    ]

    schafer5_url = 'youtube.com/user/schafer5'
    for test_case in test_cases:
        delete_schafer5_file_if_exists()
        test_case.create_list_for(schafer5_url)


if __name__ == '__main__':
    main()
