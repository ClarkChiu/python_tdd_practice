from unittest.mock import patch

from python_tdd_practice.logger import Logger


@patch('python_tdd_practice.logger.datetime.datetime')
def test_log(mock_datetime):
    test_now = 123
    test_message = "A test message"
    mock_datetime.now.return_value = test_now

    test_logger = Logger()
    test_logger.log(test_message)
    assert test_logger.messages == [(test_now, test_message)]
