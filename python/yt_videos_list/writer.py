import csv
import re
from .custom_logger import log, log_write_information
from .scroller      import store_already_written_videos
@log_write_information
def create_file(file_type, file_name, file_buffering, newline, csv_writer, timestamp, logging_locations, identifier, reverse_chronological, video_data):
    with open(f'temp_{file_name}_{timestamp}.{file_type}', mode='w', newline=newline, encoding='utf-8',  buffering=file_buffering) as temp_file:
        if file_type == 'csv':
            fieldnames = ['Video Number', 'Video Title', 'Video Duration', identifier, 'Watched', 'Watch again later', 'Notes']
            csv_writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        new_videos = total_videos = len(video_data)
        create_entries(file_type, temp_file, csv_writer, logging_locations, identifier, video_data, reverse_chronological, total_videos, number_of_existing_videos=0, file_visited_videos=set())
    return file_name, new_videos, total_videos, reverse_chronological, logging_locations
@log_write_information
def update_file(file_type, file_name, file_buffering, newline, csv_writer, timestamp, logging_locations, identifier, reverse_chronological, video_data, file_visited_videos, video_id_only):
    if not file_visited_videos: file_visited_videos = store_already_written_videos(file_name, file_type)
    file_visited_videos = format_visited_videos_for_id(file_visited_videos, video_id_only, logging_locations)
    with open(f'{file_name}.{file_type}', mode='r+', newline=newline, encoding='utf-8',  buffering=file_buffering) as old_file, open(f'temp_{file_name}_{timestamp}.{file_type}', mode='w+', newline=newline, encoding='utf-8',  buffering=file_buffering) as temp_file:
        if file_type == 'csv':
            number_of_existing_videos = int(max(re.findall('^(\d+)?,', old_file.read(), re.M), key=lambda i: int(i)))
            fieldnames                = ['Video Number', 'Video Title', 'Video Duration', identifier, 'Watched', 'Watch again later', 'Notes']
            csv_writer                = csv.DictWriter(temp_file, fieldnames=fieldnames)
            if reverse_chronological: csv_writer.writeheader()
        else:
            number_of_existing_videos = int(max(re.findall('^(?:### )?Video Number:\s*(\d+)', old_file.read(), re.M), key=lambda i: int(i)))
        new_videos   = find_number_of_new_videos(video_data, file_visited_videos)
        total_videos = number_of_existing_videos + new_videos
        create_entries(file_type, temp_file, csv_writer, logging_locations, identifier, video_data, reverse_chronological, total_videos, number_of_existing_videos, file_visited_videos)
        if reverse_chronological:
            old_file.seek(0)
            if file_type == 'csv': old_file.readline()
            for line in old_file:  temp_file.write(line)
        else:
            temp_file.seek(0)
            for line in temp_file: old_file.write(line)
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
    visited_on_page = {video[3] for video in video_data}
    return len(visited_on_page.difference(file_visited_videos))
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
