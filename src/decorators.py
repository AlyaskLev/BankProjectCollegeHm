import logging
from functools import wraps

def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # настройка логирования
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            # создание обработчика для вывода в консоль
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            if filename:
                # если передан filename, то логируем в файл
                file_handler = logging.FileHandler(filename)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")  # логируем успешный вызов функции
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # повторно поднимаем ошибку

        return wrapper

    return decorator