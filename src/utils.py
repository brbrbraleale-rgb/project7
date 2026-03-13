


import json

# 1. Добавляем импорт логера
from logger import setup_logger

# 2. Создаем объект логера (выполнит настройки handler и formatter)
logger = setup_logger('utils')


def get_financial_transactions(file_path: str) -> list:
    """
    Принимает путь до JSON-файла и возвращает список словарей.
    Отлавливает разные ошибки формата и пустые данные.
    """
    try:
        # Логируем начало выполнения
        logger.info(f"Попытка открыть файл по пути: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):
                # ЛОГИРОВАНИЕ: Успешно
                logger.info("Данные успешно загружены из JSON-файла")
                return data

            # ЛОГИРОВАНИЕ: Ошибка формата данных
            logger.error(f"Ошибка: ожидался список, получен {type(data)}")
            return []

    except FileNotFoundError:
        # ЛОГИРОВАНИЕ: Файл не найден (уровень ERROR)
        logger.error(f"Файл не найден: {file_path}")
        return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        # ЛОГИРОВАНИЕ: Ошибка внутри файла (уровень ERROR)
        logger.error(f"Ошибка декодирования или поврежденный JSON в файле: {file_path}")
        return []


if __name__ == "__main__":
    # Тест успешного случая (путь к json)
    get_financial_transactions("data/operations.json")

    # Тест ошибки (несуществующий файл)
    get_financial_transactions("non_existent.json")
