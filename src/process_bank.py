import re
from collections import Counter

def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Фильтрует список транзакций по наличию строки поиска в описании (description).
    """
    # Создаем паттерн. re.IGNORECASE.
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    result = []
    for operation in data:
        # Проверяем наличие ключа 'description' и ищем в нем совпадение
        description = operation.get('description', '')
        if re.search(pattern, description):
            result.append(operation)

    return result



def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Считает количество операций для каждой категории из заданного списка.
    """
    # Собираем все описания из транзакций (только те, что есть в списке категорий)
    descriptions = [
        op.get('description') for op in data
        if op.get('description') in categories
    ]

    # Counter создаст словарь с подсчетом вхождений
    counts = Counter(descriptions)

    # Если нужно, чтобы в итоговом словаре были те категории,
    # по которым 0 операций дополнить результат:
    return {category: counts.get(category, 0) for category in categories}




