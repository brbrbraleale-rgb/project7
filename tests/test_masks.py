import pytest
from masks import get_mask_card_number, get_mask_account

# Тесты для get_mask_card_number
@pytest.mark.parametrize("card_in, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("0000000000000000", "0000 00** **** 0000")
])
def test_get_mask_card_number_param(card_in, expected):
    """тест маскировки карты"""
    assert get_mask_card_number(card_in) == expected

def test_get_mask_card_number_fixture(card_number_fixture):
    """Тест маскировки карты с использованием фикстуры"""
    assert get_mask_card_number(card_number_fixture) == "0987 65** **** 4567"


# Тесты для get_mask_account
@pytest.mark.parametrize("acc_in, expected", [
    ("12345678901234567890", "** 7890"),
    ("11112222", "** 2222")
])
def test_get_mask_account_param(acc_in, expected):
    """ тест маскировки счета"""
    assert get_mask_account(acc_in) == expected

def test_get_mask_account_fixture(account_number_fixture):
    """Тест маскировки счета с использованием фикстуры"""
    assert get_mask_account(account_number_fixture) == "** 4305"


