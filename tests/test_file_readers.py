import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
#импорт правильный ли?
from file_readers import read_financial_operations


class TestFinancialReading(unittest.TestCase):

    @patch('os.path.exists')
    @patch('pandas.read_csv')
    def test_read_csv_success(self, mock_read_csv, mock_exists):
        # Имитируем, что файл существует
        mock_exists.return_value = True
        # Имитируем данные pandas
        mock_df = pd.DataFrame([{'date': '2023-10-01', 'amount': 100}])
        mock_read_csv.return_value = mock_df

        result = read_financial_operations('fake_path.csv')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], 100)

    @patch('os.path.exists')
    @patch('pandas.read_excel')
    def test_read_excel_success(self, mock_read_excel, mock_exists):
        # Имитируем, что файл существует
        mock_exists.return_value = True
        # Имитируем данные pandas
        mock_df = pd.DataFrame([{'date': '2023-10-02', 'amount': 500}])
        mock_read_excel.return_value = mock_df

        result = read_financial_operations('fake_path.xlsx')

        # Теперь result
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['date'], '2023-10-02')


if __name__ == '__main__':
    unittest.main()

