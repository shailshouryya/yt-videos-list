'''
Test module for testing the selenium safaridriver.
The safaridriver is currently only supported on
macOS machines, so the `yt_videos_list` program
should operate as expected on macOS machines,
but exit with the following message on other
systems:
"Safari is probably not supported on {host} operating
systems. In order for the safaridriver to run on a
{host} OS, you will likely need to do many manual
configurations. For this reason, this package does not
provide built in support for safaridriver on a {host} OS."
'''
from test_shared import run_tests_for, delete_all_test_output_files

if __name__ == '__main__':
    import os
    from determine import determine_user_os
    USER_OS       = determine_user_os()
    if USER_OS == 'windows': os.system(r'.\tests\setup.bat')
    else:                    os.system( 'sh tests/setup.sh')




def main():
    '''
    Tests the selenium safaridriver on the host platform.
    Program should operate as expected on macOS, but
    terminate on other systems with the following:
    "Safari is probably not supported on {host} operating
    systems. In order for the safaridriver to run on a
    {host} OS, you will likely need to do many manual
    configurations. For this reason, this package does not
    provide built in support for safaridriver on a {host} OS."
    '''
    browsers   = ['safari']
    delete_all_test_output_files()
    run_tests_for(browsers)
    delete_all_test_output_files()


if __name__ == '__main__':
    main()
