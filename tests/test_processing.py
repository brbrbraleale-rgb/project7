import pytest
from processing import filter_by_state, sort_by_date



def test_filter_by_state_default(sample_data):
    """Проверка фильтрации по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

def test_filter_by_state_canceled(sample_data):
    """Проверка фильтрации по конкретному статусу"""
    result = filter_by_state(sample_data, state="CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_sort_by_date_ascending(sample_data):
    """Проверка сортировки от старых к новым (reverse=False)"""
    data_with_dates = [i for i in sample_data if "date" in i]
    result = sort_by_date(data_with_dates, reverse=False)
    assert result[0]["date"] == "2021-01-01"
    assert result[-1]["date"] == "2025-12-31"