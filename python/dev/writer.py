import csv
import re
import os

from .custom_logger import log, log_write_information
from .scroller      import store_already_written_videos


padding = 39


@log_write_information
def create_file(file_type, file_name, file_buffering, newline, csv_writer, timestamp, logging_locations, identifier, reverse_chronological, video_data):
    temp_file_name = f'temp_{file_name}_{timestamp}.{file_type}'
    with open(temp_file_name, mode='w', newline=newline, encoding='utf-8',  buffering=file_buffering) as temp_file:
        if file_type == 'csv':
            fieldnames = ['Video Number', 'Video Title', 'Video Duration', identifier, 'Watched', 'Watch again later', 'Notes']
            csv_writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        new_videos = total_videos = len(video_data)
        create_entries(file_type, temp_file, csv_writer, logging_locations, identifier, video_data, reverse_chronological, total_videos, number_of_existing_videos=0, file_visited_videos=set())
    log('Closing'.ljust(padding) + f'{temp_file_name}', logging_locations)
    videos = format_video_plurality(new_videos)
    log('Finished writing to'.ljust(padding)               + f'{temp_file_name}', logging_locations)
    log(f'{new_videos} {videos} written to'.ljust(padding) + f'{temp_file_name}', logging_locations)
    # rename temp_{file_name} to {file_name}.{extension} here AFTER everything else finishes to ensure atomicity
    final_file_name = f'{file_name}.{file_type}'
    log(f'Successfully completed write, renaming {temp_file_name} to {final_file_name}', logging_locations)
    os.replace(temp_file_name, final_file_name)
    log('Successfully renamed'.ljust(padding) + f'{temp_file_name} to {final_file_name}', logging_locations)
    return file_name, new_videos, total_videos, reverse_chronological, logging_locations



# write the information for all new videos to a temp file, then
#     write the contents from the pre-existing file TO the end of the TEMP file when reverse_chronological=True
#     write the contents from the temp file TO the end of the PRE-EXISTING file when reverse chronological=False

@log_write_information
def update_file(file_type, file_name, file_buffering, newline, csv_writer, timestamp, logging_locations, identifier, reverse_chronological, video_data, file_visited_videos, video_id_only):
    if not file_visited_videos: file_visited_videos = store_already_written_videos(file_name, file_type)
    file_visited_videos                             = format_visited_videos_for_id(file_visited_videos, video_id_only, logging_locations)
    temp_file_name = f'temp_{file_name}_{timestamp}.{file_type}'
    original_file_name = f'{file_name}.{file_type}'
    with open(original_file_name, mode='r+', newline=newline, encoding='utf-8',  buffering=file_buffering) as old_file, open(temp_file_name, mode='w+', newline=newline, encoding='utf-8',  buffering=file_buffering) as temp_file:
        if file_type == 'csv':
            number_of_existing_videos = int(max(re.findall('^(\d+)?,', old_file.read(), re.M), key=lambda i: int(i)))
            fieldnames                = ['Video Number', 'Video Title', 'Video Duration', identifier, 'Watched', 'Watch again later', 'Notes']
            csv_writer                = csv.DictWriter(temp_file, fieldnames=fieldnames)
            if reverse_chronological: csv_writer.writeheader() # only write header when reverse_chronological=True since the pre-existing csv file will already contain the header when reverse_chronological=False (and the new videos will be added to the bottom of the pre-existing file)
        else:
            number_of_existing_videos = int(max(re.findall('^(?:### )?Video Number:\s*(\d+)', old_file.read(), re.M), key=lambda i: int(i)))
        new_videos   = find_number_of_new_videos(video_data, file_visited_videos)
        total_videos = number_of_existing_videos + new_videos
        videos       = format_video_plurality(new_videos)
        if new_videos != 0:
            create_entries(file_type, temp_file, csv_writer, logging_locations, identifier, video_data, reverse_chronological, total_videos, number_of_existing_videos, file_visited_videos)
            log('Finished writing to'.ljust(padding)                         + f'{temp_file_name}', logging_locations)
            log(f'{new_videos} ***NEW*** {videos} written to'.ljust(padding) + f'{temp_file_name}', logging_locations)
            if reverse_chronological:
                old_file.seek(0)
                if file_type == 'csv': old_file.readline()         # skip the header since the header is already written at the top of temp file, and the contents of the pre-existing file are added to the END of the temp file
                for line in old_file:  temp_file.write(line)
            else:
                temp_file.seek(0)                                  # no need to skip the first line for csv files since csv header only written when reverse_chronological=True
                for line in temp_file: old_file.write(line)
    log('Closing'.ljust(padding) + f'{temp_file_name}', logging_locations)
    if not reverse_chronological or (reverse_chronological and new_videos == 0):
        # if the reverse_chronological flag was set to True BUT no new videos were found: remove temp_{file_name} since
        #   the original ChannelName_reverse_chronological.ext file stayed the same ahd no new information was written to the temp file
        #     this is an **important detail** since when the reverse_chronological flag is set to True, the program writes the new information to the temp file and then
        #     appends the original file contents to the end of the temp file, so removing the temp file would normally lose the new information since the new video data
        #     only gets written to the temp file - when there is no new video data, though, this is fine since there is no new data
        # if the reverse_chronological flag was set to False: remove temp_{file_name} since
        #   if new data was found:    all new information from the temp file was appended to the end of the original ChannelName_chronological.ext file (new data is at bottom of file)
        #   if no new data was found: the original file stayed the same
        os.remove(temp_file_name)
    else:
        # if the reverse_chronological flag was set to True: rename temp_{file_name} to {file_name}.{extension} since program appends old info from the original file to the end of new data in the temp file
        log(f'Successfully completed write, renaming {temp_file_name} to {original_file_name}', logging_locations)
        os.replace(temp_file_name, original_file_name)
        log('Successfully renamed'.ljust(padding) + f'{temp_file_name} to {original_file_name}', logging_locations)
    return file_name, new_videos, total_videos, reverse_chronological, logging_locations

