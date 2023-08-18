from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings

from src import consts
from src.utils import parse_toml_file

project_info = parse_toml_file(toml_path=consts.PROJECT_FILE_PATH)
bot_messages = project_info["messages"]
tool_poetry = project_info["tool"]["poetry"]


class MixinConfig(BaseSettings):
    """Миксин конфиг класс."""

    class Config:
        """Конфиг"""

        env_file = ".env"
        env_file_encoding = "utf-8"


class TGBotConfig(MixinConfig):
    """Класс с настройками для бота"""

    bot_token: SecretStr


class ProjectConfig(BaseModel):
    """Класс с настройками проекта"""

    hello_pattern: ClassVar[str] = bot_messages["hello_pattern"]
    help_pattern: ClassVar[str] = bot_messages["help_pattern"]
    post_url: ClassVar[str] = bot_messages["post_url"]
    repository_url: ClassVar[str] = tool_poetry["repository"]


class StaticFilePaths(BaseModel):
    """Класс для хранения путей к статическим файлам."""

    _root_path: ClassVar[str] = Path("static")

    photo_school: ClassVar[str] = Path(_root_path, "school.jpg")
    photo_selfie: ClassVar[str] = Path(_root_path, "last_selfie.jpg")

    voice_gpt: ClassVar[str] = Path(_root_path, "voice_gpt.mp3")
    voice_sql_nosql: ClassVar[str] = Path(_root_path, "voice_sql_nosql.mp3")
    voice_first_love: ClassVar[str] = Path(_root_path, "voice_first_love.mp3")
