import pytz
from datetime import time
from calendar import MONDAY
from computation import generateNewShiftStartMessage

# TODO - Can you add parameters in documentation tooltip?
class Shift():
  """
  TODO - Add description

  Args:
    TODO - Add types (if needed)

  Raises:
    TODO - Add raises (if needed), check Updater


  Attributes:
    TODO - Add attributes (if needed)
  """
  def __init__(self, startTime: time, days: list[int], message: str):
    self.startTime = startTime
    self.days = days
    self.message = message

  @property
  def startTime(self):
    return self._startTime

  @startTime.setter
  def startTime(self, value):
    if not isinstance(value, time):
      raise TypeError("Property must be of type time.")
    # TODO - Should we do a value check here? (Maybe time must be set in the future)
    self._startTime = value

  @property
  def days(self):
    return self._days

  @days.setter
  def days(self, value):
    if not isinstance(value, list):
      raise TypeError("Property must be a list of integers.")
    for element in value:
      if not isinstance(element, int):
        raise TypeError("Property must be a list of integers.")
    if not all(map(lambda x: x in range(7), value)):
      raise ValueError("List must only contain digits in the range from 0 to 6 (MONDAY to FRIDAY)")
    self._days = value

  @property
  def message(self):
    return self._message

  @message.setter
  def message(self, value):
    if not isinstance(value, str):
      raise TypeError("Property must be of type string.")
    # TODO - Should we do a value check here?
    self._message = value

# TODO - Make private?
newShiftStartTime = time(hour=8, minute=0, second=0, tzinfo=pytz.timezone("Europe/Bucharest"))
newShiftStartDay = [MONDAY]
newShiftStartMessage = generateNewShiftStartMessage()

newShiftStart = Shift(newShiftStartTime, newShiftStartDay, newShiftStartMessage)

