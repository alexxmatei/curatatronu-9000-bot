# TODO - Keep in mind getCurrentWeekNr() can return 0 figure a workaround
from queries import getDbRandomGreeting, getDbResponsibleNameByOrderNr
from schema import GreetingsType
from stringlib import replaceUserNameInMessage
from timedate import getCurrentDayNr, getCurrentWeekNr
from data import userNamePattern, daysLeftPattern

def calculateDaysLeftInWeek():
    # ToDo - On windows once scheduler starts, days do not update and get
    #        re-calculated anymore.
    DAYS_IN_WEEK = 7
    daysLeftInWeek = DAYS_IN_WEEK - getCurrentDayNr()
    return daysLeftInWeek

def replaceNumberOfDaysInMessage(message: str, textToReplace:str):
    return message.replace(textToReplace, str(calculateDaysLeftInWeek()))

def calcResponsibleOrderNrInWeekNr(weekNr: int):
    """Calculates the order_number of the responsible for the given week number.

    Args:
        weekNr (`int`) - Must be value between 1 and 53. The number of the week in a year.
    Returns:
        :class:`int` - The order_number of the responsible in that given week.
    """
    if not isinstance(weekNr, int):
        raise TypeError("Input must be an integer.")
    if weekNr < 1 or weekNr > 53:
        raise ValueError("Input must be between 1 and 53.")
    return (weekNr - 1) % 4 + 1

# TODO - Function description
#      - Move into a new file?
def generateNewShiftStartMessage():
    randomWeeklyShiftStartMsg: str = getDbRandomGreeting(GreetingsType.weeklyShiftStart.value)
    # TODO WeekNr = 0 on 01.01.2023, look into this
    currentWeekResponsibleOrderNr: str = calcResponsibleOrderNrInWeekNr(getCurrentWeekNr())
    currentWeekResponsibleName: str = (getDbResponsibleNameByOrderNr(currentWeekResponsibleOrderNr))
    newShiftStartMessage: str = replaceUserNameInMessage(randomWeeklyShiftStartMsg, userNamePattern, currentWeekResponsibleName)
    
    return newShiftStartMessage

def generateNewShiftReminderMessage():
    randomWeeklyShiftReminderMsg: str = getDbRandomGreeting(GreetingsType.weeklyShiftReminder.value)
    # TODO WeekNr = 0 on 01.01.2023, look into this
    currentWeekResponsibleOrderNr: str = calcResponsibleOrderNrInWeekNr(getCurrentWeekNr())
    currentWeekResponsibleName: str = (getDbResponsibleNameByOrderNr(currentWeekResponsibleOrderNr))
    shiftReminderMessage: str = replaceUserNameInMessage(randomWeeklyShiftReminderMsg, userNamePattern, currentWeekResponsibleName)
    shiftReminderMessage: str = replaceNumberOfDaysInMessage(shiftReminderMessage, daysLeftPattern)
    
    return shiftReminderMessage
