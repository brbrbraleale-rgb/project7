def filter_by_currency(transactions, currency_code):
    """
    Возвращает итератор для транзакций с заданной валютой.
    """
    for transaction in transactions:
        try:
            current_currency = transaction["operationAmount"]["currency"]["code"]
            if current_currency == currency_code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions):
    """
    Генератор, который поочередно возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")
