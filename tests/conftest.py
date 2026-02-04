import pytest

@pytest.fixture
def card_number_fixture():
    """Фикстура для стандартного номера карты"""
    return "0987654323454567"

@pytest.fixture
def account_number_fixture():
    """Фикстура для стандартного номера счета"""
    return "73654108430135874305"
