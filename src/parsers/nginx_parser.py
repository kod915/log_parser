import re
from datetime import datetime
from typing import Optional
from src.core.models import LogRecord

class NginxLogParser:

    PATTERN = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - '
        r'\[(?P<time>[^\]]+)\] '
        r'"(?P<method>[A-Z]+) (?P<url>\S+) HTTP/\d\.\d" '
        r'(?P<status>\d{3}) '
        r'(?P<bytes>\d+|-)'
    )

    def parse(self, line: str) -> Optional[LogRecord]:
        match = self.PATTERN.match(line)
        if not match:
            return None
        
        data = match.groupdict()
        

        time_str = data['time'].split()[0]
        timestamp = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S')
        

        status_code = int(data['status'])
        if status_code >= 500:
            level = "ERROR"
        elif status_code >= 400:
            level = "WARNING"
        else:
            level = "INFO"
        

        bytes_sent = int(data['bytes']) if data['bytes'] != '-' else None
        
        return LogRecord(
            timestamp=timestamp,
            level=level,
            message=f"{data['method']} {data['url']}",
            client_ip=data['ip'],
            status_code=status_code,
            bytes_sent=bytes_sent

        )
    