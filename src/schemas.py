from enum import Enum
from typing import ClassVar

from pydantic import BaseModel, Field


class AvailableActions(Enum):
    """Класс с доступными действиями"""

    gpt: str = "Что такое GPT 👾"
    sql_nosql: str = "Разница между SQL и NoSQL 💾"
    first_love: str = "История первой любви ❤️"
    read_post: str = "О моем увлечении 🎨"
    git: str = "Ссылка на проект 💻"
    help: str = "Помощь 💡"
