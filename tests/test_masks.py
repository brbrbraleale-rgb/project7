import pytest
from masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(card_number_standard):
    """Проверка корректности маскировки номера карты"""
    result = get_mask_card_number(card_number_standard)
    assert result == "0987 65** **** 4567"

def test_get_mask_account(account_number_short):
    """Проверка маскировки номера счета (последние 4 цифры)"""
    result = get_mask_account(account_number_short)
    assert result == "** 7654"

def test_transaction_list_filtering(transaction_list):
    """Тест логики обработки списка словарей из фикстуры"""
    executed = [t for t in transaction_list if t["state"] == "EXECUTED"]
    assert len(executed) == 2



