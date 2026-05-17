import pytest
from datetime import datetime
from src.core.models import LogRecord

def test_logrecord_creation():
    # Creation of a LogRecord with all fields
    record = LogRecord(
        timestamp=datetime.now(),
        level="INFO",
        message="Test message",
        client_ip="192.168.1.1",
        status_code=200,
        bytes_sent=1024
    )
    assert record.client_ip == "192.168.1.1"
    assert record.status_code == 200

def test_logrecord_optional_fields():
    # Creation of a LogRecord with only required fields
    record = LogRecord(
        timestamp=datetime.now(),
        level="ERROR",
        message="Error message"
    )
    assert record.client_ip is None
    assert record.status_code is None
    assert record.bytes_sent is None

def test_logrecord_with_minimal_data():
    # Creation of a LogRecord with minimal data
    record = LogRecord(
        timestamp=datetime.now(),
        level="WARNING",
        message="Warning"
    )
    assert record.level == "WARNING"



def test_logrecord_invalid_status_code():
    record = LogRecord(
        timestamp=datetime.now(),
        level="INFO",
        message="Test",
        status_code=999
    )
    assert record.status_code == 999