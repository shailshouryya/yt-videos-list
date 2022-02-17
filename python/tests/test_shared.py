'''
Test module for cross-module logic for running
integration tests for the `yt_videos_list`
package - regardless of the driver
being tested or host operating system.
'''
import os
import sys
import time
import shutil
import hashlib
import datetime
import threading

from determine import determine_path_slash

from save_thread_result import ThreadWithResult

from yt_videos_list import ListCreator


NOW       = datetime.datetime.now
ISOFORMAT = datetime.datetime.isoformat


def run_tests_for(browsers_list):
    '''
    Runs 2 threads simultaneously to test both
    `reverse_chronological` AND `chronological`
    test cases for every driver in the provided
    `browsers_list`.
    '''
    file_content_mismatch = 'At least one output file produced by this test does not match the expectation!'
    test_cases = create_test_cases(browsers_list)
    total      = len(test_cases)
    current    = 0
    log_test_info('*' * 140,        'CoreySchafer_reverse_chronological_videos_list.log', 'CoreySchafer_chronological_videos_list.log', 'CoreySchafer_reverse_chronological_video_ids_list.log', 'CoreySchafer_chronological_video_ids_list.log')
    log_test_info('Running tests!', 'CoreySchafer_reverse_chronological_videos_list.log', 'CoreySchafer_chronological_videos_list.log', 'CoreySchafer_reverse_chronological_video_ids_list.log', 'CoreySchafer_chronological_video_ids_list.log')
    while current < total:
        # each test_case is a ListCreator instance for
        # video_id_only set to True or False with
        # reverse_chronological set to True or False
        # for EACH driver in the browsers_list,
        # and within EACH test case,
        # there are 5 variations to test - see
        # the list object "variations"
        # in verify_update() for more details
        if threading.active_count() - 1 == 0:
            # the main thread counts as a thread, so we
            # need to subtract 1 to determine the
            # number of threads we've created
            # manually
            thread_1_case      = test_cases[current]
            is_id = '_id' if getattr(thread_1_case, 'video_id_only') is True else ''
            if getattr(thread_1_case, 'reverse_chronological') is True: log_1_name = f'CoreySchafer_reverse_chronological_video{is_id}s_list.log'
            else:                                                       log_1_name = f'CoreySchafer_chronological_video{is_id}s_list.log'
            test_case_thread_1 = ThreadWithResult(target=run_test_case, args=(thread_1_case, log_1_name))
            log_test_info('Starting thread for test case 1...', log_1_name)
            test_case_thread_1.start()
            log_test_info('Started thread for test case 1!', log_1_name)
            current += 1
            # safaridriver does not allow multi-threading:
            # Could not create a session: The Safari instance is already paired with another WebDriver session.
            if 'safari' not in browsers_list:
                if current == 1:
                    # wait 5 seconds to allow all just the firefox selenium webdriver dependency to download (necessary after test_cross_platforms module runs remove_dependencies())
                    time.sleep(5)
                thread_2_case      = test_cases[current]
                is_id = '_id' if getattr(thread_2_case, 'video_id_only') is True else ''
                if getattr(thread_2_case, 'reverse_chronological') is True: log_2_name = f'CoreySchafer_reverse_chronological_video{is_id}s_list.log'
                else:                                                       log_2_name = f'CoreySchafer_chronological_video{is_id}s_list.log'
                test_case_thread_2 = ThreadWithResult(target=run_test_case, args=(thread_2_case, log_2_name))
                log_test_info('Starting thread for test case 2...', log_2_name)
                test_case_thread_2.start()
                log_test_info('Started thread for test case 2!', log_2_name)
                current += 1
        while threading.active_count() - 1 != 0 and current < total:
            # the threads are still running
            time.sleep(7)
        if 'test_case_thread_1' in locals(): test_case_thread_1.join()
        if 'test_case_thread_2' in locals(): test_case_thread_2.join()
        if 'thread_1_case' in locals(): log_test_info(f'Finished testing {[thread_1_case]}!', log_1_name)
        if 'thread_2_case' in locals(): log_test_info(f'Finished testing {[thread_2_case]}!', log_2_name)
        if 'test_case_thread_1' in locals() and (getattr(test_case_thread_1, 'result', None) is None or test_case_thread_1.result == 'Failed!'): raise ValueError(file_content_mismatch)
        if 'test_case_thread_2' in locals() and (getattr(test_case_thread_2, 'result', None) is None or test_case_thread_2.result == 'Failed!'): raise ValueError(file_content_mismatch)
        test_case_complete = 'Moving on to the next driver...\n' + '⏬ '*11 + '\n\n\n'
        if   'thread_1_case' in locals() and 'thread_2_case' in locals(): log_test_info(test_case_complete, log_1_name, log_2_name)
        elif 'thread_1_case' in locals():                                 log_test_info(test_case_complete, log_1_name)
        elif 'thread_2_case' in locals():                                 log_test_info(test_case_complete, log_2_name)


