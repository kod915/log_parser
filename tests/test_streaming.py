import pytest
from unittest.mock import mock_open, patch
from src.utils.streaming import stream_log_lines

def test_streaming_normal_file():
    with patch('builtins.open', mock_open(read_data="line1\nline2\nline3\n")):
        lines = list(stream_log_lines('fake.log'))
        assert len(lines) == 3
        assert lines[0] == 'line1'

def test_streaming_empty_file():
    with patch('builtins.open', mock_open(read_data="")):
        lines = list(stream_log_lines('fake.log'))
        assert len(lines) == 0

def test_streaming_strips_newlines():
    with patch('builtins.open', mock_open(read_data="line1\nline2\n")):
        lines = list(stream_log_lines('fake.log'))
        assert lines[0] == 'line1'
        assert '\n' not in lines[0]
def test_streaming_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        lines = list(stream_log_lines('nonexistent.log'))
        assert lines == []  # Return empty list on file not found