from telegram import ReplyKeyboardMarkup
from api_client import get_new_image
import logging

logger = logging.getLogger(__name__)

def wake_up(update, context):
    chat = update.effective_chat
    user_name = update.message.chat.first_name
    logger.info(f"Команда /start от {user_name} (id: {chat.id})")
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f"Привет, {user_name}! Посмотри, какого котика я тебе нашёл.",
        reply_markup=button
    )
    image = get_new_image()
    if image:
        context.bot.send_photo(chat.id, image)
    else:
        context.bot.send_message(chat.id, "Не удалось загрузить картинку :(")

def new_cat(update, context):
    chat = update.effective_chat
    logger.info(f"Команда /newcat от {chat.id}")
    image = get_new_image()
    if image:
        context.bot.send_photo(chat.id, image)
    else:
        context.bot.send_message(chat.id, "Ошибка получения картинки")
