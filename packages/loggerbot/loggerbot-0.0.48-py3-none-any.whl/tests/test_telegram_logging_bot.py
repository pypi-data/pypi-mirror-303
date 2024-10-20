# © N.Sikharulidze (https://ubix.pro/)
import pytest
from unittest.mock import patch, MagicMock
from loggerbot import TelegramLoggingBot
import time

@pytest.fixture
def telegram_bot_single():
    return TelegramLoggingBot("test_token", "test_chat_id")

@pytest.fixture
def telegram_bot_multiple():
    return TelegramLoggingBot("test_token", ["test_chat_id_1", "test_chat_id_2"])

def test_initialization():
    with pytest.raises(ValueError):
        TelegramLoggingBot("", "")
    
    bot_single = TelegramLoggingBot("test_token", "test_chat_id")
    assert bot_single.tg_token == "test_token"
    assert bot_single.chat_ids == ["test_chat_id"]

    bot_multiple = TelegramLoggingBot("test_token", ["test_chat_id_1", "test_chat_id_2"])
    assert bot_multiple.tg_token == "test_token"
    assert bot_multiple.chat_ids == ["test_chat_id_1", "test_chat_id_2"]

@patch('requests.get')
def test_send_message_single(mock_get, telegram_bot_single):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_get.return_value = mock_response

    result = telegram_bot_single._send_message("TEST", "Test message")
    assert result is None  # _send_message now returns None as it only queues the message
    telegram_bot_single.message_queue.join()  # Wait for the queue to be processed
    mock_get.assert_called_once()

@patch('requests.get')
def test_send_message_multiple(mock_get, telegram_bot_multiple):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_get.return_value = mock_response

    result = telegram_bot_multiple._send_message("TEST", "Test message")
    assert result is None  # _send_message now returns None as it only queues the message
    telegram_bot_multiple.message_queue.join()  # Wait for the queue to be processed
    assert mock_get.call_count == 2

@patch('requests.get')
def test_log_levels(mock_get, telegram_bot_single):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_get.return_value = mock_response

    log_methods = [
        telegram_bot_single.debug,
        telegram_bot_single.info,
        telegram_bot_single.warning,
        telegram_bot_single.error,
        telegram_bot_single.critical,
        telegram_bot_single.alert,
        telegram_bot_single.complete
    ]

    for method in log_methods:
        result = method("Test message")
        assert result is None  # All log methods now return None as they only queue the message
        telegram_bot_single.message_queue.join()  # Wait for the queue to be processed
        mock_get.assert_called()
        mock_get.reset_mock()

def test_set_log_level(telegram_bot_single):
    import logging
    telegram_bot_single.set_log_level(logging.DEBUG)
    assert telegram_bot_single.logger.level == logging.DEBUG

def test_backward_compatibility():
    from loggerbot import LogBot
    assert LogBot is TelegramLoggingBot

@patch('time.sleep')
@patch('requests.get')
def test_rate_limiting(mock_get, mock_sleep, telegram_bot_single):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_get.return_value = mock_response

    # Set a lower rate limit for testing
    telegram_bot_single.rate_limit = 3
    telegram_bot_single.time_window = 10

    # Send messages at a rate higher than the limit
    for _ in range(5):
        telegram_bot_single._send_message("TEST", "Test message")

    # Wait for the queue to be processed
    telegram_bot_single.message_queue.join()

    # Check that sleep was called at least once (rate limiting in action)
    assert mock_sleep.call_count > 0

    # Check that all messages were eventually sent
    assert mock_get.call_count == 5
