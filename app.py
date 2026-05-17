import typer
from src.parsers.nginx_parser import NginxLogParser
from src.utils.streaming import stream_log_lines
from src.storage.database import LogRepository

app = typer.Typer()

@app.command()
def parse(file_path: str, batch_size: int = 1000):
    parser = NginxLogParser()
    repo = LogRepository(db_url='sqlite:///logs.db')
    batch = []

    typer.echo(f"Processing log file: {file_path}")
    for line in stream_log_lines(file_path):
        record = parser.parse(line)
        if record:
            batch.append(record)
        
        if len(batch) >= batch_size:
            
            repo.bulk_save(batch)
            batch = []

    if batch:
        repo.bulk_save(batch)
    typer.echo("Log parsing and storage completed.")

if __name__ == "__main__":
    app()