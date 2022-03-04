import sys
import time
import random
import traceback
import contextlib

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support   import expected_conditions as EC

from . import program
from .download.selenium_webdriver_dependencies import download_all
from .download.windows_info                    import get_drive_letter
from .download.user_os_info                    import determine_user_os
from .notifications                            import Common, ModuleMessage, ScriptMessage
from .custom_logger                            import log


def execute(urls, file_name, log_silently, txt, csv, markdown, file_suffix, all_video_data_in_memory, video_id_only, reverse_chronological, headless, scroll_pause_time, user_driver, cookie_consent, verify_page_bottom_n_times, file_buffering, list_creator_configuration, execution_type, counts=None, min_sleep=None, max_sleep=None, after_n_channels_pause_for_s=None, aggregate_logging_locations=None):
    common_message = Common(list_creator_configuration)
    module_message = ModuleMessage(list_creator_configuration)
    script_message = ScriptMessage(list_creator_configuration)


    def verify_writing_to_at_least_one_location():
        if txt is False and csv is False and markdown is False and all_video_data_in_memory is False:
            if execution_type == 'module': raise RuntimeError(module_message.not_writing_to_any_files_hint + module_message.display_current_configuration())
            else:                          raise RuntimeError(script_message.not_writing_to_any_files_hint + script_message.display_current_configuration())


    def process_url():
        try:
            _, channel_type, channel_id = parse_url()
        except IndexError as error_message:
            raise ValueError(common_message.url_error) from error_message
        base_url = 'https://www.youtube.com'
        return f'{base_url}/{channel_type}/{channel_id}/videos?view=0&sort=dd&flow=grid&shelf_id=0'

    def parse_url():
        channel_info = url.split('youtube.com/')[1]
        channel_type = channel_info.split('/')[0]
        try:
            # handle URLs such as
            # youtube.com/identifier/                 # NOTE there is a trailing slash here!
            # youtube.com/identifier/ID
            # youtube.com/identifier/ID/
            # youtube.com/identifier/ID/anythingElse
            channel_id = channel_info.split('/')[1]
        except IndexError:
            # handle URLs such as
            # youtube.com/identifier                  # NOTE there is no trailing slash here!
            channel_id = ''
        return channel_info, channel_type, channel_id


    def open_user_driver():
        nonlocal user_driver
        if user_driver is None:
            if execution_type == 'module': print(module_message.running_default_driver + '\n' + module_message.show_driver_options)
            else:                          print(script_message.running_default_driver + '\n' + script_message.show_driver_options)
            user_driver = 'firefox'
        user_driver = user_driver.lower()
        supported_drivers = {
            'firefox': configure_firefoxdriver,
            'opera':   configure_operadriver,
            'chrome':  configure_chromedriver,
            'brave':   configure_bravedriver,
            'edge':    configure_edgedriver,
            'safari':  configure_safaridriver
        }
        if user_driver not in supported_drivers:
            raise ValueError(common_message.invalid_driver + common_message.display_current_configuration())
        return supported_drivers[user_driver]()    # NOTE the need to CALL the function returned by supported_drivers[key] since the dictionary value is a function REFERENCE (the function is not yet invoked)


    def configure_firefoxdriver():
        options = selenium.webdriver.firefox.options.Options()
        if headless is True:
            options.headless = True
        return webdriver.Firefox(options=options)

    def configure_operadriver():
        # webdriver.Opera class MRO (method resolution order): WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
        # check with
        # >>> from selenium import webdriver
        # >>> help(webdriver.Opera)
        # options = selenium.webdriver.chrome.options.Options()
        # options.headless = True
        options = webdriver.ChromeOptions()
        if headless is True:
            options.add_argument('headless')
            print(common_message.unsupported_opera_headless)
        return webdriver.Opera(options=options)

    def configure_safaridriver():
        if user_os != 'macos':
            common_message.display_dependency_setup_instructions('safari', user_os)
            raise RuntimeError(common_message.selenium_launch_error)
        if headless is True:
            print(common_message.unsupported_safari_headless)
        return webdriver.Safari()

    def configure_chromedriver():
        # options = selenium.webdriver.chrome.options.Options()
        options = webdriver.ChromeOptions()
        if headless is True:
            options.add_argument('headless')
        return webdriver.Chrome(chrome_options=options)

    def configure_bravedriver():
        options = webdriver.ChromeOptions()
        if user_os == 'windows':
            drive  = get_drive_letter()
            options.binary_location = rf'{drive}:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
            executable_path         = rf'{drive}:\Windows\bravedriver.exe'
        else:
            options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
            executable_path         = '/usr/local/bin/bravedriver'
        if headless is True:
            print(common_message.unsupported_brave_headless)
            # options.headless = True
        return webdriver.Chrome(options=options, executable_path=executable_path)

    def configure_edgedriver():
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
            raise RuntimeError(common_message.selenium_launch_error)
        if headless is True:
            print(common_message.unsupported_edge_headless)
            # options.headless = True
        return webdriver.Edge(executable_path=executable_path)


    def show_user_how_to_set_up_selenium():
        if user_driver != 'safari':
            common_message.tell_user_to_download_driver(user_driver)
        common_message.display_dependency_setup_instructions(user_driver, user_os)


    def handle_opening_webdriver_exception(error_message):
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        nonlocal driver
        common_message.display_selenium_dependency_error(error_message)
        try:
            download_all()
            driver = open_user_driver()
        except selenium.common.exceptions.WebDriverException as same_error_message_again: # could not download the correct Selenium driver based on the user's OS and specified driver
            show_user_how_to_set_up_selenium()
            common_message.display_unable_to_update_driver_automatically(user_driver)
            raise RuntimeError(common_message.selenium_launch_error) from same_error_message_again


    def run_scraper():
        driver.get(url)
        manage_cookie_consent_form()
        wait = selenium.webdriver.support.ui.WebDriverWait(driver, 9)
        channel_heading_xpath       = '//yt-formatted-string[@class="style-scope ytd-channel-name"]'
        topic_channel_heading_xpath = '//yt-formatted-string[@class="style-scope ytd-topic-channel-details-renderer"]'
        def load_page(channel_heading_xpath, topic_channel_heading_xpath):
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, channel_heading_xpath)))
            except selenium.common.exceptions.TimeoutException:
                wait.until(EC.element_to_be_clickable((By.XPATH, topic_channel_heading_xpath)))
            except selenium.common.exceptions.WebDriverException as error_message:
                traceback.print_exc()
                raise RuntimeError(common_message.possible_topic_channel_in_headless_error) from error_message
        try:
            load_page(channel_heading_xpath, topic_channel_heading_xpath)
        except selenium.common.exceptions.TimeoutException as error_message:
            raise RuntimeError(common_message.selenium_unable_to_load_elements_error) from error_message
        channel_name, file_name = determine_file_name(channel_heading_xpath, topic_channel_heading_xpath)
        with yield_logger(file_name) as logging_locations:
            log( '>' * 50 + 'STARTING  PROGRAM' + '<' * 50,             logging_locations)
            log(f'Now scraping {url} using the {user_driver}driver...', logging_locations)
            log(f'Current configuration: {list_creator_configuration}', logging_locations)
            video_data = program.determine_action(url, driver, video_id_only, scroll_pause_time, verify_page_bottom_n_times, reverse_chronological, file_name, file_buffering, txt, csv, markdown, all_video_data_in_memory, logging_locations)
            program_end = time.perf_counter()
            program_end_real_time = time.time()
            program_cpu_time  = program_end - program_start
            total_real_time = program_end_real_time - program_start_real_time
            log(f'This program took {program_cpu_time} seconds ({total_real_time} seconds real time) to complete writing information for the "{channel_name}" channel to the {file_name} file.', logging_locations)
            log( '>' * 50 + 'COMPLETED PROGRAM' + '<' * 50,                                                                                          logging_locations)
        return (video_data, (channel_name, file_name), program_cpu_time, total_real_time)


    def manage_cookie_consent_form():
        if 'consent.youtube.com' in driver.current_url:
            common_message.display_cookie_redirection()
            accept_button_relative_path = '//button[@aria-label="Agree to the use of cookies and other data for the purposes described"]'
            accept_button               = driver.find_element_by_xpath(accept_button_relative_path)
            if cookie_consent is False:
                common_message.display_blocking_cookie_consent()
                wait = selenium.webdriver.support.ui.WebDriverWait(driver, 9)
                # YouTube changed the HTML formatting to make it significantly more difficult to block cookies programatically
                # the following no longer works:
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Customize"]')))
                # driver.find_element_by_xpath('//a[@aria-label="Customize"]').click()
                # the new HTML format uses dynamically named attributes, making it nearly impossible to hard code the cooking blocking process
                # example:
                # <button class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc IIdkle" jscontroller="soHxf" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc; touchcancel:JMtRjd; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;" data-idom-class="nCP5yc AjY5Oe DuMIQc IIdkle" jsname="Q7N4Oc"><div class="VfPpkd-Jh9lGc"></div><div class="VfPpkd-RLmnJb"></div><span jsname="V67aGc" class="VfPpkd-vQzf8d">Customize</span></button></div></div>
                # notice how "Customize" is now just an innerHTML attribute, and nested as a very deep child node of dynamically named attributes
                # one workaround is using a relative path from the "I AGREE" button
                customize_button_relative_path = f'{accept_button_relative_path}/../../../../div/div/button'
                wait.until(EC.element_to_be_clickable((By.XPATH, customize_button_relative_path)))
                driver.find_element_by_xpath(customize_button_relative_path).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Turn off Ad personalization"]')))    # last form element on page
                driver.find_element_by_xpath('//button[@aria-label="Turn off Search customization"]').click()
                driver.find_element_by_xpath('//button[@aria-label="Turn off YouTube History"]').click()
                driver.find_element_by_xpath('//button[@aria-label="Turn off Ad personalization"]').click()
                # clicking the button above also selects the 2 buttons below
                # driver.find_element_by_xpath('//button[@aria-label="Turn off Ad personalization on Google Search"]').click()
                # driver.find_element_by_xpath('//button[@aria-label="Turn off Ad personalization on YouTube & across the web"]').click()
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Ad personalization is off"]')))      # wait for last form element on page to update
                # driver.find_element_by_xpath('//form[@method="POST"]').click()                                             # this doesn't seem to click the button
                driver.find_elements_by_xpath('//form/div/button')[-1].click()                                               # find the CONFIRM button and click it
            elif cookie_consent is True:
                common_message.display_accepting_cookie_consent()
                accept_button.click()
            else:
                common_message.display_invalid_cookie_consent_option(cookie_consent)


    def determine_file_name(channel_heading_xpath, topic_channel_heading_xpath):
        channel_name = driver.find_element_by_xpath(channel_heading_xpath).text or driver.find_element_by_xpath(topic_channel_heading_xpath).text
        is_id = '_id' if video_id_only is True else ''
        if file_suffix is True: suffix = f'_reverse_chronological_video{is_id}s_list' if reverse_chronological else f'_chronological_video{is_id}s_list'
        else:                   suffix = ''
        if txt is False and csv is False and markdown is False:
            # program will not write to any output files
            # program will store video data in memory and return the list of lists containing the video data
            # only runs when all_video_data_in_memory=True
            formatted_file_name = ''
        elif file_name == 'auto':
            formatted_channel_name = channel_name.replace(' ', '')
            formatted_file_name    = f'{formatted_channel_name}{suffix}'
        elif file_name == 'id':
            _, channel_type, channel_id = parse_url()
            if channel_id in ('videos', ''):
                # handle URLs such as
                # youtube.com/teded                                    # id will be teded
                # youtube.com/teded/                                   # id will be teded
                # youtube.com/teded/videos                             # id will be teded
                # youtube.com/originals                                # id will be originals
                # youtube.com/originals/                               # id will be originals
                # youtube.com/originals/videos                         # id will be originals
                formatted_file_name = f'{channel_type}{suffix}'
            else:
                # handle URLs such as
                # youtube.com/channel/UC-Some24CharacterString         # id will be UC-Some24CharacterString
                # youtube.com/channel/UC-Some24CharacterString/        # id will be UC-Some24CharacterString
                # youtube.com/channel/UC-Some24CharacterString/videos  # id will be UC-Some24CharacterString
                # youtube.com/user/UserNameForChannel                  # id will be UserNameForChannel
                # youtube.com/user/UserNameForChannel/                 # id will be UserNameForChannel
                # youtube.com/user/UserNameForChannel/videos           # id will be UserNameForChannel
                # youtube.com/c/ChannelName                            # id will be ChannelName
                # youtube.com/c/ChannelName/                           # id will be ChannelName
                # youtube.com/c/ChannelName/videos                     # id will be ChannelName
                formatted_file_name = f'{channel_id}{suffix}'
        else:
            if   file_name.endswith('.txt') or file_name.endswith('.csv'): formatted_file_name = file_name[:-4]
            elif file_name.endswith('.md'):                                formatted_file_name = file_name[:-3]
            else:                                                          formatted_file_name = file_name
        return (channel_name, formatted_file_name)


    @contextlib.contextmanager
    def yield_logger(file_name):
        log_file = f'{file_name}.log'
        with open(log_file, mode='a', encoding='utf-8',  buffering=file_buffering) as output_location:
            if log_silently is True: yield (output_location,)
            else:                    yield (output_location, sys.stdout)


    verify_writing_to_at_least_one_location()
    user_os       = determine_user_os()
    if aggregate_logging_locations:
        multiplier = max(0, max_sleep - min_sleep)
        modulo, seconds = after_n_channels_pause_for_s
    try:
        driver = open_user_driver()
    except selenium.common.exceptions.WebDriverException as error_message:
        handle_opening_webdriver_exception(error_message)
    with driver:
        driver.set_window_size(780, 800)
        driver.set_window_position(0, 0)
        while urls:
            if aggregate_logging_locations:
                counts[0] += 1
                count      = counts[0]
                if count % modulo == 0 and count > 0:
                    log(f'Scraped {count} channels, so sleeping for {seconds} seconds to seem less bot-like....', aggregate_logging_locations)
                    time.sleep(seconds)
                sleep_time = min_sleep + (random.random() * multiplier)
                log(f'Sleeping for {sleep_time} seconds before scraping next URL....', aggregate_logging_locations)
                time.sleep(sleep_time)
            program_start = time.perf_counter()
            program_start_real_time = time.time()
            if urls: url = urls.popleft()
            else:    continue
            if aggregate_logging_locations: log(f'{" "*8} Scraping {count:>7}: {url}', aggregate_logging_locations)
            url = process_url()
            video_data, write_information, thread_cpu_time, thread_real_time = run_scraper()
            channel_name, output_file_name                     = write_information
            if aggregate_logging_locations: log(f'Finished scraping {count:>7}: "{channel_name}" and wrote to the {output_file_name} file in {thread_cpu_time} seconds ({thread_real_time} seconds real time)', aggregate_logging_locations)
        return (video_data, (channel_name, output_file_name))
