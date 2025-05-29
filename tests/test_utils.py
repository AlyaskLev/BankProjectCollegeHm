import json

import pytest

from src.utils import load_transactions


def test_load_transactions_valid(tmp_path):
    data = [{"amount": 100, "currency": "RUB"}, {"amount": 50, "currency": "USD"}]
    file = tmp_path / "ops.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file))
    assert isinstance(result, list)
    assert result == data


def test_load_transactions_empty_file(tmp_path):
    file = tmp_path / "empty.json"
    file.write_text("", encoding="utf-8")

    result = load_transactions(str(file))
    assert result == []


def test_load_transactions_not_list(tmp_path):
    file = tmp_path / "not_list.json"
    file.write_text(json.dumps({"a": 1}), encoding="utf-8")

    result = load_transactions(str(file))
    assert result == []


def test_load_transactions_missing_file():
    result = load_transactions("no_such_file.json")
    assert result == []