import pytest
from processing import filter_by_state, sort_by_date


def test_filter_executed(simple_list):
    """Проверка, что остается только EXECUTED"""
    result = filter_by_state(simple_list, "EXECUTED")
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"

def test_filter_empty(simple_list):
    """Проверка, что при отсутствии совпадений список пуст"""
    result = filter_by_state(simple_list, state="PENDING")
    assert len(result) == 0


@pytest.mark.parametrize("reverse_flag, expected_date", [
    (True, "2024-01-01"),  # Сначала свежая дата
    (False, "2023-01-01")  # Сначала старая дата
])
def test_sort_order(simple_list, reverse_flag, expected_date):
    """Проверка направления сортировки (прямая и обратная)"""
    result = sort_by_date(simple_list, reverse=reverse_flag)
    assert result[0]["date"] == expected_date

def test_sort_result_length(simple_list):
    """Проверка, что после сортировки количество элементов не изменилось"""
    result = sort_by_date(simple_list)
    assert len(result) == 2



