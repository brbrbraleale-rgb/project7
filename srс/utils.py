import json

def get_financial_transactions(file_path: str) -> list:
    """
    Принимает путь до JSON-файла и возвращает список словарей.
    Отлавливает разные ошибки формата и пустые данные.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            # Проверяем, что данные являются списком
            if isinstance(data, list):
                return data
            return []

    except FileNotFoundError:
        # Прямая обработка отсутствия файла по требованию проверяющего
        return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        # Если файл поврежден, пуст или в неверной кодировке
        return []
