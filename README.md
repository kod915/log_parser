# Nginx Log Parser

[![CI](https://github.com/kod915/log_parser/actions/workflows/ci.yaml/badge.svg)](https://github.com/kod915/log_parser/actions/workflows/ci.yaml)
[![Coverage](https://img.shields.io/badge/coverage-81%25-brightgreen)](https://github.com/kod915/log_parser)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A high-performance Nginx log parser that streams log files line-by-line and stores parsed data in SQLite database. Built with Python, Typer CLI, and SQLAlchemy Core for batch inserts.

## Features

- 📊 **Nginx Log Parsing** - Supports standard combined log format
- 💾 **SQLite Storage** - Lightweight database, no server setup required
- 🚀 **Streaming I/O** - Uses Python generators (yield) for files of any size
- 📦 **Bulk Inserts** - Efficiently saves thousands of records at once
- 🎯 **Type Hints** - Full typing support for better IDE experience
- 🧪 **Testing** - 81% code coverage with pytest and mocks
- 🔧 **CLI Interface** - User-friendly command line with Typer

## Requirements

- Python 3.10+
- pip (Python package manager)

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/nginx-log-parser.git
cd nginx-log-parser

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
## Usage
```bash
python app.py access.log
python app.py access.log --batch-size 500
python app.py --help
```
## Example 
```bash
echo '127.0.0.1 - - [27/Feb/2023:01:00:19 +0000] "GET / HTTP/1.1" 200 612' > test.log
python app.py test.log
```
## Project Structure
```
log_parser/
├── .github/workflows/ci.yaml
├── src/
│   ├── core/models.py
│   ├── parsers/nginx_parser.py
│   ├── utils/streaming.py
│   └── storage/database.py
├── tests/
├── app.py
├── requirements.txt
└── README.md
```
## Running Tests
```bash
pytest tests/ -v
pytest tests/ -v --cov=src --cov-report=term
pytest tests/ -v --cov=src --cov-report=html
```
## Author

kod915

