import pytest

@pytest.fixture
def card_number_standard():
    """Стандартный номер карты"""
    return "0987654323454567"

@pytest.fixture
def account_number_short():
    """Короткий номер счета"""
    return "097654"

@pytest.fixture
def transaction_list():
    """Список словарей с различными статусами state"""
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "PENDING"}
    ]
