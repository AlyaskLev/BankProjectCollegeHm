from unittest.mock import patch

import pandas as pd

from src.file_reader import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    mock_data = [{"date": "2024-01-01", "amount": 100, "currency": "USD"}]
    mock_read_csv.return_value = pd.DataFrame(mock_data)

    result = read_transactions_from_csv("transactions.csv")

    assert result == mock_data
    mock_read_csv.assert_called_once()


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_data = [{"date": "2024-01-02", "amount": 200, "currency": "EUR"}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = read_transactions_from_excel("transactions_excel.xlsx")

    assert result == mock_data
    mock_read_excel.assert_called_once()