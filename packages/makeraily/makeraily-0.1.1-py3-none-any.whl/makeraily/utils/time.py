import pytz
from datetime import datetime


tz = pytz.timezone("Asia/Shanghai")


def ts2time(ts: int):
    return datetime.fromtimestamp(ts).replace(tzinfo=tz)


def tsmilli2time(ts: int):
    return ts2time(ts / 1000).replace(tzinfo=tz)
