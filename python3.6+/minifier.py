import os
import re
import time
import shutil


def main():
    try:
        shutil.move('yt_videos_list/README.md', 'temp.md')
        shutil.rmtree('./yt_videos_list')
        time.sleep(2)
    except: print('The directory "./ship" does not exist')
    os.mkdir('yt_videos_list')
    os.mkdir('yt_videos_list/download')
    os.mkdir('yt_videos_list/file')
    shutil.move('temp.md', 'yt_videos_list/README.md')
    valid_files = []
    for root, _, files in os.walk(os.path.abspath("./dev/")):
        for file in files:
            filepath = os.path.join(root, file).split('dev')[1]
            if filepath.endswith('DS_Store'): continue
            if '__pycache__' in filepath:     continue
            valid_files.append(filepath)
    for file in valid_files:
        with open(f'dev/{file}', 'r') as read_file, open(f'yt_videos_list{file}', 'w') as write_file:
            if file.split('/')[-1] == '__init__.py':
                write_file.write(read_file.read())
                continue
            formatted = read_file.read()
            formatted = re.sub(r' +# .+', '', formatted)
            formatted = re.sub(r' +\n', '',  formatted)
            if file.split('/')[-1] != 'notifications.py' and file.split('/')[-1] != 'write.py': formatted = re.sub(r'    ', ' ', formatted)
            formatted = re.sub(r'^\n', '',   formatted, flags=re.MULTILINE)
            write_file.write(formatted)

if __name__ == '__main__':
    main()
