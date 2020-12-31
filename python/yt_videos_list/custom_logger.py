import threading
import datetime
import time
import os
NEWLINE = '\n'
def log(message, logging_locations):
 thread_name = threading.current_thread().name
 thread_name = f'[{threading.current_thread().name}]'
 isoformat   = datetime.datetime.isoformat
 now   = datetime.datetime.now
 message  = f'===>{thread_name:>>14} {isoformat(now())}: {message}\n'
 for location in logging_locations:
  location.writelines(message)
def log_extraction_information(module, writer_function, args, kwargs):
 start_time                = time.perf_counter()
 extension                 = writer_function.__name__.split('_')[-1]
 timestamp                 = kwargs.get('timestamp', 'undeteremined_start_time')
 file_name, videos_written, reverse_chronological, logging_locations = writer_function(*args, **kwargs)
 if videos_written == 1: videos = 'video'
 else:       videos = 'videos'
 if module.endswith('create_file'): log(f'Opening a temp {extension} file and writing video information to the file....',     logging_locations)
 if module.endswith('update_file'): log(f'Opening a temp {extension} file and writing ***NEW*** video information to the file....', logging_locations)
 end_time   = time.perf_counter()
 total_time = end_time - start_time
 temp_file  = f'temp_{file_name}_{timestamp}.{extension}'
 final_file = f'{file_name}.{extension}'
 log(f'Finished writing to'.ljust(39) + f'{temp_file}',                logging_locations)
 if module.endswith('create_file'): log(f'{videos_written} {videos} written to'.ljust(39) + f'{temp_file}',     logging_locations)
 if module.endswith('update_file'): log(f'{videos_written} ***NEW*** {videos} written to'.ljust(39) + f'{temp_file}', logging_locations)
 log(f'Closing'.ljust(39) + f'{temp_file}',                   logging_locations)
 log(f'Successfully completed write, renaming {temp_file} to {final_file}',           logging_locations)
 if module.endswith('update_file') and not reverse_chronological:
  os.remove(temp_file)
 else:
  os.replace(temp_file, final_file)
 log(f'Successfully renamed'.ljust(39) + f'{temp_file} to {final_file}',                         logging_locations)
 if module.endswith('create_file'): log(f'It took {total_time} seconds to write all {videos_written} {videos} to {final_file}{NEWLINE}',        logging_locations)
 if module.endswith('update_file'): log(f'It took {total_time} seconds to write the {videos_written} ***NEW*** {videos} to the pre-existing {final_file} {NEWLINE}', logging_locations)
