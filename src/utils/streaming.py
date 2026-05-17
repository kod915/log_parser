import logging

def stream_log_lines(file_path: str):
    #Memory efficient generator to read log lines from a file [3, 4]
    try:
        with open(file_path, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")