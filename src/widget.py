from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_to_mask: str) -> str:
    """Маскировка номера счёта или карты."""
    info_to_mask_split = info_to_mask.split()
    if not info_to_mask_split:
        raise ValueError("Пустая строка")

    if "Счет" in info_to_mask_split or "Счёт" in info_to_mask_split:
        try:
            account_number = int(info_to_mask_split[1])
            return f"Cчет {get_mask_account(account_number)}"
        except (IndexError, ValueError):
            raise ValueError("Некорректный номер счёта.")

    card_number: list[int] = []
    card_name = []
    for i in info_to_mask_split:
        if i.isdigit():
            card_number.extend(map(int, i))
        elif i.isalpha():
            card_name.append(i)

    if not card_number:
        raise ValueError("Некорректный номер карты.")

    str_card_number = "".join(map(str, card_number))
    str_card_name = " ".join(card_name)

    if not str_card_number or not str_card_name:
        raise ValueError("Неполные данные для маскировки карты.")

    return f"{str_card_name} {get_mask_card_number(int(str_card_number))}"


def get_date(date_string: str) -> str:
    """Преобразование строки даты из формата YYYY-MM-DDTHH:MM:SS в DD.MM.YYYY."""
    try:
        date_parts = date_string.split("T")[0].split("-")
        return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
    except (AttributeError, IndexError):
        raise ValueError("Некорректный формат даты.")
