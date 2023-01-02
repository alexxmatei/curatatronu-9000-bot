from exportTypes import newShiftStart
from telegram.ext import Updater, CallbackContext, JobQueue
from data import CURATATRONU9000_API_TOKEN, groupFacetiBaCuratenie

updater = Updater(CURATATRONU9000_API_TOKEN, use_context=True)
job: JobQueue = updater.job_queue

# TODO - Function description
def cbSendScheduledMessage(context: CallbackContext):
    context.bot.send_message(chat_id=groupFacetiBaCuratenie, text=newShiftStart.message)

jobWeekly = job.run_daily(cbSendScheduledMessage, newShiftStart.time, newShiftStart.day)

# TODO - Make more elegant
#      - Add more details (chat_id, etc.)
# List scheduled jobs
for x in range(job.jobs().__len__()):
    print(job.jobs()[x].job)

updater.start_polling()
updater.idle()