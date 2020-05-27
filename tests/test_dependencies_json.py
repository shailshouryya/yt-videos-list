import os
os.system('pip install .')

from yt_videos_list.notifications import Common


def main():
    common_messages = Common()
    drivers_dictionary = common_messages.driver_downloads_for_os
    for driver in drivers_dictionary:
        print (driver)
        for os_commands in drivers_dictionary[driver]:
            for line in drivers_dictionary[driver][os_commands]:
                print(line)

if __name__ == '__main__':
    main()
