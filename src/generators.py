from typing import Any, Generator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Generator[dict[str, Any], None, None]:
    """
    Возвращает итератор для транзакций с заданной валютой.
    """
    for transaction in transactions:
        try:
            current_currency = transaction["operationAmount"]["currency"]["code"]
            if current_currency == currency:
                yield transaction
        except KeyError, TypeError:
            continue


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[str, None, None]:
    """
    Генератор, который поочередно возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        # Извлекаем описание, если его нет — выводим текст по умолчанию
        yield str(transaction.get("description", "Описание отсутствует"))


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.
    Диапазон включительный: от start до stop.
    """
    for number in range(start, stop + 1):
        # Форматируем число в строку из 16 цифр с ведущими нулями
        card_str = f"{number:016}"

        # Разбиваем на блоки по 4 цифры
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"

        yield formatted_card