import logging
import os

# Получаем путь к корню проекта (на уровень выше src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к директории logs в корне проекта
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # создаст logs/, если нет


def setup_logger(name: str, filename: str, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:  # важно: чтобы не добавлять дубликаты
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, filename), mode="w", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
