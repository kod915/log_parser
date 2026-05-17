import sqlite3
from dataclasses import asdict
#A bulk insert allows the engine to send a single SQL statement to the database containing thousands of records, which is significantly faster than executing thousands of individual INSERT statements.
class LogRepository:
    def __init__(self, db_url: str):
        db_path = db_url.replace('sqlite:///', '')
        self.conn = sqlite3.connect(db_path)
        self.create_table()
    
    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                level TEXT,
                message TEXT,
                client_ip TEXT,
                status_code INTEGER,
                bytes_sent INTEGER
            )
        ''')
        self.conn.commit()
    
    def bulk_save(self, records: list):

        
        data = []
        for record in records:
            record_dict = asdict(record)

            record_dict['timestamp'] = str(record_dict['timestamp'])
            data.append(record_dict)
            print(f"   Rekord: {record_dict['client_ip']} - {record_dict['status_code']}")
        
        cursor = self.conn.cursor()
        cursor.executemany('''
            INSERT INTO logs (timestamp, level, message, client_ip, status_code, bytes_sent)
            VALUES (:timestamp, :level, :message, :client_ip, :status_code, :bytes_sent)
        ''', data)
        self.conn.commit()