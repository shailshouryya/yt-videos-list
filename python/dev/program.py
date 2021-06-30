import os
import datetime
import threading

from .              import scroller, writer
from .notifications import Common
from .custom_logger import log


def determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name, txt, csv, markdown, logging_locations, verify_page_bottom_n_times):
    common_message = Common()
    txt_exists = os.path.isfile(f'{file_name}.txt') if txt      else False # only check if file exists if program was specified to extract info into txt file, otherwise set to False regardless of whether a txt file already exists or not
    csv_exists = os.path.isfile(f'{file_name}.csv') if csv      else False # only check if file exists if program was specified to extract info into csv file, otherwise set to False regardless of whether a csv file already exists or not
    md_exists  = os.path.isfile(f'{file_name}.md')  if markdown else False # only check if file exists if program was specified to extract info into md  file, otherwise set to False regardless of whether a md  file already exists or not
    txt_videos = None
    csv_videos = None
    md_videos  = None
    current_condition = (txt, txt_exists, csv, csv_exists, markdown, md_exists)
    update_conditions = set(
        (
            (True,  True,  True,  True,  True,  True),   # update txt,        txt exists,   update csv,        csv exists, update md,        md exists
            (True,  True,  True,  True,  False, False),  # update txt,        txt exists,   update csv,        csv exists, do not update md, md DNE
            (True,  True,  False, False, True,  True),   # update txt,        txt exists,   do not update csv, csv DNE,    update md,        md exists
            (False, False, True,  True,  True,  True),   # do not update txt, txt DNE,      update csv,        csv exists, update md,        md exists
            (True,  True,  False, False, False, False),  # update txt,        txt exists,   do not update csv, csv DNE,    do not update md, md DNE
            (False, False, False, False, True,  True),   # do not update txt, txt DNE,      do not update csv, csv DNE,    update md,        md exists
            (False, False, True,  True,  False, False),  # do not update txt, txt DNE,      update csv,        csv exists, do not update md, md DNE
        )
    )
    if current_condition in update_conditions: videos_list, txt_videos, csv_videos, md_videos = scroller.scroll_to_old_videos(url, driver, scroll_pause_time, logging_locations, file_name, txt_exists, csv_exists, md_exists)
    else:                                      videos_list                                    = scroller.scroll_to_bottom    (url, driver, scroll_pause_time, logging_locations, verify_page_bottom_n_times)
    if len(videos_list) == 0:
        log(common_message.no_videos_found, logging_locations)
        return
    use_threads = (int(txt) + int(csv) + int(markdown)) > 1
    if use_threads:
        # ===> See commit 58c5faba14da25b89e104a50d380489a30d8df71 for more details about using threads for file I/O <===
        # The program needs to write to 2 or more files, so creating a new thread to perform file I/O for each file
        # will speed up the program.
        #
        # This is **probably** due to reduced memory lookups since most lookups for the writes will be near the same areas,
        # because all the file I/O threads will access the video information stored in memory in the same order,
        # as opposed to the MainThread writing to 1 file and going through all the memory locations for the video information for that file,
        # then RESTARTING at the beginning of the stored memory to save the video information to the next file.
        threads = []
        if txt:
            if txt_exists: txt_thread = threading.Thread(target=writer.update_file, args=('txt', videos_list, file_name, reverse_chronological, logging_locations), kwargs={'timestamp': now(), 'stored_in_file': txt_videos})
            else:          txt_thread = threading.Thread(target=writer.create_file, args=('txt', videos_list, file_name, reverse_chronological, logging_locations), kwargs={'timestamp': now()})
            txt_thread.start()
            threads.append(txt_thread)
        if csv:
            if csv_exists: csv_thread = threading.Thread(target=writer.update_file, args=('csv', videos_list, file_name, reverse_chronological, logging_locations), kwargs={'timestamp': now(), 'stored_in_file': csv_videos})
            else:          csv_thread = threading.Thread(target=writer.create_file, args=('csv', videos_list, file_name, reverse_chronological, logging_locations), kwargs={'timestamp': now()})
            csv_thread.start()
            threads.append(csv_thread)
        if markdown:
            if md_exists:  md_thread = threading.Thread(target=writer.update_file, args=('md', videos_list, file_name, reverse_chronological, logging_locations), kwargs={'timestamp': now(), 'stored_in_file': md_videos})
            else:          md_thread = threading.Thread(target=writer.create_file, args=('md', videos_list, file_name, reverse_chronological, logging_locations), kwargs={'timestamp': now()})
            md_thread.start()
            threads.append(md_thread)
        for thread in threads:
            thread.join()
    else:
        # The program needs to write to only 1 file, so there's no need to create a new thread to perform file I/O
        # since there will be nothing else to run concurrently with this new subthread. If anything, creating a new thread for only
        # 1 file I/O operation might slow the program down, since the program needs to manage the work of the subthread that
        # the MainThread could be doing.
        if txt:
            if txt_exists: writer.update_file('txt', videos_list, file_name, reverse_chronological, logging_locations, timestamp=now(), stored_in_file=txt_videos)
            else:          writer.create_file('txt', videos_list, file_name, reverse_chronological, logging_locations, timestamp=now())
        if csv:
            if csv_exists: writer.update_file('csv', videos_list, file_name, reverse_chronological, logging_locations, timestamp=now(), stored_in_file=csv_videos)
            else:          writer.create_file('csv', videos_list, file_name, reverse_chronological, logging_locations, timestamp=now())
        if markdown:
            if md_exists:  writer.update_file('md', videos_list, file_name, reverse_chronological, logging_locations, timestamp=now(), stored_in_file=md_videos)
            else:          writer.create_file('md', videos_list, file_name, reverse_chronological, logging_locations, timestamp=now())

def now():
    return datetime.datetime.now().isoformat().replace(':', '_').replace('.', '-')
