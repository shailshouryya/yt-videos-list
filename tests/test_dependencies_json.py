import os
import re
os.system('pip install .')

from yt_videos_list.notifications import Common


def main():
    common_messages = Common()
    drivers_dictionary = common_messages.driver_downloads_for_os
    with open('temp.json', 'w') as f:
        f.write('{\n')
        for driver in drivers_dictionary:
            f.write(f'  "{driver}": ' + '{\n')
            for supproted_os in drivers_dictionary[driver]:
                f.write(f'    "{supproted_os}": [\n')
                for command in drivers_dictionary[driver][supproted_os]:
                    command = command.replace('\n', '').replace('"', "'")
                    f.write(f'      "{command}",\n')
                f.write('    ],\n')
            f.write('  },\n')
        f.write('}')
    with open('temp.json', 'r') as ftemp, open('dependencies.json', 'w') as ffinal:
        formatted = re.sub(',\n    ]', '\n    ]', ftemp.read())
        formatted = re.sub('],\n  },', ']\n  },', formatted)
        formatted = re.sub('},\n}',    '}\n}',    formatted)
        formatted = re.sub('%CD%',     'C',       formatted)
        ffinal.write(formatted)
    os.remove('temp.json')


if __name__ == '__main__':
    main()
