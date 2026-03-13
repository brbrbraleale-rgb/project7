import os
from typing import Any, cast

import pandas as pd


def read_financial_operations(file_path: str) -> list[dict[str, Any]]:
    """Считывает данные из CSV или XLSX и возвращает список словарей."""
    if not os.path.exists(file_path):
        return []
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, sep=None, engine="python")
        else:
            df = pd.read_excel(file_path)

        # 1. Решаем ошибку типа через cast (говорим PyCharm, что ключи — это точно строки)
        data = df.astype(object).replace({pd.NA: None, float("nan"): None}).to_dict(orient="records")
        return cast(list[dict[str, Any]], data)

    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError):
        return []
    # noinspection PyBroadException
    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError, RuntimeError):
        return []




# Вводные данные (пути)
path_excel = r"C:\Users\Admin\Downloads\transactions_excel.xlsx"
path_csv = r"C:\Users\Admin\Downloads\transactions.csv"

# Проверка CSV
csv_data = read_financial_operations(path_csv)
print(f"CSV: Найдено {len(csv_data)} операций")
if csv_data:
    print(f"Первая запись CSV: {csv_data[0]}")

print("-" * 30)

# Проверка Excel
excel_data = read_financial_operations(path_excel)
print(f"Excel: Найдено {len(excel_data)} операций")
if excel_data:
    print(f"Первая запись Excel: {excel_data[0]}")
