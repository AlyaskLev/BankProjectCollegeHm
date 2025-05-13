from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    target_state = state.lower()
    return [item for item in data if item.get("state", "").lower() == target_state]


def sort_by_date(date_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Сортирует список словарей по ключу 'date' в порядке убывания.    """
    try:
        return sorted(
            date_list,
            key=lambda x: datetime.fromisoformat(x["date"]),
            reverse=True
        )
    except (KeyError, ValueError, TypeError) as e:
        raise TypeError(f"Ошибка сортировки по дате: {e}")
