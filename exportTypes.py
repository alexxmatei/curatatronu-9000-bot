import pytz
from datetime import time
from calendar import MONDAY
from computation import generateNewShiftStartMessage

# TODO - Description?
class Shift:
  def __init__(self, time, day, message):
    self.time = time
    self.day = day
    self.message = message

# TODO - Make private?
newShiftStartTime = time(hour=8, minute=0, second=0, tzinfo=pytz.timezone("Europe/Bucharest"))
newShiftStartDay = [MONDAY]
newShiftStartMessage = generateNewShiftStartMessage()

newShiftStart = Shift(newShiftStartTime, newShiftStartDay, newShiftStartMessage)

