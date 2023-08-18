from loguru import logger
from telegram import ForceReply, Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters

from src.config import StaticFilePaths
from src.service.keyboard import reply_keyboard


async def send_voice_gpt(update: Update) -> None:
    """Функция, которая отправляет голосовое сообщение о GPT"""

    logger.info(f"Пользователь [{update.effective_user.id}] выполнил send_voice_gpt.")

    with open(StaticFilePaths.voice_gpt, "rb") as voice:
        await update.callback_query.message.reply_voice(
            voice=voice,
            reply_markup=reply_keyboard(),
        )


async def send_voice_sql_no_sql(update: Update) -> None:
    """Функция, которая отправляет голосовое сообщение о разнице между SQL и NoSQL"""

    logger.info(
        f"Пользователь [{update.effective_user.id}] выполнил send_voice_sql_no_sql."
    )

    with open(StaticFilePaths.voice_sql_nosql, "rb") as voice:
        await update.callback_query.message.reply_voice(
            voice=voice,
            reply_markup=reply_keyboard(),
        )


async def send_voice_first_love(update: Update) -> None:
    """Функция, которая отправляет голосовое сообщение о первой любви"""

    logger.info(
        f"Пользователь [{update.effective_user.id}] выполнил send_voice_first_love."
    )

    with open(StaticFilePaths.voice_first_love, "rb") as voice:
        await update.callback_query.message.reply_voice(
            voice=voice,
            reply_markup=reply_keyboard(),
        )
