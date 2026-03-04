import json
from unittest.mock import patch, mock_open
from utils import get_financial_transactions


def test_get_financial_transactions_valid_list():
    """ корректный JSON со списком транзакций"""
    mock_data = json.dumps([{"id": 1, "amount": "100.00"}, {"id": 2, "amount": "200.00"}])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_financial_transactions("fake_path.json")
        assert result == [{"id": 1, "amount": "100.00"}, {"id": 2, "amount": "200.00"}]


def test_get_financial_transactions_empty_or_invalid():
    """ файл не найден (возвращает пустой список)"""
    # Патчим os.path.exists, чтобы он вернул False
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        result = get_financial_transactions("non_existent.json")
        assert result == []


def test_get_financial_transactions_not_a_list():
    """ JSON содержит словарь вместо списка"""
    mock_data = json.dumps({"id": 1, "status": "error"})  # Это объект {}, а не список []

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = get_financial_transactions("wrong_format.json")
            assert result == []
