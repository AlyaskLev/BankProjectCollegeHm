import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return[
        {
            "id": 1,
            "operationAmount":{
                "currency":{"code":"USD"}
            }
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {"code": "EUR"}
            }
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {"code": "USD"}
            }
        },
    ]

def test_filter_by_currency_usd(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 1
    assert next(usd_transactions)["id"] == 3


def test_filter_by_currency_eur(sample_transactions):
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    assert next(eur_transactions)["id"] == 2


def test_filter_by_currency_empty(sample_transactions):
    empty_transactions = filter_by_currency(sample_transactions, "NO")
    with pytest.raises(StopIteration):
        next(empty_transactions)


@pytest.fixture
def sample_transaction_descriptions():
    return [
        {"description": "Перевод организации", "id": 1},
        {"description": "Перевод со счета на счет", "id": 2},
        {"description": "Перевод с карты на карту", "id": 3}
    ]


def test_transaction_descriptions(sample_transaction_descriptions):
    descriptions = transaction_descriptions(sample_transaction_descriptions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


def test_transaction_descriptions_empty():
    empty_transaction = []
    assert list(transaction_descriptions(empty_transaction)) == []


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999998, 9999999999999999, [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ])
])

def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError):
        list(card_number_generator(-1,5))
    with pytest.raises(ValueError):
        list(card_number_generator(10,5))
