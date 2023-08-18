import tomllib
from pathlib import Path


def parse_toml_file(toml_path: Path) -> dict:
    """Парсит TOML файл и возвращает словарь."""

    return tomllib.loads(toml_path.read_text())
