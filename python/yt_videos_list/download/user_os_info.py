import warnings
import platform
from ..notifications import Common
def determine_user_os():
 user_os = platform.system().lower()
 if user_os.startswith('darwin'): return 'macos'
 elif user_os.startswith('linux'): return 'linux'
 elif user_os.startswith('windows'): return 'windows'
 else:
  warnings.warn(Common().display_unsupported_os(user_os), RuntimeWarning)
  warnings.resetwarnings()
  return user_os
