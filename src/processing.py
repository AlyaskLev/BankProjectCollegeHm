from typing import Dict, List

input_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """функция для фильтрации списка словарей по ключу 'state'"""
    lower_state = state.lower()
    return [item for item in data if item.get("state", "").lower() == lower_state]


print(filter_by_state(input_data, state="executed"))
print(filter_by_state(input_data, state="canceled"))


def sort_by_date(date_list: List[Dict]) -> List[Dict]:
    """функция для сортировки списка словарей по датам"""
    return sorted(date_list, key=lambda x: x["date"], reverse=True)


print(sort_by_date(input_data))
