import threading
import datetime
def log(message, logging_output_location):
 thread_name = threading.current_thread().name
 thread_name = f'[{threading.current_thread().name}]'
 isoformat   = datetime.datetime.isoformat
 now   = datetime.datetime.now
 message  = f'===>{thread_name:>>14} {isoformat(now())}: {message}\n'
 logging_output_location.writelines(message)
