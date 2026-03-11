import pandas as pd
import os


def read_financial_operations(file_path):
    """Считывает данные из CSV или XLSX и возвращает список словарей."""
    if not os.path.exists(file_path):
        return []
    try:
        if file_path.endswith('.csv'):
            # Считываем CSV с автоопределением разделителя
            df = pd.read_csv(file_path, sep=None, engine='python')
        else:
            # Считываем Excel
            df = pd.read_excel(file_path)

        # Преобразуем в список словарей, заменяя пустоты (NaN) на None
        return df.where(pd.notnull(df), None).to_dict(orient='records')
    except Exception:
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




