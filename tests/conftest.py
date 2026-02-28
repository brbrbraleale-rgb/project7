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


@pytest.fixture
def card_input():
    """Простая строка с данными карты"""
    return "Visa Gold 1234567812345678"

@pytest.fixture
def account_input():
    """Простая строка с данными счета"""
    return "Счет 12345678901234567890"

@pytest.fixture
def date_input():
    """Строка с датой в данном формате"""
    return "2024-05-20T10:00:00"
  

@pytest.fixture
def sample_transactions():
    """Фикстура с набором данных для тестов."""
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3},  # отсутствует
    ]


@pytest.fixture
def card_range_data():
    """Фикстура, возвращающая параметры для диапазона генерации."""
    return {"start": 1, "stop": 3}



@pytest.fixture
def get_log(capsys):
    """Фикстура возвращает функцию, которая читает последний вывод консоли."""
    def _read():
        return capsys.readouterr().out.strip()
    return _read
