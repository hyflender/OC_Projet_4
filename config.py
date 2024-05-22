# config.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Jinja2 template and rapport files
TEMPLATE_DIR = BASE_DIR / "views" / "templates"
TEMPLATE_DIR.mkdir(exist_ok=True)

# Reports
# Check if the 'data' directory exists, if not, create it
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

REPORT_DIR = BASE_DIR / "data" / "reports"
REPORT_DIR.mkdir(exist_ok=True)

# Flake8_Report
FLAKE8_REPORT_DIR = BASE_DIR / "flake8_report"
FLAKE8_REPORT_DIR.mkdir(exist_ok=True)


PLAYERS_FILE = DATA_DIR / "players.json"
if not PLAYERS_FILE.exists():
    PLAYERS_FILE.touch()

TOURNAMENTS_FILE = DATA_DIR / "tournaments.json"
if not TOURNAMENTS_FILE.exists():
    TOURNAMENTS_FILE.touch()


# Logs directory and file
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
