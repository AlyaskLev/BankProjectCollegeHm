from src.log_config import setup_logger

logger = setup_logger('masks', 'masks.log')


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты."""
    if not isinstance(card_number, int):
        logger.error("Некорректный тип номера карты: %s", type(card_number))
        return "Некорректный номер карты."
    elif card_number <= 0 or len(str(card_number)) != 16:
        logger.error("Неверная длина номера карты: %s", card_number)
        return "Длина карты должна состоять минимум из 4, максимум из 16 символов."

    masked = f"{str(card_number)[:4]} {str(card_number)[4:6]} ** {str(card_number)[12:]}"
    logger.debug("Маскированный номер карты: %s", masked)
    return masked


def get_mask_account(account: int) -> str:
    """Функция маскировки номера счета."""
    account_str = str(account)
    if len(account_str) < 4 or len(account_str) > 16:
        logger.error("Неверная длина номера счета: %s", account_str)
        raise ValueError("Номер счета должен состоять от 4 до 16 символов.")
    masked = f"**{account_str[-4:]}"
    logger.debug("Маскированный номер счета: %s", masked)
    return masked
