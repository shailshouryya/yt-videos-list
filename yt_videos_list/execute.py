import os
import sys
import platform
import time

import selenium
from selenium import webdriver

from . import program
from . import download_dependencies
from .windows import get_drive_letter
from .notifications import Common, ModuleMessage, ScriptMessage


def logic(channel, channel_type, file_name, txt, txt_write_format, csv, csv_write_format, docx, docx_write_format, chronological, headless, scroll_pause_time, user_driver, execution_type):
    common_message = Common()
    module_message = ModuleMessage()
    script_message = ScriptMessage()

    def determine_file_name():
        if file_name is not None:
            return file_name
        else:
            return f'{channel}VideosList'

    def verify_write_format(file_type, write_format, file_name, file_extension):
        def new_write_format():
            user_response = input()
            if 'proceed' in user_response.strip().lower(): return 'w'
            elif 'skip'  in user_response.strip().lower(): return 0
            else:
                print('\n' + common_message.invalid_response)
                common_message.display_file_already_exists_prompt(filename)
                return new_write_format()
        if file_type is True and write_format == 'x':
            filename    = f'{file_name}.{file_extension}'
            file_exists = bool(os.path.isfile(f'./{filename}'))
            if file_exists is True:
                common_message.display_file_already_exists_warning(filename)
                common_message.display_file_already_exists_prompt(filename)
                return new_write_format()
            return 'x'
        else:
            return write_format

    def configure_brave_driver():
        options = webdriver.ChromeOptions()
        if user_os == 'windows':
            drive  = get_drive_letter()
            options.binary_location = rf'{drive}:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
            executable_path         = rf'{drive}:\Windows\bravedriver.exe'
        else:
            options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
            executable_path         = '/usr/local/bin/bravedriver'
        # options.headless = True
        return webdriver.Chrome(options=options, executable_path=executable_path)

    def configure_edge_driver():
        # options = selenium.webdriver.remote.webdriver.WebDriver()
        if user_os == 'windows':
            drive  = get_drive_letter()
            # options.binary_location = rf'{drive}:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
            executable_path         = rf'{drive}:\Windows\msedgedriver.exe'
        else:
            # options.binary_location = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
            executable_path         = '/usr/local/bin/msedgedriver'
            print(common_message.unsupported_edge)
            print(module_message.show_driver_options)
            sys.exit()
        # options.headless = True
        return webdriver.Edge(executable_path=executable_path)


    def check_driver():
        if   'firefox' in user_driver: return webdriver.Firefox
        elif 'opera'   in user_driver: return webdriver.Opera
        elif 'chrome'  in user_driver: return webdriver.Chrome
        elif 'brave'   in user_driver: return configure_brave_driver
        elif 'edge'    in user_driver: return configure_edge_driver
        elif 'safari'  in user_driver:
            if user_os != 'macos':
                common_message.display_dependency_setup_instructions('safari', user_os)
                sys.exit()
            return webdriver.Safari
        else:
            print(common_message.invalid_driver)
            return 'invalid'

    def set_up_headless_firefox_driver():
        options = selenium.webdriver.firefox.options.Options()
        options.headless = True
        return seleniumdriver(options=options)

    def set_up_headless_opera_driver():
        # Opera driver MRO: WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
        # options = selenium.webdriver.chrome.options.Options()
        # options.headless = True
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = seleniumdriver(options=options)
        print(common_message.unsupported_opera_headless)
        return driver

    def set_up_headless_safari_driver():
        print(common_message.unsupported_safari_headless)
        return seleniumdriver()

    def set_up_headless_chrome_driver():
        # options = selenium.webdriver.chrome.options.Options()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return seleniumdriver(chrome_options=options)

    def set_up_headless_brave_driver():
        print(common_message.unsupported_brave_headless)
        return configure_brave_driver()

    def set_up_headless_edge_driver():
        print(common_message.unsupported_edge_headless)
        return configure_edge_driver()

    def open_user_driver():
        if headless is False:
            return seleniumdriver()
        else: # headless is True
            if   user_driver == 'firefox': return set_up_headless_firefox_driver()
            elif user_driver == 'opera':   return set_up_headless_opera_driver()
            elif user_driver == 'safari':  return set_up_headless_safari_driver()
            elif user_driver == 'chrome':  return set_up_headless_chrome_driver()
            elif user_driver == 'brave':   return set_up_headless_brave_driver()
            elif user_driver == 'edge':    return set_up_headless_edge_driver()

    def determine_user_os():
        if   platform.system().lower().startswith('darwin'):  return 'macos'
        elif platform.system().lower().startswith('linux'):   return 'linux'
        elif platform.system().lower().startswith('windows'): return 'windows'
        else:
            print(common_message.unsupported_os)
            sys.exit()

    def show_user_how_to_set_up_selenium():
        if user_driver != 'safari':
            common_message.tell_user_to_download_driver(user_driver)
        common_message.display_dependency_setup_instructions(user_driver, user_os)

    def check_user_input():
        nonlocal channel, channel_type, file_name, txt_write_format, csv_write_format, docx_write_format, user_driver
        base_url     = 'https://www.youtube.com'
        videos       = 'videos'
        url          = f'{base_url}/{channel_type}/{channel}/{videos}'

        file_name = determine_file_name()
        txt_write_format  = verify_write_format(txt,  txt_write_format,  file_name, 'txt')
        csv_write_format  = verify_write_format(csv,  csv_write_format,  file_name, 'csv')
        docx_write_format = verify_write_format(docx, docx_write_format, file_name, 'docx')

        if (txt_write_format == 0 and csv_write_format == 0) or (txt is False and csv is False):
            print(common_message.not_writing_to_any_files)
            print(module_message.not_writing_to_any_files_hint) if execution_type == 'module' else print(script_message.not_writing_to_any_files_hint)
            sys.exit() # the files already exist and the user doesn't want to overwrite either of them

        if user_driver is None:
            print(module_message.running_default_driver) if execution_type == 'module' else print(script_message.running_default_driver)
            print(module_message.show_driver_options)    if execution_type == 'module' else print(script_message.show_driver_options)
            user_driver = 'firefox'
        seleniumdriver = check_driver()
        if seleniumdriver == 'invalid':
            sys.exit()
        return url, seleniumdriver




    user_os             = determine_user_os()
    url, seleniumdriver = check_user_input()
    program_start       = time.perf_counter()
    try:
        driver = open_user_driver()
    except selenium.common.exceptions.WebDriverException as err:
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        common_message.display_selenium_dependency_error(err)
        try:
            download_dependencies.run()
            driver = open_user_driver()
        except: # could not download the correct Selenium driver based on the user's OS and specified driver
            show_user_how_to_set_up_selenium()
            return
    with driver:
        print(f'\n\n\nNow scraping {url} using the {user_driver}driver:')
        videos_list = program.scroll_to_bottom(url, driver, scroll_pause_time)
        if len(videos_list) == 0:
            print(common_message.no_videos_found)
            return
        if txt is True and txt_write_format != 0: program.write_to_txt(videos_list, file_name, txt_write_format, chronological)
        if csv is True and csv_write_format != 0: program.write_to_csv(videos_list, file_name, csv_write_format, chronological)
    program_end = time.perf_counter()
    total_time  = program_end - program_start
    print(f'This program took {total_time} seconds to complete.\n')
