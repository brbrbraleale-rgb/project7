import pytest
from widget import mask_account_card, get_date


def test_mask_account_card_visa(card_input):
    """Проверка правильного определения типа 'Карта'"""
    result = mask_account_card(card_input)
    assert "Visa Gold" in result
    assert "** ****" in result  # Проверка, что маска карты применилась

def test_mask_account_card_account(account_input):
    """Проверка правильного определения типа 'Счет'"""
    result = mask_account_card(account_input)
    assert "Счет" in result
    assert result.endswith("7890")  # Проверка, что маска счета (последние 4 цифры) работает



def test_get_date_simple(date_input):
    """Простая проверка преобразования формата даты"""
    assert get_date(date_input) == "20.05.2024"

@pytest.mark.parametrize("input_date, expected", [
    ("2025-12-31T23:59:59", "31.12.2025"),
    ("2000-01-01T00:00:00", "01.01.2000")
])
def test_get_date_variants(input_date, expected):
    """Параметризованный тест для разных дат"""
    assert get_date(input_date) == expected

