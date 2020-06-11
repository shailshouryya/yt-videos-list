import os
import re
import time
import shutil


def main():
    try: shutil.rmtree('./ship')
    except: print('The directory "./ship" does not exist')
    os.mkdir('ship')
    os.mkdir('ship/download')
    os.mkdir('ship/file')
    valid_files = []
    for root, _, files in os.walk(os.path.abspath("./yt_videos_list/")):
        for file in files:
            filepath = os.path.join(root, file).split('yt_videos_list')[2]
            if filepath.endswith('DS_Store'): continue
            valid_files.append(filepath)
    for file in valid_files:
        with open(f'yt_videos_list/{file}', 'r') as read_file, open(f'ship{file}', 'w') as write_file:
            if file.split('/')[-1] == '__init__.py':
                write_file.write(read_file.read())
                continue
            formatted = read_file.read()
            formatted = re.sub(r'    ', ' ', formatted)
            formatted = re.sub(r'^\n', '',   formatted, flags=re.MULTILINE)
            write_file.write(formatted)

if __name__ == '__main__':
    main()
