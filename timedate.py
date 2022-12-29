from datetime import datetime

def getCurrentWeekNr():
    now = datetime.now()
    weekNr = int(now.strftime("%W"))
    return weekNr

print("Week:",getCurrentWeekNr())