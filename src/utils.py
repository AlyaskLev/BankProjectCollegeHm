import json
import os

from src.log_config import setup_logger

logger = setup_logger("utils", "utils.log")


def load_transactions(filepath: str) -> list[dict]:
    if not os.path.exists(filepath):
        logger.warning(f"Файл не найден: {filepath}")
        return []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из {filepath}")
                return data
            else:
                logger.error(f"Некорректный формат данных в {filepath}")
    except Exception as e:
        logger.error(f"Ошибка при чтении {filepath}: {e}")

    return []
