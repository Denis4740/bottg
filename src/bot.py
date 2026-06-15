import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from handlers import wake_up, newcat
from utils import setup_logging

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN не найден в .env файле")

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Бот запускается...")

    # Создаём приложение вместо Updater
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler('start', wake_up))
    application.add_handler(CommandHandler('newcat', new_cat))

    # Запускаем бота (метод run_polling включает polling и блокирует выполнение)
    logger.info("Бот начал опрос")
    application.run_polling()

if __name__ == '__main__':
    main()
