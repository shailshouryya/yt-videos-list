import sys
import platform
from ..notifications import Common
def determine_user_os():
 user_os = platform.system().lower()
 if user_os.startswith('darwin'): return 'macos'
 elif user_os.startswith('linux'): return 'linux'
 elif user_os.startswith('windows'): return 'windows'
 else:
  print(Common().unsupported_os)
  sys.exit()
