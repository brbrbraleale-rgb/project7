import pytest

@pytest.fixture
def card_number_fixture():
    """Фикстура для стандартного номера карты"""
    return "0987654323454567"

@pytest.fixture
def account_number_fixture():
    """Фикстура для стандартного номера счета"""
    return "73654108430135874305"


@pytest.fixture
def simple_list():
    """Фикстура для сортировки и фильтрации набором данных"""
    return [
        {"state": "EXECUTED", "date": "2023-01-01"},
        {"state": "CANCELED", "date": "2024-01-01"}
    ]
