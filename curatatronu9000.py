import os
from telegram import Bot
from dotenv import load_dotenv
from supabase import create_client, Client

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