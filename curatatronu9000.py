from exportTypes import newShiftStart, programStart
from telegram import Bot
from telegram.ext import Updater, CallbackContext, JobQueue
from data import CURATATRONU9000_API_TOKEN, groupFacetiBaCuratenie

curatatronu9000Bot: Bot = Bot(token=CURATATRONU9000_API_TOKEN)
updater = Updater(CURATATRONU9000_API_TOKEN, use_context=True)
job: JobQueue = updater.job_queue

# TODO - Function description
def cbSendScheduledMessage1(context: CallbackContext):
    context.bot.send_message(chat_id=groupFacetiBaCuratenie, text=newShiftStart.message)
    # TODO - Function description
def cbSendScheduledMessage2(context: CallbackContext):
    context.bot.send_message(chat_id=groupFacetiBaCuratenie, text=programStart.message)

jobWeekly = job.run_daily(cbSendScheduledMessage1, newShiftStart.time, newShiftStart.day)
jobWeekly = job.run_daily(cbSendScheduledMessage2, programStart.time, programStart.day)

# TODO - Make more elegant
#      - Add more details (chat_id, etc.)
# List scheduled jobs
for x in range(job.jobs().__len__()):
    print(job.jobs()[x].job)

##### Get & List all updates #####
updates = curatatronu9000Bot.get_updates()
print(updates)
for x in updates:
    print (x)
##################################

updater.start_polling()
updater.idle()