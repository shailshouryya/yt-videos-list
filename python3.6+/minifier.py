import os
import re
import time
import shutil

from tests.test_shared import determine_path_slash


def clear_target_directory(target_directory):
    readme           = f'./{target_directory}/README.md'

    shutil.move  (f'{readme}', 'temp.md')
    shutil.rmtree(f'./{target_directory}')
    time.sleep(2)
    os.mkdir(target_directory)
    shutil.move('temp.md', f'{readme}')


def minify_source_directory_into_target_directory(slash, source_directory, target_directory):
    valid_files       = []
    local_directories = set()

    for root, _, files in os.walk(os.path.abspath(f'./{source_directory}')):
        for file in files:
            filepath = os.path.join(root, file).split(source_directory)[1]
            local_directory = root.split(source_directory)[1]
            if local_directory: local_directories.add(local_directory) # tryuthy check skips adding an empty string '' to local_directories for files that are in root of source_directory
            if filepath.endswith('DS_Store'): continue
            if '__pycache__' in filepath:     continue
            valid_files.append(filepath)
    for local_directory in local_directories:
        os.makedirs(f'{target_directory}{local_directory}', exist_ok=True) # since sets are unordered, we might create a nested directory before the outer directory, so the exist_ok argument=True avoids this error -> FileExistsError: [Errno 17] File exists: '{local_directory}' (which is an outer directory for a nested directory that we made in the process of making a nested directory)
    for file in valid_files:
        with open(f'{source_directory}{slash}{file}', 'r') as read_file, open(f'{target_directory}{slash}{file}', 'w') as write_file:
            if '__init__.py' in file:
                write_file.write(read_file.read())
                continue
            formatted = read_file.read()
            formatted = re.sub(r' +# .+', '', formatted)
            formatted = re.sub(r' +\n', '',  formatted)
            formatted = re.sub(r'^\n', '',   formatted, flags=re.MULTILINE)
            if 'notifications.py' not in file and 'write.py' not in file: formatted = re.sub(r'    ', ' ', formatted)
            write_file.write(formatted)


def main():
    slash            = determine_path_slash()
    source_directory = 'dev'
    target_directory = 'yt_videos_list'

    clear_target_directory(target_directory)
    minify_source_directory_into_target_directory(slash, source_directory, target_directory)


if __name__ == '__main__':
    main()
