from widget import mask_account_card, get_date



def test_mask_account_card_visa(card_data):
    """Проверка маскировки карты Visa"""
    result = mask_account_card(card_data)
    assert "Visa Platinum" in result
    assert "*" in result

def test_mask_account_card_account(account_data):
    """Проверка маскировки счета"""
    result = mask_account_card(account_data)
    assert "Счет" in result
    assert result.endswith(account_data[-4:])


def test_get_date_valid(raw_date_string):
    """Проверка правильности преобразования формата даты"""
    assert get_date(raw_date_string) == "11.03.2024"



