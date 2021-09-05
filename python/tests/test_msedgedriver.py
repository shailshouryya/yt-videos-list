'''
Test module for testing the selenium msedgedriver.
The msedgedriver is currently only supported on
Windows machines, so the `yt_videos_list` program
should operate as expected on Windows machines,
but exit with the following message on other
systems:
"ERROR! Selenium automation with msedgedriver
(Microsoft Edge) is not yet supported on your
platform. Please use a different browser!"
'''

if __name__ == '__main__':
    import os
    from determine import determine_user_os
    USER_OS       = determine_user_os()
    if USER_OS == 'windows':
        FORMATTED_PIP    = 'pip'
        FORMATTED_PYTHON = 'python'
    else:
        FORMATTED_PIP    = 'pip3'
        FORMATTED_PYTHON = 'python3'
    os.system(f'{FORMATTED_PYTHON} minifier.py')
    os.system(f'{FORMATTED_PIP}    install .')

from test_shared import run_tests_for, delete_all_test_output_files


def main():
    '''
    Tests the selenium msedgedriver on the host platform.
    Program should operate as expected on Windows, but
    terminate on other systems with the following:
    "ERROR! Selenium automation with msedgedriver
    (Microsoft Edge) is not yet supported on your
    platform. Please use a different browser!"
    '''
    browsers   = ['edge']
    run_tests_for(browsers)
    delete_all_test_output_files()


if __name__ == '__main__':
    main()
