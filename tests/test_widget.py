import pytest

from src.widget import get_date, mask_account_card


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


@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-01T23:59:59", "01.12.2023"),
    ("2020-01-01", "01.01.2020")
])
def test_get_date_valid(date_string, expected):
    assert get_date(date_string) == expected


@pytest.mark.parametrize("invalid_input", [
    "invalid-date",
    "2024/03/11",
    "",        # пустая строка
    None       # тип не строка
])
def test_get_date_invalid(invalid_input):
    with pytest.raises(ValueError, match="Некорректный формат даты."):
        get_date(invalid_input)
