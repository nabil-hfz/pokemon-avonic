import unittest
from unittest.mock import patch

from utils import Logger


class TestLogger(unittest.TestCase):

    @patch('logging.debug')
    def test_log_debug(self, mock_debug):
        """Test that log_debug correctly calls Logger.debug."""
        message = "Debug message"
        Logger.log_debug(message)
        mock_debug.assert_called_once_with(message)

    @patch('logging.info')
    def test_log_info(self, mock_info):
        """Test that log_info correctly calls Logger.info."""
        message = "Information message"
        Logger.log_info(message)
        mock_info.assert_called_once_with(message)

    @patch('logging.error')
    def test_log_error(self, mock_error):
        """Test that log_error correctly calls Logger.error."""
        message = "Error message"
        Logger.log_error(message)
        mock_error.assert_called_once_with(message)