def log_test_info(message, *args):
    thread_name  = f'[{threading.current_thread().name}]'
    current_time = datetime.datetime.now().isoformat()
    utc_offset   = time.strftime('%z')
    message      = f'{current_time}{utc_offset} {thread_name:>12} {message}\n'
    sys.stdout.writelines(message)
    for log_file in args:
        with open(log_file, mode='a', encoding='utf-8') as output_location:
            output_location.writelines(message)


def create_test_cases(browsers):
    '''
    Creates an instance of `ListCreator` for a
    video_id_only=True and video_id_only=False for a
    reverse chronological AND chronological test case
    for each driver in the provided `browsers` list.
    '''
    return [
        ListCreator(driver=browser, reverse_chronological=is_reverse_chronological, video_id_only=is_video_id_only)
        for browser in browsers
        for is_video_id_only         in [True, False]
        for is_reverse_chronological in [True, False]
    ]


def run_test_case(list_creator, log_file):
    '''
    Calls `verify_update()`, which
    runs all variations (no pre-existing files,
    pre-existing txt, pre-existing csv, pre-existing md, and
    pre-existing txt + csv + md files) of the provided test case
    (a specific driver for the `video_id_only` attribute set to `True` or `False`
    with the `reverse_chronological` attribute
    set to either `True` or `False`) using the
    `list_creator.create_list_for()` method and verifies resulting
    output files match the content in the corresponding full
    reference files.
    '''
    path_slash               = determine_path_slash()
    test_url                 = 'youtube.com/user/schafer5'
    is_reverse_chronological = getattr(list_creator, 'reverse_chronological')
    is_video_id_only         = getattr(list_creator, 'video_id_only')
    is_id  = '_id'                                       if is_video_id_only         else  ''
    suffix = f'reverse_chronological_video{is_id}s_list' if is_reverse_chronological else f'chronological_video{is_id}s_list'
    partialfile_path = f'tests{path_slash}reference_files{path_slash}partial_CoreySchafer_{suffix}'
    fullfile_path    = f'tests{path_slash}reference_files{path_slash}full_CoreySchafer_{suffix}'
    return verify_update(list_creator, test_url, partialfile_path, fullfile_path, log_file)


def verify_update(list_creator, test_url, test_file, full_file, log_file):
    '''
    Uses the `reverse_chronological` and `video_id_only` attributes of the `list_creator`
    argument to determine the suffix, then uses the reference
    `test_file` to create a partial test file. Runs the
    `create_list_for(test_url)` method on the provided
    `list_creator` instance. Calls
    `compare_test_files_to_reference_files(full_file, file_name)`
    to ensure content in the created output files match the
    content in the full reference files.
    '''
    variations = [
        ['csv', 'txt', 'md'],
        [],
        ['csv'],
        ['txt'],
        ['md']
        ]
    for variation in variations:
        is_video_id_only         = vars   (list_creator)["video_id_only"]
        is_reverse_chronological = vars   (list_creator)['reverse_chronological']
        driver_name              = getattr(list_creator, 'driver')
        log_test_info(f'TESTING list_creator.video_id_only={is_video_id_only}, list_creator.reverse_chronological={is_reverse_chronological} for {driver_name}driver', log_file)
        log_test_info(f'Full configuration: {repr(list_creator)}', log_file)
        is_id  = '_id'                                       if is_video_id_only         else  ''
        suffix = f'reverse_chronological_video{is_id}s_list' if is_reverse_chronological else f'chronological_video{is_id}s_list'
        use_partial_files(variation, test_file, suffix, log_file) # the file this function creates should be the SAME as the returned string to the file_name variable in the next line
        test_output_file = list_creator.create_list_for(test_url, log_silently=True)[1][1]
        # verify calling the create_list_for() method updates the partial file properly
        failed = compare_test_files_to_reference_files(full_file, test_output_file, log_file)
        if failed == 'Failed!':
            return 'Failed!'
    return 'Passed!'

def use_partial_files(types_of_partial_files, test_file, suffix, log_file):
    '''
    Removes all pre-existing files with the corresponding `suffix`
    for the file extensions in the `types_of_partial_files` tuple
    (`reverse_chronological_video[_id]s_list`
    or
    `chronological_video[_id]s_list`;
    the prefix in all cases is `CoreySchafer_`), then creates a
    partial file for the file extensions in the
    `types_of_partial_files` tuple
    using the `partial_CoreySchafer_{suffix}.{extension}`
    reference file(s).
    '''
    log_test_info(f'TESTING with pre-existing files containing the following extensions: {types_of_partial_files}....\n', log_file)
    delete_all_test_output_files_with_suffix(suffix)
    for extension in types_of_partial_files:
        create_partial_file(test_file, suffix, extension)

