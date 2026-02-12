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


import pytest
from generators import transaction_descriptions

@pytest.mark.parametrize("index, expected_desc", [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Описание отсутствует")
])
def test_transaction_descriptions_logic(sample_transactions, index, expected_desc):
    """Тест проверяет корректность возвращаемых строк по индексам."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions[index] == expected_desc


@pytest.mark.parametrize("input_data, expected_length", [
    ([{"description": "A"}, {"description": "B"}], 2),
    ([], 0),
    ([{"no_desc": "X"}], 1)
])
def test_transaction_descriptions_structure(input_data, expected_length):
    """Тест проверяет работу генератора с разными входными структурами."""
    result = list(transaction_descriptions(input_data))
    assert len(result) == expected_length
