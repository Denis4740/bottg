import logging
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from handlers import wake_up, new_cat
from utils import setup_logging

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN не найден в .env файле")

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Бот запускается...")
    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.start_polling()
    logger.info("Бот начал опрос")
    updater.idle()

if __name__ == '__main__':
    main()
