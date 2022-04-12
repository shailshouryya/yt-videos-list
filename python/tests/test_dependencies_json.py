'''
Test module for creating json and txt file
containing the commands for downloading
required selenium webdriver dependencies
for supported selenium drivers. The commands
are generated from the
`yt_videos_list.notifications` module.
'''
import os
import re
import json

from determine import determine_user_os

from yt_videos_list.notifications import Common


def main():
    '''
    Imports Common class from `yt_videos_list.notifications`
    to use the commands dictionary (`driver_downloads_for_os`)
    defined in the `Common().__init__` method to create json
    and json-like text files. Both files contain all commands
    for downloading required selenium webdriver dependencies
    for supported selenium drivers. Output placed
    in `../docs/` directory.
    '''
    common_messages = Common()
    drivers_dictionary = common_messages.driver_downloads_for_os

    write_pseudo_json(drivers_dictionary)
    format_pseudo_json()
    with open(f'..{PATH_SLASH}docs{PATH_SLASH}dependencies.json', mode='w', encoding='utf-8') as json_file:
        json.dump(drivers_dictionary, json_file, indent=4)


def write_pseudo_json(drivers_dictionary):
    '''
    Creates a txt file containing all commands
    for supported selenium drivers. The helper
    function `format_pseudo_json()`
    strips formatting characters used to
    separate commands (commas, newlines).
    '''
    with open('temp.json', mode='w', encoding='utf-8') as file:
        file.write('{\n')
        for driver in drivers_dictionary:
            file.write(f'  {driver}: ' + '{\n')
            for supproted_os in drivers_dictionary[driver]:
                file.write(f'    {supproted_os}: [\n\n')
                for command in drivers_dictionary[driver][supproted_os]:
                    file.write(f'      {command}\n')
                file.write('    ],\n')
            file.write('  },\n')
        file.write('}')

def format_pseudo_json():
    '''
    Strips formatting characters used
    to separate commands (commas, newlines) from the
    txt file. Results in json-like structured file
    except with an extra newline, instead of double
    quotation marks and commas, to separate the commands.
    '''
    with open('temp.json', mode='r', encoding='utf-8') as ftemp, open(f'..{PATH_SLASH}docs{PATH_SLASH}dependencies_pseudo_json.txt', mode='w', encoding='utf-8') as ffinal:
        formatted = re.sub(',\n    ]', '\n    ]', ftemp.read())
        formatted = re.sub('],\n  },', ']\n  },', formatted)
        formatted = re.sub('},\n}',    '}\n}',    formatted)
        formatted = re.sub('%CD%',     'C',       formatted)
        ffinal.write(formatted)
    os.remove('temp.json')


if __name__ == '__main__':
    if determine_user_os() == 'windows': os.system(r'.\tests\setup.bat'); PATH_SLASH = '\\'
    else:                                os.system( 'sh tests/setup.sh'); PATH_SLASH = '/'
    main()
