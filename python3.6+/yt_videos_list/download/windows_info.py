import subprocess
def get_drive_letter():
 return subprocess.getoutput('echo %CD%').split(':')[0]
def get_user_name():
 return subprocess.getoutput("whoami").split('\\')[1]
