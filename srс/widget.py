from masks import get_mask_account
from masks import get_mask_card_number


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


def get_date(date_string: str) -> str:
    """
        Принимает строку с датой в формате '2024-03-11T02:26:18.671407'
        и возвращает дату в формате 'ДД.ММ.ГГГГ/
    "11.03.2024")'.
    """
    # Извлекаем год, месяц и день с помощью срезов
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Собираем в нужном порядке
    return f"{day}.{month}.{year}"


# Пример:
date_ = "2024-03-11T02:26:18.671407"
print(get_date(date_))
