import os
import re
import json

from determine import determine_user_os
USER_OS = determine_user_os()
if USER_OS == 'windows':
    FORMATTED_PIP = 'pip'
    PATH_SLASH    = '\\'
else:
    FORMATTED_PIP = 'pip3'
    PATH_SLASH    = '/'
os.system(f'{FORMATTED_PIP} install .')


from yt_videos_list.notifications import Common

def write_pseudo_json(drivers_dictionary):
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
    with open('temp.json', 'r', encoding='utf-8') as ftemp, open(f'..{PATH_SLASH}docs{PATH_SLASH}dependencies_pseudo_json.txt', 'w', encoding='utf-8') as ffinal:
        formatted = re.sub(',\n    ]', '\n    ]', ftemp.read())
        formatted = re.sub('],\n  },', ']\n  },', formatted)
        formatted = re.sub('},\n}',    '}\n}',    formatted)
        formatted = re.sub('%CD%',     'C',       formatted)
        ffinal.write(formatted)
    os.remove('temp.json')

def main():
    common_messages = Common()
    drivers_dictionary = common_messages.driver_downloads_for_os

    write_pseudo_json(drivers_dictionary)
    format_pseudo_json()
    with open(f'..{PATH_SLASH}docs{PATH_SLASH}dependencies.json', 'w', encoding='utf-8') as ffinal:
        json.dump(drivers_dictionary, ffinal, indent=4)


if __name__ == '__main__':
    main()
