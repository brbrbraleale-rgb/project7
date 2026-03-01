import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Принимает транзакцию и возвращает сумму в рублях через ExchangeRate-API."""

    # Извлекли данные
    amount_data = transaction.get("operationAmount", {})
    amount = float(amount_data.get("amount", 0))
    currency = amount_data.get("currency", {}).get("code")

    # Если уже в рублях возвращаем как есть
    if currency == "RUB":
        return amount

    # Конвертация для USD или EUR
    if currency in ["USD", "EUR"]:
        # Исправленный URL: добавлен v6 и правильные слеши по совету из интернета
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/RUB/{amount}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Проверяем, что API вернуло статус "success" по совету из интернета
            if data.get("result") == "success":
                return float(data.get("conversion_result", 0.0))

        except (requests.RequestException, ValueError, KeyError):
            return 0.0

    return 0.0
