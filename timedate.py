from datetime import datetime

def getCurrentWeekNr():
    now: datetime = datetime.now()
    weekNr: int = int(now.strftime("%W"))
    # TODO - Validate output
    return weekNr

# TODO - comment - Day is between 0 (Monday) and 6 (Sunday)
def getCurrentDayNr():
    now: datetime = datetime.now()
    dayNr: int = now.weekday()
    return dayNr