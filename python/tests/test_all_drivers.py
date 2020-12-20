'''
Test module for testing all drivers currently
supported by the `yt_videos_list` package.
'''
import test_cross_platform_drivers
import test_safaridriver
import test_msedgedriver

from determine import determine_user_os

def main():
    '''
    Runs test cases on cross platform drivers
    (firefox, opera, chrome, brave) first, then runs test
    cases for platform specific drivers. On macOS,
    safaridriver is tested before msedgedriver,
    and on Windows msedgedriver is tested before
    safaridriver. Since msedgedriver is incompatible
    on macOS and safaridriver is incompatible on
    Windows, they are tested last since the
    `yt_videos_list` program terminates on
    an incompatible driver with an error message.
    '''
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
