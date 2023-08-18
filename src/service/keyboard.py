from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from src.schemas import AvailableActions


def reply_keyboard():
    """Функция для создания клавиатуры."""

    keyboard = [
        [
            InlineKeyboardButton(
                AvailableActions.gpt.value, callback_data=AvailableActions.gpt.name
            )
        ],
        [
            InlineKeyboardButton(
                AvailableActions.sql_nosql.value,
                callback_data=AvailableActions.sql_nosql.name,
            )
        ],
        [
            InlineKeyboardButton(
                AvailableActions.first_love.value,
                callback_data=AvailableActions.first_love.name,
            )
        ],
        [
            InlineKeyboardButton(
                AvailableActions.read_post.value,
                callback_data=AvailableActions.read_post.name,
            )
        ],
        [
            InlineKeyboardButton(
                AvailableActions.git.value, callback_data=AvailableActions.git.name
            )
        ],
        [
            InlineKeyboardButton(
                AvailableActions.help.value, callback_data=AvailableActions.help.name
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
