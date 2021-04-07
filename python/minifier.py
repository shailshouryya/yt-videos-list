'''
Script to strip all comments and extra whitespace from code
in `dev/` directory (used during development) before placing
formatted code in `yt_videos_list` directory (shipped on PyPI).
'''

import os
import re
import shutil

from tests.determine import determine_path_slash


def clear_target_directory(target_directory):
    readme = f'./{target_directory}/README.md'
    shutil.move  (f'{readme}', 'temp.md')
    shutil.rmtree(f'./{target_directory}')
    os.mkdir(target_directory)
    shutil.move('temp.md', f'{readme}')


def minify_source_directory_into_target_directory(slash, source_directory, target_directory):
    valid_files       = []
    local_directories = set()
    for root, _, files in os.walk(os.path.abspath(f'./{source_directory}')):
        for file in files:
            filepath = os.path.join(root, file).split(source_directory)[1]
            if filepath.endswith('DS_Store'): continue
            if '__pycache__' in filepath:     continue
            local_directory = root.split(source_directory)[1]
            if local_directory: local_directories.add(local_directory) # truthy check skips adding an empty string '' to local_directories for files that are in root of source_directory
            valid_files.append(filepath)
    for local_directory in local_directories:
        os.makedirs(f'{target_directory}{local_directory}', exist_ok=True) # since sets are unordered, we might create a nested directory before the outer directory, so the exist_ok argument=True avoids this error -> FileExistsError: [Errno 17] File exists: '{local_directory}' (which is an outer directory for a nested directory that we made in the process of making a nested directory)
    for file in valid_files:
        with open(f'{source_directory}{slash}{file}', 'r', encoding='utf-8') as read_file, open(f'{target_directory}{slash}{file}', 'w', encoding='utf-8') as write_file:
            if '__init__.py' in file:
                write_file.write(read_file.read())
                continue
            formatted = read_file.read()
            formatted = re.sub(' +# .+',   '', formatted)                     # remove comments from lines that end with comments
            formatted = re.sub('^\s*# .+', '', formatted, flags=re.MULTILINE) # remove lines that contain only comments and no code
            formatted = re.sub(' +\n',     '', formatted)                     # remove lines that contain only spaces
            formatted = re.sub('^\n',      '', formatted, flags=re.MULTILINE) # remove lines that contain only a newline
            if 'write.py' not in file:
                formatted = re.sub('    ',           ' ',       formatted) # replace 4 spaces with 1 space (reduces spaces taken by indentation)
                formatted = re.sub('([\S])  +?(\S)', '\\1 \\2', formatted) # replace extra spacing anywhere in a line given the character before AND after the spaces is a non-space character (the non-space character check avoids replacing spaces necessary for indentation)
            write_file.write(formatted)


def main():
    slash            = determine_path_slash()
    source_directory = 'dev'
    target_directory = 'yt_videos_list'

    clear_target_directory(target_directory)
    minify_source_directory_into_target_directory(slash, source_directory, target_directory)


if __name__ == '__main__':
    main()
