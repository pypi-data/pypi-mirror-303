import pytest
from unittest.mock import patch
from src.random_interrupt.main import send_notification

@patch('src.random_interrupt.main.notification')
def test_notification_called(mock_notification):
    send_notification("Test Title", "Test Message", 15)
    mock_notification.notify.assert_called_once_with(
        title="Test Title",
        message="Test Message",
        app_icon=None,
        timeout=15
    )

def test_notification_default_values():
    with patch('src.random_interrupt.main.notification') as mock_notification:
        send_notification("Random Interrupt", "Time for a break!", 10)
        mock_notification.notify.assert_called_once_with(
            title="Random Interrupt",
            message="Time for a break!",
            app_icon=None,
            timeout=10
        )

def test_notification_different_messages():
    with patch('src.random_interrupt.main.notification') as mock_notification:
        send_notification("Title 1", "Message 1", 5)
        send_notification("Title 2", "Message 2", 15)
        
        assert mock_notification.notify.call_count == 2
        mock_notification.notify.assert_any_call(
            title="Title 1",
            message="Message 1",
            app_icon=None,
            timeout=5
        )
        mock_notification.notify.assert_any_call(
            title="Title 2",
            message="Message 2",
            app_icon=None,
            timeout=15
        )
