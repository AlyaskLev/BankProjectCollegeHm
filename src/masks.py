def get_mask_card_number(card_number: int) -> str:
    """функция маскировки номера карты"""
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


print(get_mask_card_number(7000792289606361))


def get_mask_account(account: int) -> str:
    """функция маскировки банковского счёта"""
    return f"**{str(account)[16:]}"


print(get_mask_account(73654108430135874305))