def format_visited_videos_for_id(file_visited_videos, video_id_only, logging_locations):
    if video_id_only is True:
        log('Updating set to keep only the video ID from the full video URL...', logging_locations)
        formatted_visited_videos = set()
        while file_visited_videos:
            full_url       = file_visited_videos.pop()
            video_id       = full_url.split('watch?v=')[1]
            formatted_visited_videos.add(video_id)
        log('Finished formatting the video IDs in the set...\n', logging_locations)
        file_visited_videos = formatted_visited_videos
    return file_visited_videos

def find_number_of_new_videos(video_data, file_visited_videos):
    visited_on_page = {video[3] for video in video_data}                       # set comprehension
    return len(visited_on_page.difference(file_visited_videos))                # same as len(visited_on_page - file_visited_videos)



def create_entries(file_type, new_file, csv_writer, logging_locations, identifier, video_data, reverse_chronological, total_videos, number_of_existing_videos, file_visited_videos):
    if reverse_chronological is True:
        video_number = total_videos
        incrementer  = -1
    else:
        video_number = number_of_existing_videos + 1
        incrementer  = 1
    total_writes = 0
    new          = ' new ' if number_of_existing_videos > 0 else ' '
    writer = csv_writer if file_type == 'csv' else new_file
    for video_datum in video_data:
        # do NOT use video_number from video_datum since video number is based on number of extracted videos,
        # NOT the offset number based on the number of videos already in the file
        # NOTE that the video_datum[0] element will contain the correct video number for newly created files
        # BUT the incrementer method used below allows this function to work for both new AND pre-existing files
        _, video_title, video_duration, video_url = video_datum
        if video_url in file_visited_videos:
            continue
        create_row(file_type, writer, video_number, video_title, video_duration, video_url, identifier)
        video_number += incrementer
        total_writes += 1
        if total_writes % 250 == 0:
            log(f'{total_writes}{new}videos written to {new_file.name}...', logging_locations)

def create_row(file_type, writer, video_number, video_title, video_duration, video_url, identifier):
    if file_type == 'csv':
        writer.writerow(
            {
                'Video Number':      f'{video_number}',
                'Video Title':       f'{video_title}',
                'Video Duration':    f'{video_duration}',
                identifier:          f'{video_url}',
                'Watched':           '',
                'Watch again later': '',
                'Notes':              ''
            }
        )
    else:
        newline  = '\n'
        markdown = file_type == 'md'
        def ljust(text):
            if markdown:
                prefix  = '### '
                padding = 24
            else:
                prefix  = ''
                padding = 19
            return f'{prefix}{text}'.ljust(padding)
        if markdown:
            writer.write(f'## {video_title}{newline}')
            writer.write(f'{ljust("Video Number:")}{video_number}{newline}')
        else:
            writer.write(f'{ljust("Video Number:")}{video_number}{newline}')
            writer.write(f'{ljust("Video Title:")}{video_title}{newline}')
        writer.write(f'{ljust("Video Duration:")}{video_duration}{newline}')
        writer.write(f'{ljust(identifier + ":")}{video_url}{newline}')
        writer.write(f'{ljust("Watched:")}{newline}')
        writer.write(f'{ljust("Watch again later:")}{newline}')
        writer.write(f'{ljust("Notes:")}{newline}')
        writer.write('*'*75 + newline)
        if markdown: writer.write('\n')


def format_video_plurality(new_videos_written):
    if new_videos_written == 1: return 'video'
    else:                       return 'videos'
