import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2022-01-01T10:00:00.000000'},
        {'id': 2, 'state': 'executed', 'date': '2021-05-10T12:00:00.000000'},
        {'id': 3, 'state': 'CANCELED', 'date': '2022-01-01T10:00:00.000000'},
        {'id': 4, 'state': 'FAILED', 'date': '2019-11-30T09:45:00.000000'},
        {'id': 5, 'state': '', 'date': '2020-06-15T15:00:00.000000'},
    ]


@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 2]),
    ("executed", [1, 2]),
    ("CANCELED", [3]),
    ("FAILED", [4]),
    ("UNKNOWN", []),
    ("", [5])
])
def test_filter_by_state(sample_data, state, expected_ids):
    result = filter_by_state(sample_data, state)
    result_ids = [item['id'] for item in result]
    assert result_ids == expected_ids


def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_same_dates():
    data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2022-01-01T10:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2022-01-01T10:00:00.000000'}
    ]
    result = sort_by_date(data)
    assert result == data  # порядок сохраняется


def test_sort_by_date_invalid_format():
    data = [
        {'id': 1, 'state': 'EXECUTED', 'date': 'not-a-date'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-01T10:00:00.000000'}
    ]
    with pytest.raises(TypeError):
        sort_by_date(data)
