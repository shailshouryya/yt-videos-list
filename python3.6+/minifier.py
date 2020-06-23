import os
import re
import time
import shutil

from tests.test_shared import determine_path_slash


def main():
    slash            = determine_path_slash()
    source_directory = 'dev'
    target_directory = 'yt_videos_list'
    readme           = f'./{target_directory}/README.md'
    shutil.move  (f'{readme}', 'temp.md')
    shutil.rmtree(f'./{target_directory}')
    time.sleep(2)
    os.mkdir(target_directory)
    os.mkdir('yt_videos_list/download')
    os.mkdir('yt_videos_list/file')
    shutil.move('temp.md', f'{readme}')
    valid_files      = []
    for root, _, files in os.walk(os.path.abspath(f'./{source_directory}')):
        for file in files:
            filepath = os.path.join(root, file).split(source_directory)[1]
            if filepath.endswith('DS_Store'): continue
            if '__pycache__' in filepath:     continue
            valid_files.append(filepath)
    for file in valid_files:
        with open(f'{source_directory}{slash}{file}', 'r') as read_file, open(f'{target_directory}{slash}{file}', 'w') as write_file:
            if '__init__.py' in file:
                write_file.write(read_file.read())
                continue
            formatted = read_file.read()
            formatted = re.sub(r' +# .+', '', formatted)
            formatted = re.sub(r' +\n', '',  formatted)
            if 'notifications.py' not in file and 'write.py' not in file: formatted = re.sub(r'    ', ' ', formatted)
            formatted = re.sub(r'^\n', '',   formatted, flags=re.MULTILINE)
            write_file.write(formatted)

if __name__ == '__main__':
    main()
