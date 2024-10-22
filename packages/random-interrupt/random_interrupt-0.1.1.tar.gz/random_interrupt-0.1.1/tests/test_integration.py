import pytest
from unittest.mock import patch
from src.random_interrupt.main import main
import sys

@patch('src.random_interrupt.main.send_notification')
@patch('src.random_interrupt.main.time.sleep')
def test_full_run(mock_sleep, mock_send_notification):
    with patch('sys.argv', ['main.py', '--overall-time', '60', '--number-of-interrupts', '5']):
        main()

    assert mock_send_notification.call_count == 5
    assert mock_sleep.call_count >= 4  # At least 4 sleeps between 5 interrupts

@patch('src.random_interrupt.main.send_notification')
@patch('src.random_interrupt.main.time.sleep')
def test_run_with_custom_notification(mock_sleep, mock_send_notification):
    with patch('sys.argv', ['main.py', '--overall-time', '60', '--number-of-interrupts', '5', 
                            '--notification-title', 'Custom Title', '--notification-message', 'Custom Message', 
                            '--notification-timeout', '20']):
        main()

    assert mock_send_notification.call_count == 5
    mock_send_notification.assert_called_with('Custom Title', 'Custom Message', 20)

@patch('src.random_interrupt.main.send_notification')
@patch('src.random_interrupt.main.time.sleep')
def test_run_with_min_gap(mock_sleep, mock_send_notification):
    with patch('sys.argv', ['main.py', '--overall-time', '60', '--number-of-interrupts', '5', '--min-gap', '5']):
        main()

    assert mock_send_notification.call_count == 5
    assert mock_sleep.call_count >= 4  # At least 4 sleeps between 5 interrupts

@patch('src.random_interrupt.main.send_notification')
@patch('src.random_interrupt.main.time.sleep')
def test_run_with_invalid_input(mock_sleep, mock_send_notification):
    with patch('sys.argv', ['main.py', '--overall-time', '-60', '--number-of-interrupts', '5']):
        with pytest.raises(ValueError, match="Overall time must be positive"):
            main()

    assert mock_send_notification.call_count == 0
    assert mock_sleep.call_count == 0
