import functools
import threading
import datetime
import time

from io import (
    TextIOWrapper,
)
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Set,
    TextIO,
    Tuple,
)

NEWLINE = '\n'

def log(
    message: str,
    logging_locations: Tuple[TextIOWrapper] | Tuple[TextIOWrapper, TextIO],
) -> None:
    thread_name       = f'[{threading.current_thread().name}]'
    current_time      = datetime.datetime.now().isoformat()
    utc_offset        = time.strftime('%z')
    formatted_message = f'{current_time}{utc_offset} {thread_name:>12} {message}\n'
    for location in logging_locations:
        location.write(formatted_message)


def log_time_taken(
    cpu_start_time: float,
    real_start_time: float,
    first_part_of_message: str,
    last_part_of_message: str,
    logging_locations: Tuple[TextIOWrapper] | Tuple[TextIOWrapper, TextIO]
) -> None:
    cpu_end_time  = time.perf_counter()
    real_end_time = time.time()
    cpu_time      = cpu_end_time - cpu_start_time
    real_time     = real_end_time - real_start_time
    log(f'{first_part_of_message}{real_time} time.time() seconds ({cpu_time} time.perf_counter() seconds){last_part_of_message}', logging_locations)


def log_write_information(
    writer_function: Callable[[Any], Any]
) -> Callable[
    [
        Any,
    ], Any
]: # Wrapped[..., Any, (*args: Tuple, **kwargs: Dict), None]
    @functools.wraps(writer_function)
    def wrap_writer_function(
        *args: Tuple[str | None | Tuple[TextIOWrapper] | Tuple[TextIOWrapper, TextIO] | bool | List[int | str] | Set[str]],
        **kwargs: Dict[str, Any],
    ) -> None:
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
        if function_name == 'create_file': log(f'It took {function_real_time} time.time() seconds ({function_cpu_time} time.perf_counter() seconds) to write all {new_videos_written} {videos} to {final_file}',                            logging_locations)
        if function_name == 'update_file': log(f'It took {function_real_time} time.time() seconds ({function_cpu_time} time.perf_counter() seconds) to write the {new_videos_written} ***NEW*** {videos} to the pre-existing {final_file}', logging_locations)
        log(f'{final_file} now contains information for {total_videos} {videos}{NEWLINE}',                                                                            logging_locations)
    return wrap_writer_function
