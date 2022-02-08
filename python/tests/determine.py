import platform
import sys


def determine_user_os():
    '''
    This is the exact same function as the `determine_user_os()`
    function in the `download.user_os_info.py` module. This
    is included in a separate file under the `tests/` directory
    to avoid the problem of importing the function from
    `yt_videos_list`. Loading the function from the submodule
    itself doesn't cause problems, but doing so prevents us
    from reloading `yt_videos_list` into memory after performing
    `pip install .`
    or
    `pip3 install .` in the same python instance.
    '''
    user_os = platform.system().lower()
    if   user_os.startswith('darwin'):  return 'macos'
    elif user_os.startswith('linux'):   return 'linux'
    elif user_os.startswith('windows'): return 'windows'
    else:
        raise RuntimeError(f'Unsupported operating system! You are on: {user_os}\nPlease add tests to verify the program runs properly on {user_os}.\nNow exiting tests...')


def determine_path_slash():
    r'''
    Returns the type of slash used in the file system of
    the host machine. i.e.
    Windows: '\\'
    macOS:   '/'
    Linux:   '/'
    '''
    if determine_user_os() == 'windows': return '\\'
    else:                                return '/'
