import time

def check_import_time():
    start = time.time()
    from yt_videos_list import ListCreator
    end = time.time()
    print(f'Took {end-start} seconds to import ListCreator')

check_import_time()
