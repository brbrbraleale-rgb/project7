from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция принимает список словарей и возвращает новый список,
    содержащий только те элементы, у которых state совпадает с заданным.
    """
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Функция принимает список словарей и возвращает новый список,
    отсортированный по ключу 'date'.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
