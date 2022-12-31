
import pytz
from telegram import Bot
from datetime import time
from data import SUPABASE_KEY, SUPABASE_URL, CURATATRONU9000_API_TOKEN, userAlId
from timedate import getCurrentWeekNr
from telegram.ext import Updater, CallbackContext, JobQueue
from supabase import create_client, Client

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
curatatronu9000Bot: Bot = Bot(token=CURATATRONU9000_API_TOKEN)
updater = Updater(CURATATRONU9000_API_TOKEN, use_context=True)
job: JobQueue = updater.job_queue

curatatronu9000Bot.send_message(text='INIȚIERE PROTOCOL TEST...', chat_id=userAlId)

print(getCurrentWeekNr())

messageSchedule = time(hour=19, minute=0, second=0, tzinfo=pytz.timezone("Europe/Bucharest"))

def callbackSendScheduledMessage(context: CallbackContext):
    context.bot.send_message(chat_id=userAlId, 
                             text='It is: ' + str(messageSchedule))

jobWeekly = job.run_daily(callbackSendScheduledMessage, messageSchedule)

updater.start_polling()
updater.idle()