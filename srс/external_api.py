import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Использует API для конвертации USD/EUR.
    """
    # 1. Извлекаем данные из вложенного словаря транзакции
    # Согласно структуре JSON: transaction['operationAmount']['amount']
    amount_data = transaction.get("operationAmount", {})
    amount = float(amount_data.get("amount", 0))
    currency = amount_data.get("currency", {}).get("code")

    # 2. Если валюта уже в рублях, конвертацию игнорируем
    if currency == "RUB":
        return amount

    # 3. Если валюта USD или EUR, делаем запрос к API
    if currency in ["USD", "EUR"]:
        # Используем 'pair' для прямой конвертации суммы
        url = f"https://v6.exchangerate-api.com{API_KEY}/pair/{currency}/RUB/{amount}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Проверка на ошибки (например, 404 или 401)
            data = response.json()

            # По документации этого API результат лежит в ключе 'conversion_result'
            return float(data.get("conversion_result", 0.0))

        except (requests.RequestException, ValueError, KeyError):
            # В случае любой ошибки возвращаем 0.0
            return 0.0

    # Если валюта не RUB/USD/EUR, возвращаем 0.0 или исходную сумму
    return 0.0
