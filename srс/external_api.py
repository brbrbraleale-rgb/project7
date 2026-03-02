import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Если конвертация невозможна, возвращает исходную сумму (не 0.0).
    """
    amount_data = transaction.get("operationAmount", {})
    amount = float(amount_data.get("amount", 0))
    currency = amount_data.get("currency", {}).get("code")

    # Если сумма 0 или валюта уже RUB, возвращаем как есть
    if amount == 0 or currency == "RUB":
        return amount

    # Поддерживаемые валюты для конвертации
    if currency in ["USD", "EUR"]:
        #  формат URL для v6 с указанием суммы
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/RUB/{amount}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Проверка успешного статуса и извлечение результата
            if data.get("result") == "success":
                return float(data.get("conversion_result", amount))
        except (requests.RequestException, ValueError, KeyError):
            # В случае ошибки API возвращаем исходную сумму, чтобы не терять данные
            return amount

    return amount



test_transaction = {
    "operationAmount": {
        "amount": "20.00",
        "currency": {"code": "USD"}
    }
}

# Вызов функции
result = convert_to_rub(test_transaction)
print(f"Результат конвертации: {result} RUB")
