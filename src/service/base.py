from loguru import logger
from telegram import (
    ForceReply,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters

from src.config import ProjectConfig
from src.schemas import AvailableActions
from src.service.keyboard import reply_keyboard
from src.service.voice import (
    send_voice_first_love,
    send_voice_gpt,
    send_voice_sql_no_sql,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Функция приветствия для команды /start."""

    logger.info(f"Пользователь [{update.effective_user.id}] выполнил команду /start.")

    user = update.effective_user

    hello_message = ProjectConfig.hello_pattern.format(user_first_name=user.first_name)
    await update.message.reply_html(
        hello_message,
        reply_markup=reply_keyboard(),
    )


async def send_help(update: Update) -> None:
    """Функция для предоставления инструкции по использованию."""

    logger.info(f"Пользователь [{update.effective_user.id}] выполнил send_help.")

    help_message = ProjectConfig.help_pattern
    await update.callback_query.message.reply_html(
        help_message,
        reply_markup=reply_keyboard(),
    )


async def send_git(update: Update) -> None:
    """Функция для отправки ссылки на репозиторий проекта."""

    logger.info(f"Пользователь [{update.effective_user.id}] выполнил send_git.")

    await update.callback_query.message.reply_text(
        ProjectConfig.repository_url,
        reply_markup=reply_keyboard(),
    )


async def read_post(update: Update) -> None:
    """Функция для отправки ссылки на статью."""

    logger.info(f"Пользователь [{update.effective_user.id}] выполнил read_post.")

    await update.callback_query.message.reply_html(
        text=ProjectConfig.post_url,
        reply_markup=reply_keyboard(),
    )


def button_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функция для обработки нажатия кнопок."""

    match update.callback_query.data:
        case AvailableActions.gpt.name:
            return send_voice_gpt(update)
        case AvailableActions.sql_nosql.name:
            return send_voice_sql_no_sql(update)
        case AvailableActions.first_love.name:
            return send_voice_first_love(update)
        case AvailableActions.read_post.name:
            return read_post(update)
        case AvailableActions.git.name:
            return send_git(update)
        case AvailableActions.help.name:
            return send_help(update)
        case _:
            return send_help(update)
