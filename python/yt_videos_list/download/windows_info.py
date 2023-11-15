import subprocess
def get_drive_letter(
) -> str:
 return subprocess.getoutput('echo %CD%').split(':')[0]
def get_user_name(
) -> str:
 return subprocess.getoutput('whoami').split('\\')[1]
