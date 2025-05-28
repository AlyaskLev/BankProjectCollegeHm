import os
import json

def load_transactions(filepath: str) -> list[dict]:
    """Загружает транзакции из JSON-файла"""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, IOError):
        return []

    return []
