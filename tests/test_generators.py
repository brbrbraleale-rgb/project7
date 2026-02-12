import pytest
from generators import filter_by_currency

def test_filter_by_currency_valid():
    """тест проверяет, что функция корректно находит транзакции с нужной валютой и игнорирует остальные"""
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "id": 1},
        {"operationAmount": {"currency": {"code": "RUB"}}, "id": 2},
        {"operationAmount": {"currency": {"code": "USD"}}, "id": 3},
    ]

    result = list(filter_by_currency(transactions, "USD"))

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_invalid_structure():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},  # Валидная
        {"invalid_key": "bad_data"},  # Вызовет KeyError
        None,  # Вызовет TypeError
        {"operationAmount": None}  # Вызовет TypeError
    ]

    result = list(filter_by_currency(transactions, "USD"))

    """ Возвращает только одну корректную транзакцию, остальные пропущены"""
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"
