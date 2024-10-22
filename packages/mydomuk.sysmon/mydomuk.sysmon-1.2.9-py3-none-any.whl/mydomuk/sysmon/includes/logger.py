import logging
from enum import Enum

applog = logging.getLogger("sysmon")

class LOGLEVEL(Enum):
    LEVEL_INFO = logging.INFO
    LEVEL_DEBUG = logging.DEBUG
    LEVEL_CRITICAL = logging.CRITICAL
    LEVEL_VERBOSE = -1
    LEVEL_NOTSET = logging.NOTSET


_isdebug: bool = False
_curlevel: LOGLEVEL = LOGLEVEL.LEVEL_NOTSET

def initlog(level: LOGLEVEL=LOGLEVEL.LEVEL_INFO):
    global _isdebug, _curlevel  
    formatter = '%(asctime)s - %(name)s[%(levelname).1s] - %(message)s'
    _curlevel = level
    if level == LOGLEVEL.LEVEL_DEBUG:
        _isdebug = True
    elif level == LOGLEVEL.LEVEL_VERBOSE:
        level = LOGLEVEL.LEVEL_DEBUG
    logging.basicConfig(level=logging.NOTSET, format=formatter, datefmt="%b%d %H:%M:%S")
    applog.setLevel(int(level.value))


def isDebug():
    return _isdebug

def infolog(*msg):
    applog.info(*msg)

def errorlog(*msg):
    applog.error(*msg)

def debuglog(*msg):
    applog.debug(*msg)

def verboselog(*msg):
    if _curlevel == LOGLEVEL.LEVEL_VERBOSE:
        applog.debug(*msg)
