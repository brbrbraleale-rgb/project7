import json
import os

def get_financial_transactions(file_path: str) -> list:
    """
    Принимает путь до JSON-файла и возвращает список словарей.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    # Проверяем, существует ли файл по указанному пути
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Пытаемся загрузить данные из файла
            data = json.load(f)

            # Проверяем, что данные являются списком (согласно условию)
            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, UnicodeDecodeError):
        # Если файл пустой или содержит некорректный JSON, возвращаем пустой список
        return []
