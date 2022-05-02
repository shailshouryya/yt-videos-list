import functools
import threading
import datetime
import time
import os

NEWLINE = '\n'

def log(message, logging_locations):
    thread_name       = f'[{threading.current_thread().name}]'
    current_time      = datetime.datetime.now().isoformat()
    utc_offset        = time.strftime('%z')
    formatted_message = f'{current_time}{utc_offset} {thread_name:>12} {message}\n'
    for location in logging_locations:
        location.write(formatted_message)


def log_time_taken(cpu_start_time, real_start_time, first_part_of_message, last_part_of_message, logging_locations):
    cpu_end_time  = time.perf_counter()
    real_end_time = time.time()
    cpu_time      = cpu_end_time - cpu_start_time
    real_time     = real_end_time - real_start_time
    log(f'{first_part_of_message}{cpu_time} seconds ({real_time} seconds real time){last_part_of_message}', logging_locations)


def log_write_information(writer_function):
    @functools.wraps(writer_function)
    def wrap_writer_function(*args, **kwargs):
        function_name                                                                         = writer_function.__name__
        function_cpu_start_time                                                               = time.perf_counter()
        function_real_start_time                                                              = time.time()
        extension                                                                             = args[0] # file_type
        timestamp                                                                             = args[5] # timestamp (determined by the now() function in program.py)
        file_name, new_videos_written, total_videos, reverse_chronological, logging_locations = writer_function(*args, **kwargs)   # writer_function() writes to temp_{file_name}
        if new_videos_written == 1: videos = 'video'
        else:                       videos = 'videos'
        function_cpu_end_time    = time.perf_counter()
        function_real_end_time   = time.time()
        function_cpu_time        = function_cpu_end_time - function_cpu_start_time
        function_real_time       = function_real_end_time - function_real_start_time
        temp_file  = f'temp_{file_name}_{timestamp}.{extension}'    # determine temp_{file_name} for wrap_writer_function() scope (writer_function defines it in its own scope already)
        final_file = f'{file_name}.{extension}'
        padding    = 39
        log('Finished writing to'.ljust(padding) + f'{temp_file}',                                                                    logging_locations)
        if function_name == 'create_file': log(f'{new_videos_written} {videos} written to'.ljust(padding)           + f'{temp_file}', logging_locations)
        if function_name == 'update_file': log(f'{new_videos_written} ***NEW*** {videos} written to'.ljust(padding) + f'{temp_file}', logging_locations)
        log('Closing'.ljust(padding) + f'{temp_file}',                                                                                logging_locations)
        log(f'Successfully completed write, renaming {temp_file} to {final_file}',                                                    logging_locations)
        if function_name == 'update_file' and not reverse_chronological: # ChannelName_chronological.ext files
            # if the function that ran was update_file with the reverse_chronological flag set to False: remove temp_{file_name} since all new information from the temp file was appended to the end of the original file (new data is at bottom of file)
            os.remove(temp_file)
        else:
            # if the function that ran was create_file: rename temp_{file_name} to {file_name}.{extension} here AFTER everything else finishes to ensure atomicity
            # if the function that ran was update_file with the reverse_chronological flag set to True: rename temp_{file_name} to {file_name}.{extension} since program appends old info from the original file to the end of new data in the temp file
            os.replace(temp_file, final_file)
        log('Successfully renamed'.ljust(padding) + f'{temp_file} to {final_file}',                                                                                   logging_locations)
        if function_name == 'create_file': log(f'It took {function_cpu_time} seconds ({function_real_time} seconds real time)) to write all {new_videos_written} {videos} to {final_file}',                            logging_locations)
        if function_name == 'update_file': log(f'It took {function_cpu_time} seconds ({function_real_time} seconds real time)) to write the {new_videos_written} ***NEW*** {videos} to the pre-existing {final_file}', logging_locations)
        log(f'{final_file} now contains information for {total_videos} {videos}{NEWLINE}',                                                                            logging_locations)
    return wrap_writer_function
