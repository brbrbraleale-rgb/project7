from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """
    Функция принимает список словарей и возвращает новый список,
    содержащий только те элементы, у которых state совпадает с заданным.
    """
    result = []
    for item in data:
        if item.get('state') == state:
            result.append(item)
    return result
