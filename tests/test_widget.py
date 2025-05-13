import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def card_and_account_cases():
    return [
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98 ** 7658"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22 ** 4444"),
        ("Счет 1234567890123456", "Cчет **3456"),
        ("Счет 1234", "Cчет **1234"),
    ]


@pytest.mark.parametrize("input_str, expected", [
    ("Visa Gold 1234567812345678", "Visa Gold 1234 56 ** 5678"),
    ("Счет 9876543210987654", "Cчет **7654"),
])
def test_mask_account_card_basic(input_str, expected):
    assert mask_account_card(input_str) == expected


def test_mask_account_card_from_fixture(card_and_account_cases):
    for input_str, expected in card_and_account_cases:
        assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str", [
    "",  # пустая строка
    "Visa 1234abcd5678",  # некорректный номер карты
    "CardName OnlyText",  # без цифр
    "Счет abcdefg",       # счет с буквами
])
def test_mask_account_card_invalid_input(input_str):
    with pytest.raises(ValueError):
        mask_account_card(input_str)


@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2022-12-01T00:00:00.000000", "01.12.2022"),
])
def test_get_date_valid(input_date, expected):
    assert get_date(input_date) == expected


@pytest.mark.parametrize("invalid_date", [
    "invalid-date",
    "2024/03/11",
    "2024-03-11",  # без 'T'
    "",
    None,
])
def test_get_date_invalid(invalid_date):
    with pytest.raises((AttributeError, IndexError, TypeError)):
        get_date(invalid_date)
