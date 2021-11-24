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
    os.system(f'{FORMATTED_PIP}    install . --use-feature=in-tree-build')

from test_shared import run_tests_for, delete_all_test_output_files


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
    run_tests_for(browsers)
    delete_all_test_output_files()


if __name__ == '__main__':
    main()
