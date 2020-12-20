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

from test_shared import run_tests_for


def main():
    browsers   = ['edge']
    run_tests_for(browsers)


if __name__ == '__main__':
    main()
