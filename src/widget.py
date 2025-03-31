from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_to_mask: str) -> str:
    """маскировка номер счета/карты"""
    info_to_mask_split = info_to_mask.split()
    if "Счет" in info_to_mask_split:
        return f"Cчет {get_mask_account(int(info_to_mask_split[1]))}"
    else:
        card_number: list[int] = []
        card_name = []
        for i in info_to_mask_split:
            if i.isdigit():
                card_number.extend(map(int, i))
            elif i.isalpha():
                card_name.append(i)
        str_card_number = "".join(map(str, card_number))
        str_card_name = " ".join(card_name)
        return f"{str_card_name} {get_mask_card_number(int(str_card_number))}"


print(mask_account_card("Visa Classic 6831982476737658"))


def get_date(date_string: str) -> str:
    """функция принимает дату в одном формате и преобразует её"""
    date_parts = date_string.split("T")[0].split("-")
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"


print(get_date("2024-03-11T02:26:18.671407"))
