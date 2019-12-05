from enum import IntEnum
from datetime import datetime

class Weekday(IntEnum):
    MONDAY      = 0
    TUESDAY     = 1
    WEDNESDAY   = 2
    THURSDAY    = 3
    FRIDAY      = 4
    SATURDAY    = 5
    SUNDAY      = 6

def meetup_date(year, month, nth=0, weekday=None):
    _nth = 4 if nth == 0 else nth
    _weekday = 3 if not weekday else weekday

    d = datetime(year, month, 1)
    weekday = d.weekday()
    fd = 1
    if weekday > _weekday:
        fd = (6 - weekday) + (_weekday + 1) + 1
    elif weekday < _weekday:
        fd = 1 + (_weekday - weekday)
    wd = fd + (7 * (_nth - 1))

    return datetime(year, month, wd).date()