import platform
import ctypes, os
import psutil
import shutil

from datetime import datetime
from .constants import UTC

def gethostname():
    hostname = platform.node()
    if "." in hostname:
        hostname = hostname.split(".", 2)[0]
    return hostname


def isAdmin() -> bool:
    is_admin: bool = False
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def isWindows() -> bool:
    return psutil.WINDOWS

def get_timestamp():
    now = datetime.now(UTC)
    value = now.strftime("%Y%m%dT%H%M%S.%f+00:00")
    return value

