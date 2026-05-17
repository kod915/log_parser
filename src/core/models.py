from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator
@dataclass
class LogRecord:
    #Defines the structure of a log record    
    timestamp: datetime #The time when the log entry was created
    level: str #The severity level of the log (e.g., INFO, ERROR)
    message: str #The log message content
    client_ip: Optional[str] = None #The IP address of the client making the request
    status_code: Optional[int] = None #The HTTP status code returned by the server
    bytes_sent: Optional[int] = None #The number of bytes sent in the response

    @field_validator('status_code')
    @classmethod
    def validate_status_code(cls, v):
        if v is not None and (v < 100 or v > 599):
            raise ValueError(f'Invalid status code: {v}')
        return v
    
    @field_validator('client_ip')
    @classmethod
    def validate_ip(cls, v):
        if v is not None:
            parts = v.split('.')
            if len(parts) != 4:
                raise ValueError(f'Invalid IP: {v}')
        return v