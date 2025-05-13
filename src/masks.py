def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты."""
    if not isinstance(card_number, int):
        return "Некорректный номер карты."
    elif card_number <= 0 or len(str(card_number)) != 16:
        return "Длина карты должна состоять минимум  из 4, максимум из 16 символов."

    return f"{str(card_number)[:4]} {str(card_number)[4:6]} ** {str(card_number)[12:]}"


def get_mask_account(account: int) -> str:
    """Функция маскировки номера счета."""
    account_str = str(account)
    if len(account_str) < 4 or len(account_str) > 16:
        raise ValueError("Номер счета должен состоять от 4 до 16 символов.")
    return f"**{account_str[-4:]}"
