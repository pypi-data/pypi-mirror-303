import datetime
import os
import sys
import time

from . import base36

DATE_2K = 946684800

def getNoise() -> str:
    counter = int.from_bytes(os.urandom(2), 'little')
    return format(counter, 'x').zfill(2)[-2:]

def parseAid(aid: str) -> datetime.datetime:
    """aidを生成します。

    Returns:
        str: aid
    """
    base36_time = aid[:8]
    time_milliseconds = int(base36.decode(base36_time))
    timestamp = DATE_2K + time_milliseconds / 1000
    if sys.version_info < (3, 11):
        return datetime.datetime.utcfromtimestamp(timestamp)
    return datetime.datetime.fromtimestamp(timestamp, datetime.UTC)

def genAid(timestamp: float=None) -> str:
    """aidを生成します。

    Returns:
        str: aid
    """
    if timestamp is None:
        timestamp = int((time.time() - DATE_2K) * 1000)
    else:
        timestamp = int((timestamp - DATE_2K) * 1000)
    base36_time = base36.encode(timestamp)
    noise = getNoise()
    aid = base36_time.zfill(8) + noise.zfill(2)
    return aid