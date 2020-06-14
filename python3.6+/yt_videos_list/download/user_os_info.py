import sys
import platform
from ..notifications import Common
def determine_user_os():
 if   platform.system().lower().startswith('darwin'):  return 'macos'
 elif platform.system().lower().startswith('linux'):   return 'linux'
 elif platform.system().lower().startswith('windows'): return 'windows'
 else:
  print(Common().unsupported_os)
  sys.exit()
