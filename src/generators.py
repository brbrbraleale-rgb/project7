def filter_by_currency(transactions, currency_code):
    """
    Возвращает итератор для транзакций с заданной валютой.
    """
    for transaction in transactions:
        try:
            current_currency = transaction["operationAmount"]["currency"]["code"]
            if current_currency == currency_code:
                yield transaction
        except KeyError, TypeError:
            continue


def transaction_descriptions(transactions):
    """
    Генератор, который поочередно возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, stop):
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.
    Диапазон включительный: от start до stop.
    """
    for number in range(start, stop + 1):
        card_str = f"{number:016}"

        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"

        yield formatted_card