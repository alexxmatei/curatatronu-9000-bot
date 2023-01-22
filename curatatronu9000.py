#TODO - Add reminders throught the for curatatronu'-9000 Copied
#Ex:
#weekly_shift_reminder
#Bă @user, e miercuri, mai ai 5 zile de curățenie
#Bă @user, e vineri, mai ai 3 zile de curățenie
#weekly_shift_end
#Bă @user, e duminică, azi e ultima ta zi de curățenie

from exportTypes import newShiftStart, shiftReminder
from telegram.ext import Updater, CallbackContext, JobQueue
from data import CURATATRONU9000_API_TOKEN, groupFacetiBaCuratenieId

updater = Updater(CURATATRONU9000_API_TOKEN, use_context=True)
job: JobQueue = updater.job_queue

# TODO - Function description
def cbSendScheduledShiftStartMessage(context: CallbackContext):
    if not isinstance(context, CallbackContext):
        raise TypeError("Input must be of type CallbackContext.")
    context.bot.send_message(chat_id=groupFacetiBaCuratenieId, text=newShiftStart.message)

def cbSendScheduledShiftReminderMessage(context: CallbackContext):
    if not isinstance(context, CallbackContext):
        raise TypeError("Input must be of type CallbackContext.")
    context.bot.send_message(chat_id=groupFacetiBaCuratenieId, text=shiftReminder.message)

jobWeeklyShiftStart = job.run_daily(cbSendScheduledShiftStartMessage, newShiftStart.startTime, newShiftStart.days)
jobWeeklyShiftReminder = job.run_daily(cbSendScheduledShiftReminderMessage, shiftReminder.startTime, shiftReminder.days)

# TODO - Make more elegant
#      - Add more details (chat_id, etc.)
# List scheduled jobs
for x in range(job.jobs().__len__()):
    print(job.jobs()[x].job)

updater.start_polling()
updater.idle()
