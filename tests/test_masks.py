import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    (1234567812345678, "1234 56 ** 5678"),
    (1111222233334444, "1111 22 ** 4444"),
    (9999999999999999, "9999 99 ** 9999"),
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [
    "1234567812345678",  # строка
    None,                # None
    12.34,               # float
    "",                  # пустая строка
    [],                  # список
])
def test_get_mask_card_number_invalid_type(card_number):
    assert get_mask_card_number(card_number) == "Некорректный номер карты."


@pytest.mark.parametrize("card_number", [
    1234,                            # слишком короткий
    12345678901234,                  # 14 символов
    12345678901234567890,            # слишком длинный
    0,                               # ноль
    -1234567890123456                # отрицательный
])
def test_get_mask_card_number_invalid_length(card_number):
    assert get_mask_card_number(card_number) == "Длина карты должна состоять минимум  из 4, максимум из 16 символов."




@pytest.mark.parametrize("account, expected", [
    (12345678, "**5678"),
    (9876543210123456, "**3456"),
    (1234, "**1234"),
    (100000, "**0000")
])
def test_get_mask_account_valid(account, expected):
    assert get_mask_account(account) == expected


@pytest.mark.parametrize("account", [
    123,                             # меньше 4 символов
    12345678901234567890             # больше 16
])
def test_get_mask_account_invalid_length(account):
    with pytest.raises(ValueError, match="Номер счета должен состоять от 4 до 16 символов."):
        get_mask_account(account)