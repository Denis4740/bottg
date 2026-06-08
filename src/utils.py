import logging
import os

def setup_logging():
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/main.log'),
            logging.StreamHandler()
        ]
    )

def send_message(bot, chat_id, text):
    """Утилита для отправки текстового сообщения (если нужна отдельно)"""
    bot.send_message(chat_id=chat_id, text=text)
