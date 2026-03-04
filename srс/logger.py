import logging
import os

# Получили путь к папке проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")  # Выходим из src в корень к logs

# Создаем папку
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def setup_logger(name):
    logger = logging.getLogger(name)

    # Путь будет: корень/logs/имя_модуля.log
    file_path = os.path.join(LOG_DIR, f"{name}.log")

    # mode='w' — перезапись, encoding='utf-8' — для русского
    file_handler = logging.FileHandler(file_path, mode='w', encoding='utf-8')

    # Формат
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    return logger
