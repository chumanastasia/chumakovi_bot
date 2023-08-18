from loguru import logger
from telegram import ForceReply, Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters

from src.config import StaticFilePaths
from src.service.keyboard import reply_keyboard


async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Функция, которая отправляет фото."""

    logger.info(f"Пользователь [{update.effective_user.id}] выполнил send_photo.")

    if update.message.text.lower() == "твое последнее селфи":
        with open(StaticFilePaths.photo_selfie, "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                reply_markup=reply_keyboard(),
            )
    elif update.message.text.lower() == "фото из старшей школы":
        with open(StaticFilePaths.photo_school, "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                reply_markup=reply_keyboard(),
            )
