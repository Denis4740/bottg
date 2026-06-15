from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes
from api_client import get_new_image   # предположим, она асинхронная (или сделаем)
import logging
import asyncio

logger = logging.getLogger(__name__)

async def wake_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user_name = update.message.chat.first_name
    logger.info(f"Команда /start от {user_name} (id: {chat.id})")
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    # Добавляем await
    await context.bot.send_message(
        chat_id=chat.id,
        text=f"Привет, {user_name}! Посмотри, какого котика я тебе нашёл.",
        reply_markup=button
    )
    # Если get_new_image синхронная, запускаем её в отдельном потоке, чтобы не блокировать
    image = await asyncio.to_thread(get_new_image)   # если get_new_image синхронная
    # Если get_new_image уже асинхронная, просто await get_new_image()
    if image:
        await context.bot.send_photo(chat.id, image)
    else:
        await context.bot.send_message(chat.id, "Не удалось загрузить картинку :(")

async def newcat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    logger.info(f"Команда /newcat от {user_id}")
    # Используем get_new_image, а не get_random_cat_url
    cat_url = await asyncio.to_thread(get_new_image)   # если get_new_image синхронная
    # Если get_new_image возвращает URL, то:
    await update.message.reply_photo(photo=cat_url, caption="Вот вам кот!")
