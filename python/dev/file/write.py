import functools
import csv

from ..custom_logger import log, log_extraction_information


def time_writer_function(writer_function):
    @functools.wraps(writer_function)
    def wrapper_timer(*args, **kwargs):
        log_extraction_information(writer_function.__name__, writer_function, args, kwargs)
    return wrapper_timer


@time_writer_function
def create_file(file_type, list_of_videos, file_name, reverse_chronological, logging_locations, timestamp):
    if file_type == 'csv': newline = ''
    else:                  newline = None
    csv_writer = None
    with open(f'temp_{file_name}_{timestamp}.{file_type}', 'w', newline=newline, encoding='utf-8') as temp_file:
        if file_type == 'csv':
            fieldnames = ['Video Number', 'Video Title', 'Video URL', 'Watched?', 'Watch again later?', 'Notes']
            csv_writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        total_videos = create_writer(file_type, temp_file, csv_writer, reverse_chronological, list_of_videos, logging_locations)
    return file_name, total_videos, reverse_chronological, logging_locations

def create_writer(file_type, file, csv_writer, reverse_chronological, list_of_videos, logging_locations):
    total_videos, total_writes, video_number, incrementer = prepare_output(list_of_videos, reverse_chronological)
    for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
        video_number, total_writes = entry(file_type, file, csv_writer, selenium_element, video_number, incrementer, total_writes)
        if total_writes % 250 == 0:
            log(f'{total_writes} videos written to {file.name}...', logging_locations)
    return total_videos

def prepare_output(list_of_videos, reverse_chronological):
    total_videos = len(list_of_videos)
    total_writes = 0
    if reverse_chronological:
        video_number = total_videos
        incrementer  = -1
    else:
        video_number = 1
        incrementer  = 1
    return total_videos, total_writes, video_number, incrementer


def update_status(video_number, total_writes, incrementer):
    video_number += incrementer
    total_writes += 1
    return video_number, total_writes



def entry(file_type, file_object, csv_writer, selenium_element, video_number, incrementer, total_writes):
    if file_type == 'csv': return write_csv (csv_writer,  selenium_element, video_number, incrementer, total_writes)
    else:                  return write_text(file_object, selenium_element, video_number, incrementer, total_writes, file_type)

def write_text(file, selenium_element, video_number, incrementer, total_writes, file_type):
    newline = '\n'
    md      = file_type == 'md'
    if md: spacing = f'{newline}' + '- ' + f'{newline}'
    else:  spacing = f'{newline}' + ' '*4
    if md:
        file.write(f'### Video Title:  {selenium_element.get_attribute("title")}{newline}')
        file.write(f'Video Number: {video_number}{newline}')
    else:
        file.write(f'Video Number: {video_number}{newline}')
        file.write(f'Video Title:  {selenium_element.get_attribute("title")}{newline}')
    file.write(f'Video URL:    {selenium_element.get_attribute("href")}{newline}')
    file.write(f'Watched?{spacing}{newline}')
    file.write(f'Watch again later?{spacing}{newline}')
    file.write(f'Notes:{spacing}{newline}')
    file.write('*'*75 + newline)
    return update_status(video_number, total_writes, incrementer)

def write_csv(writer, selenium_element, video_number, incrementer, total_writes):
    writer.writerow(
        {
            'Video Number':      f'{video_number}',
            'Video Title':       f'{selenium_element.get_attribute("title")}',
            'Video URL':         f'{selenium_element.get_attribute("href")}',
            'Watched?':           '',
            'Watch again later?': '',
            'Notes':              ''
        }
    )
    return update_status(video_number, total_writes, incrementer)
