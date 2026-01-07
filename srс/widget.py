from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(number: str) -> str:
    """Функция вызывает импортированные функции, принимает номер карты или счёт и возвращает маску карты или счёта"""
    # Разделяем строку на название (текст) и номер (цифры)
    string = number.split()
    name = " ".join(string[:-1])  # Все, кроме последнего элемента (название карты/счета)
    number = string[-1]  # Последний элемент (сам номер)
    if "Счет" in name:
        # Если в названии есть слово "Счет", вызываем маску для счета
        masked_number = get_mask_account(number)
    else:
        # В остальных случаях вызываем маску для карты
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"

# Пример:
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
