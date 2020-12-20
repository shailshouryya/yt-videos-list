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
USER_OS    = determine_user_os()
PATH_SLASH = '\\'if USER_OS == 'windows' else '/'
if __name__ == '__main__':
    if USER_OS == 'windows':
        FORMATTED_PIP    = 'pip'
        FORMATTED_PYTHON = 'python'
    else:
        FORMATTED_PIP    = 'pip3'
        FORMATTED_PYTHON = 'python3'
    os.system(f'{FORMATTED_PYTHON} minifier.py')
    os.system(f'{FORMATTED_PIP}    install .')

from yt_videos_list.notifications import Common


def write_pseudo_json(drivers_dictionary):
    '''
    Creates a txt file containing all commands
    for supported selenium drivers. The helper
    function `format_pseudo_json()`
    strips formatting characters used to
    separate commands (commas, newlines).
    '''
    with open('temp.json', 'w', encoding='utf-8') as file:
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
    with open('temp.json', 'r', encoding='utf-8') as ftemp, open(f'..{PATH_SLASH}docs{PATH_SLASH}dependencies_pseudo_json.txt', 'w', encoding='utf-8') as ffinal:
        formatted = re.sub(',\n    ]', '\n    ]', ftemp.read())
        formatted = re.sub('],\n  },', ']\n  },', formatted)
        formatted = re.sub('},\n}',    '}\n}',    formatted)
        formatted = re.sub('%CD%',     'C',       formatted)
        ffinal.write(formatted)
    os.remove('temp.json')

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
    with open(f'..{PATH_SLASH}docs{PATH_SLASH}dependencies.json', 'w', encoding='utf-8') as ffinal:
        json.dump(drivers_dictionary, ffinal, indent=4)


if __name__ == '__main__':
    main()
