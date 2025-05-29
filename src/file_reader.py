from pathlib import Path
from typing import Dict, List

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent


def read_transactions_from_csv(filename: str) -> List[Dict]:
    """Считывает транзакции из CSV-файла из папки data и возвращает список словарей."""
    file_path = BASE_DIR / "data" / filename
    df = pd.read_csv(file_path, sep=';')  # <-- указали правильный разделитель
    return df.to_dict(orient="records")


def read_transactions_from_excel(filename: str) -> List[Dict]:
    """Считывает транзакции из Excel-файла из папки data и возвращает список словарей."""
    file_path = BASE_DIR / "data" / filename
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


csv_data = read_transactions_from_csv("transactions.csv")
xlsx_data = read_transactions_from_excel("transactions_excel.xlsx")
