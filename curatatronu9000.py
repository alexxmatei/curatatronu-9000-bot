import os
import pytz
from telegram import Bot
from datetime import time
from dotenv import load_dotenv
from timedate import getCurrentWeekNr
from supabase import create_client, Client
from telegram.ext import Updater, CallbackContext, JobQueue

# The load_dotenv function will read a file named .env in the current working directory.
# It will then load any environment variables that are defined in the file.
# These environment variables can then be accessed using the os module.
load_dotenv()

# Get the CURATATRONU9000_API_TOKEN environment variable stored in the local .env file
CURATATRONU9000_API_TOKEN: str = os.environ['CURATATRONU9000_API_TOKEN']
userAlId: str = os.environ['USER_AL_ID'] # do the same for USER_AL_ID

curatatronu9000Bot: Bot = Bot(token=CURATATRONU9000_API_TOKEN)

curatatronu9000Bot.send_message(text='INIȚIERE PROTOCOL TEST...', chat_id=userAlId)

SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print(getCurrentWeekNr())

messageSchedule = time(hour=18, minute=30, second=0, tzinfo=pytz.timezone("Europe/Bucharest"))

updater = Updater(CURATATRONU9000_API_TOKEN, use_context=True)
job: JobQueue = updater.job_queue

def callbackSendScheduledMessage(context: CallbackContext):
    context.bot.send_message(chat_id=userAlId, 
                             text='It is: ' + str(messageSchedule))

jobWeekly = job.run_daily(callbackSendScheduledMessage, messageSchedule)

updater.start_polling()
updater.idle()