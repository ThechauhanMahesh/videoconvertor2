from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 4796990
API_HASH = "32b6f41a4bf740efed2d4ce911f145c7"
BOT_TOKEN = "5031588187:AAGf3XLCvPZH6DVtaEBpr-Dghv7lDNlRQOE"
BOT_UN = "VideoConvertorRobot"
FORCESUB = int("-1001581768849")
FORCESUB_UN = "DroneBots"
ACCESS_CHANNEL = int("-1001768362393")
MONGODB_URI = "mongodb+srv://Vasusen:darkmaahi@cluster0.o7uqb.mongodb.net/cluster0?retryWrites=true&w=majority"
AUTH_USERS = 5351121397
LOG_ID = 1844675200
LOG_CHANNEL = "LogForVC"
Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
