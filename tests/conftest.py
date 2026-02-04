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

@pytest.fixture
def sample_data():
    """Различные комбинации state и date для тестов"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-05-20"},
        {"id": 3, "state": "EXECUTED", "date": "2025-12-31"},
        {"id": 4, "state": "PENDING", "date": "2022-10-10"},
        {"id": 5, "date": "2021-01-01"}  # Случай без ключа state
    ]


