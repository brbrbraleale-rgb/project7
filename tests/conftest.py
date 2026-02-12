import pytest

@pytest.fixture
def sample_transactions():
    """Фикстура с набором данных для тестов."""
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3} #отсутствует
    ]


import pytest

@pytest.fixture
def card_range_data():
    """Фикстура, возвращающая параметры для диапазона генерации."""
    return {"start": 1, "stop": 3}
