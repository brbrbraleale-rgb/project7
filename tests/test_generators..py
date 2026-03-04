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
        {"operationAmount": None},  # Вызовет TypeError
    ]

    result = list(filter_by_currency(transactions, "USD"))

    """ Возвращает только одну корректную транзакцию, остальные пропущены"""
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


from generators import transaction_descriptions


@pytest.mark.parametrize(
    "index, expected_desc",
    [
        (0, "Перевод организации"),
        (1, "Перевод со счета на счет"),
        (2, "Описание отсутствует"),
    ],
)
def test_transaction_descriptions_logic(sample_transactions, index, expected_desc):
    """Тест проверяет корректность возвращаемых строк по индексам."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions[index] == expected_desc


@pytest.mark.parametrize(
    "input_data, expected_length",
    [
        ([{"description": "A"}, {"description": "B"}], 2),
        ([], 0),
        ([{"no_desc": "X"}], 1),
    ],
)
def test_transaction_descriptions_structure(input_data, expected_length):
    """Тест проверяет работу генератора с разными входными структурами."""
    result = list(transaction_descriptions(input_data))
    assert len(result) == expected_length


from generators import card_number_generator

"""Проверка корректности формата и значений (используем фикстуру)"""


def test_card_generator_format(card_range_data):
    gen = card_number_generator(card_range_data["start"], card_range_data["stop"])
    result = list(gen)

    assert len(result) == 3
    assert result[0] == "0000 0000 0000 0001"
    assert result[-1] == "0000 0000 0000 0003"
    assert all(len(card) == 19 for card in result)


""" Параметризация для проверки различных диапазонов"""


@pytest.mark.parametrize(
    "start, stop, expected_len, first_val",
    [
        (10, 10, 1, "0000 0000 0000 0010"),
        (9999999999999998, 9999999999999999, 2, "9999 9999 9999 9998"),
        (1, 0, 0, None),  # Пустой диапазон
    ],
)
def test_card_generator_ranges(start, stop, expected_len, first_val):
    gen = list(card_number_generator(start, stop))

    assert len(gen) == expected_len
    if expected_len > 0:
        assert gen[0] == first_val