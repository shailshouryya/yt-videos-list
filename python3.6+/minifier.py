import os
import re


def main():
    valid_files       = []
    for root, dirs, files in os.walk(os.path.abspath("./yt_videos_list/")):
        for file in files:
            filepath = os.path.join(root, file).split('yt_videos_list')[2]
            if filepath.endswith('DS_Store'): continue
            valid_files.append(filepath)
    for file in valid_files:
        with open(f'yt_videos_list/{file}', 'r') as read_file, open(f'ship{file}', 'w') as write_file:
            print(file)

    print(valid_files)
if __name__ == '__main__':
    main()
