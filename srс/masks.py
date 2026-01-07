def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты в виде строки и возвращает замаскированный номер карты: XXXX XX** **** XXXX"""
    first_block = card_number[0:4]
    two_block = card_number[4:6]
    masked_middle = "** ****"  # Маскируем 6 цифр как "** ****"
    last_block = card_number[12:16]

    return f"{first_block} {two_block}{masked_middle} {last_block}"


card_number = "0987654323454567"
print(get_mask_card_number(card_number))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу ** XXXX """
    masked_account = "**"
    first_block = account_number[-4:]
    return f"{masked_account} {first_block}"


account_number = "097654"
print(get_mask_account(account_number))
