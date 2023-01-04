from datetime import datetime

def getCurrentWeekNr():
    now = datetime.now()
    weekNr = int(now.strftime("%W"))
    # TODO - Validate output
    return weekNr