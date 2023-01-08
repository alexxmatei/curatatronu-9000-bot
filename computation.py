# TODO - Keep in mind getCurrentWeekNr() can return 0 figure a workaround
from queries import getDbRandomGreeting, getDbResponsibleNameByOrderNr
from stringlib import replaceUserNameInMessage
from timedate import getCurrentWeekNr


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
    # TODO - Define type "weekly-shift-start" (and others) somewhere
    # TODO - Edit, use the new naming convention for values (snake_casing)
    randomWeeklyShiftStartMsg=getDbRandomGreeting("weekly-shift-start")
    # TODO WeekNr = 0 on 01.01.2023, look into this
    currentWeekResponsibleOrderNr = calcResponsibleOrderNrInWeekNr(getCurrentWeekNr())
    currentWeekResponsibleName = (getDbResponsibleNameByOrderNr(currentWeekResponsibleOrderNr))
    # TODO - Specify "@user" pattern somewhere as a constant
    newShiftStartMessage = replaceUserNameInMessage(randomWeeklyShiftStartMsg, "@user", currentWeekResponsibleName)
    return newShiftStartMessage
