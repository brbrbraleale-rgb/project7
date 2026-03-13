import os

from file_readers import read_financial_operations
from generators import filter_by_currency
from process_bank import process_bank_search
from processing import filter_by_state
from processing import sort_by_date
# Импортируем функции из модулей папки src
from utils import get_financial_transactions
from widget import get_date
from widget import mask_account_card


def main():

    data = []

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Первый input для выбора файла
    choice = input("Пользователь: ")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        # Здесь логика загрузки JSON
        file_path = os.path.join('data', 'operations.json')

        # вызов готовой функции теперь она станет цветной в импорте
        data = get_financial_transactions(file_path)
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")

        # Здесь логика загрузки CSV
        file_path = os.path.join('data', 'transactions.csv')
        data = read_financial_operations(file_path)
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        # Здесь логика загрузки XLSX
        file_path = os.path.join('data', 'transactions.xlsx')
        data = read_financial_operations(file_path)

    else:
        # ЗАВЕРШЕНИЕ: Если выбор не 1, 2 или 3, выводим ошибку и выходим из функции.
        print("Программа: Ошибка. Такого пункта меню нет.")
        return  # Этот оператор остановит выполнение main

        # если программа дошла сюда, 'data' существует.
    if not data:
        print("Программа: Данные не найдены или файл пуст.")
        return

    # Список допустимых статусов в верхнем регистре
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        user_status = input("Пользователь: ").strip().upper()  # Приводим к единому регистру

        if user_status in valid_statuses:
            # Вызываем функцию (из модуля processing)
            # Она получит список словарей и строку, например "EXECUTED"
            data = filter_by_state(data, user_status)

            print(f"Программа: Операции отфильтрованы по статусу \"{user_status}\"")
            break  # Успешно отфильтровали, выходим из цикла
        else:
            # Если ввели "test" или что-то другое
            print(f"Программа: Статус операции \"{user_status}\" недоступен.")
            # Цикл пойдет на новый круг и снова напечатает "Введите статус"

    # Сортировка по дате
    is_sort = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if is_sort == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        # Если в ответе есть "убыв", ставим True, иначе False (возрастание)
        is_reverse = True if "убыв" in order else False
        data = sort_by_date(data, is_reverse)

    # Фильтрация по валюте (только рубли)
    only_rub = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()

    if only_rub == "да":
        # Вызываем функцию-итератор и сразу превращаем результат в список
        data = list(filter_by_currency(data, "RUB"))
        print("Программа: Отфильтровано. Оставлены только рублевые транзакции.")
    else:
        print("Программа: Выводятся транзакции во всех валютах.")

    # Фильтрация по ключевому слову в описании
    is_filter_desc = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if is_filter_desc == "да":
        search_query = input("Введите строку для поиска: ")
        # Использую ту самую функцию с регулярными выражениями, которую писала в начале
        data = process_bank_search(data, search_query)

    # итоговая распечатка
    print("\nПрограмма: Распечатываю итоговый список транзакций...")

    if not data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Программа: Всего банковских операций в выборке: {len(data)}\n")

        for op in data:
            # Дата и описание
            date_formatted = get_date(op.get('date', ''))
            print(f"{date_formatted} {op.get('description', 'Без описания')}")

            # Маскировка счетов
            from_info = op.get('from')
            to_info = op.get('to')
            if from_info:
                print(f"{mask_account_card(from_info)} -> {mask_account_card(to_info)}")
            else:
                print(f"{mask_account_card(to_info)}")

            # Сумма
            amount = op.get('operationAmount', {}).get('amount')
            currency = op.get('operationAmount', {}).get('currency', {}).get('name')
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
