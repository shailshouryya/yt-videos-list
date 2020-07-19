import test_cross_platform_drivers
import test_safaridriver
import test_msedgedriver

from yt_videos_list.download.user_os_info import determine_user_os

def main():
    test_cross_platform_drivers.main()
    user_os = determine_user_os()
    if user_os == 'macos':
        test_safaridriver.main()
        test_msedgedriver.main()
    elif user_os == 'windows':
        test_msedgedriver.main()
        test_safaridriver.main()

if __name__ == '__main__':
    main()
