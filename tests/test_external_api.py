from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get, monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")

    mock_resp = mock_get.return_value
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"rates": {"RUB": 75.0}}

    tx = {
        "operationAmount": {
            "amount": 100,
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rub(tx)
    assert isinstance(result, float)
    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get, monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")

    mock_resp = mock_get.return_value
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"rates": {"RUB": 90.0}}

    tx = {
        "operationAmount": {
            "amount": 50,
            "currency": {"code": "EUR"}
        }
    }

    result = convert_to_rub(tx)
    assert result == 4500.0


def test_convert_to_rub_rub_no_request(monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")
    called = False

    def fake_get(*args, **kwargs):
        nonlocal called
        called = True
        return None

    monkeypatch.setattr("src.external_api.requests.get", fake_get)

    tx = {
        "operationAmount": {
            "amount": 123.45,
            "currency": {"code": "RUB"}
        }
    }

    result = convert_to_rub(tx)
    assert result == 123.45
    assert called is False


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get, monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")

    mock_resp = mock_get.return_value
    mock_resp.status_code = 500
    mock_resp.json.return_value = {}

    tx = {
        "operationAmount": {
            "amount": 10,
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rub(tx)
    assert result == 0.0