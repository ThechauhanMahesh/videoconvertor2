from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 2992000
API_HASH = "235b12e862d71234ea222082052822fd"
BOT_UN = "Batakk"
BOT_TOKEN = "6387408633:AAHq3eVrM0EqXt_aEeIWUQD2lwGlXlAEF1g"

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