def delete_all_test_output_files_with_suffix(suffix):
    '''
    Deletes all files containing the corresponding suffix to ensure
    tests return valid results not skewed by any pre-existing files.
    The `delete_file(filepath, extension)` helper function deletes
    pre-existing files with the specified extension. The `suffix`
    used to create `filepath` includes
    `reverse_chronological_video[_id]s_list` and `chronological_video[_id]s_list`
    and the extensions include `txt`, `csv`, and `md`. The prefix in
    all cases is `CoreySchafer_`
    '''
    test_output_file = f'CoreySchafer_{suffix}'
    delete_file(test_output_file, 'txt')
    delete_file(test_output_file, 'csv')
    delete_file(test_output_file, 'md' )

def delete_file(filepath, extension):
    '''
    Removes the file {filepath}.{extension} if it exists.
    '''
    if os.path.exists(f'{filepath}.{extension}'):
        os.remove(f'{filepath}.{extension}')

def create_partial_file(test_file, suffix, extension):
    '''
    Creates a partial file using `{test_file}.{extension}`
    as the reference file and renames it to
    `CoreySchafer_{suffix}.{extension}`.
    '''
    shutil.copy(f'{test_file}.{extension}', f'CoreySchafer_{suffix}.{extension}')


def compare_test_files_to_reference_files(full_file, test_output_file, log_file):
    '''
    Ensures the resulting test output file `test_output_file`
    contains the exact same content as the reference `full_file` by
    comparing the sha256 hash of both files. If the hashes match,
    the tests continue, but if the hashes don't match, the
    program exits by raising the `ValueError` exception in the
    originating `run_tests_for(browsers_list)` function.

    NOTE: on a multi-threaded program, a `ValueError` exception
    (or any other exception) only terminates the thread on which
    the exception is raised, but any other threads will
    continue to execute until they finish. For this reason, the
    `ValueError` exception is raised in the
    `run_tests_for(browsers_list)` function instead of in
    this function, since this function is called from and run from
    a subthread, whereas `run_tests_for(browsers_list)` function
    is called from and run on the MainThread.
    Since the exception is raised in the MainThread, any other
    concurrently running threads will continue to execute until
    they finish, but no FURTHER work will be done after that.
    '''
    with open(f'{test_output_file}.txt', mode='r', encoding='utf-8') as test_txt, open(f'{test_output_file}.csv', mode='r', encoding='utf-8') as test_csv, open(f'{test_output_file}.md', mode='r', encoding='utf-8') as test_md:
        current_txt = hashlib.sha256(test_txt.read().encode('utf-8')).hexdigest()
        current_csv = hashlib.sha256(test_csv.read().encode('utf-8')).hexdigest()
        current_md  = hashlib.sha256(test_md.read().encode ('utf-8')).hexdigest()
    with open(f'{full_file}.txt', mode='r', encoding='utf-8') as full_txt, open(f'{full_file}.csv', mode='r', encoding='utf-8') as full_csv, open(f'{full_file}.md', mode='r', encoding='utf-8') as full_md:
        verified_txt = hashlib.sha256(full_txt.read().encode('utf-8')).hexdigest()
        verified_csv = hashlib.sha256(full_csv.read().encode('utf-8')).hexdigest()
        verified_md  = hashlib.sha256(full_md.read().encode ('utf-8')).hexdigest()
    failed = False
    if current_txt != verified_txt: log_test_info(f'❌ ERROR! The updated txt file does NOT match the {full_file}.txt file!',       log_file); failed = True
    else:                           log_test_info(f'✅ The updated txt file matches the {full_file}.txt file :)',                   log_file)
    if current_csv != verified_csv: log_test_info(f'❌ ERROR! The updated csv file does NOT match the {full_file}.csv file!',       log_file); failed = True
    else:                           log_test_info(f'✅ The updated csv file matches the {full_file}.csv file :)',                   log_file)
    if current_md  != verified_md:  log_test_info(f'❌ ERROR! The updated md  file does NOT match the {full_file}.md  file!\n\n\n', log_file); failed = True
    else:                           log_test_info(f'✅ The updated md  file matches the {full_file}.md  file :)\n\n\n',             log_file)
    if failed:
        log_test_info(f'❗️❗️ FAILED at {ISOFORMAT(NOW())}! ❗️❗️', log_file)
        return 'Failed!'
    return 'Passed!'


def delete_all_test_output_files():
    suffixes = [
        'chronological_videos_list',
        'chronological_video_ids_list',
        'reverse_chronological_videos_list',
        'reverse_chronological_video_ids_list',
    ]
    for suffix in suffixes:
        delete_all_test_output_files_with_suffix(suffix)
