from loguru import logger
from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from src.config import TGBotConfig
from src.service.base import button_handle, start
from src.service.photo import send_photo

bot_config = TGBotConfig()


def main():
    """Начало работы бота."""

    logger.info("Запуск бота...")

    app = Application.builder().token(bot_config.bot_token.get_secret_value()).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_photo))
    app.add_handler(CallbackQueryHandler(button_handle))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
