import os
os.system('pip install .')

from yt_videos_list.notifications import Common


def main():
    common_messages = Common()
    drivers_dictionary = common_messages.driver_downloads_for_os
    with open('dependencies.json', 'w') as f:
        f.write('{\n')
        for driver in drivers_dictionary:
            f.write(f'  "{driver}": ' + '{\n')
            for os in drivers_dictionary[driver]:
                f.write(f'    "{os}": [\n')
                for command in drivers_dictionary[driver][os]:
                    command = command.replace('\n', '').replace('"', "'")
                    f.write(f'      "{command}",\n')
                f.write('    ],\n')
            f.write('  },\n')
        f.write('}')

if __name__ == '__main__':
    main()
