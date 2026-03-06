import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub

class TestConvertToRub(unittest.TestCase):

    @patch('requests.get')
    def test_convert_to_rub_success(self, mock_get):
        """Тест успешной конвертации: добавляем 'result': 'success' в мок"""
        # Настраиваем, чтобы он прошел проверку if data.get("result") == "success"
        mock_get.return_value.json.return_value = {
            "result": "success",
            "conversion_result": 7500.0
        }
        mock_get.return_value.status_code = 200

        transaction = {
            "operationAmount": {
                "amount": "100.0",
                "currency": {"code": "USD"}
            }
        }

        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @patch('requests.get')
    def test_convert_to_rub_api_error(self, mock_get):
        import requests
        # Имитируем ошибку, которую ваша функция точно ловит
        mock_get.side_effect = requests.RequestException("API Error")

        transaction = {
            "operationAmount": {
                "amount": "100.0",
                "currency": {"code": "EUR"}
            }
        }

        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)

if __name__ == '__main__':
    unittest.main()




