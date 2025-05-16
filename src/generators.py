from typing import Any, Dict, Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по валюте и возвращает итератор."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(transactions: list[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции по очереди."""
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    if not (1 <= start <= 9999999999999999):
        raise ValueError("start must be in range 1..9999999999999999")
    if not (1 <= stop <= 9999999999999999):
        raise ValueError("stop must be in range 1..9999999999999999")
    if start > stop:
        raise ValueError("start must be less than or equal to stop")

    for number in range(start, stop + 1):
        card_num = f"{number:016d}"
        yield ' '.join([card_num[i:i+4] for i in range(0, 16, 4)])

