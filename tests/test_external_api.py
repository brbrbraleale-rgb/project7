import unittest
from unittest.mock import patch
from external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    @patch('requests.get')
    def test_convert_to_rub_success(self, mock_get):
        """Тест успешной конвертации из USD в RUB"""
        # Настраиваем мок ответа API
        mock_get.return_value.json.return_value = {"conversion_result": 7500.0}
        mock_get.return_value.status_code = 200

        transaction = {
            "operationAmount": {
                "amount": "100.0",
                "currency": {"code": "USD"}
            }
        }

        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_convert_to_rub_api_error(self, mock_get):
        """Тест возврата 0.0 при ошибке запроса"""
        # Имитируем ошибку подключения
        mock_get.side_effect = Exception("API Connection Error")

        transaction = {
            "operationAmount": {
                "amount": "100.0",
                "currency": {"code": "EUR"}
            }
        }

        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
