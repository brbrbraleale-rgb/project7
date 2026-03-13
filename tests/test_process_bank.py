import pytest

from process_bank import process_bank_operations
from process_bank import process_bank_search


def test_process_bank_search():
    """Тест фильтрации по описанию (регистронезависимый поиск)"""
    data = [
        {"description": "Перевод организации"},
        {"description": "Оплата кофе"},
        {"description": "Перевод со счета"}
    ]
    # Проверяем, что находит 2 перевода, игнорируя регистр
    assert len(process_bank_search(data, "перевод")) == 2
    # Проверяем, что при отсутствии совпадений вернет пустой список
    assert process_bank_search(data, "налоги") == []


def test_process_bank_operations():
    """Тест подсчета количества операций по категориям"""
    data = [
        {"description": "Перевод"},
        {"description": "Перевод"},
        {"description": "Оплата"}
    ]
    categories = ["Перевод", "Оплата", "Снятие"]
    result = process_bank_operations(data, categories)

    # Проверяем точные значения счетчика
    assert result["Перевод"] == 2
    assert result["Оплата"] == 1
    assert result["Снятие"] == 0  # Категория есть в списке, но нет в данных
