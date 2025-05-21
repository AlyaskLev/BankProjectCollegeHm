import pytest
import logging
from pathlib import Path


from src.decorators import log

@pytest.fixture(autouse=True)
def clear_log_handlers():
    root_logger = logging.getLogger()
    while root_logger.hasHandlers():
        root_logger.removeHandler(root_logger.handlers.pop())

@pytest.fixture
def caplog(caplog):
    yield caplog

def test_successful_function_execution(caplog):
    @log()
    def my_func():
        pass

    my_func()
    records = caplog.records
    assert any(record.message == 'my_func ok' for record in records), "Сообщение о выполнении функции отсутствует"

def test_function_exception(caplog):
    @log()
    def faulty_function():
        raise ValueError('Test exception occurred')

    with pytest.raises(ValueError):
        faulty_function()

    records = caplog.records
    assert any(
        record.levelname == 'ERROR' and 'faulty_function error:' in record.message
        for record in records
    ), "Ошибка не была зафиксирована в логе"

def test_file_logging():
    logfile = "./log.txt"  # Постоянный путь к файлу
    @log(logfile)
    def write_to_file():
        pass

    write_to_file()
    assert Path(logfile).exists(), "Лог-файл не был создан."
    with open(logfile, 'r') as f:
        contents = f.read().strip()
        assert 'write_to_file ok' in contents, "Запись в файл отсутствовала"

def test_correct_function_name(caplog):
    """Проверяет правильное отображение имени функции в логах."""
    @log()
    def another_function():
        pass

    another_function()
    records = caplog.records
    assert any(record.message == 'another_function ok' for record in records), "Имя функции неверно указано в логе"

def test_multiple_calls(caplog):
    @log()
    def multiple_call_function():
        pass

    for _ in range(3):
        multiple_call_function()

    records = caplog.records
    messages = [record.message for record in records]
    assert len(messages) == 3 and all(message.endswith('ok') for message in messages), \
           "Ожидалось три отдельных строки логов с успешным выполнением"

# запускает тесты
if __name__ == "__main__":
    pytest.main(['-v', '-s'])