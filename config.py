# config.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# DATA Files

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

PLAYERS_FILE = DATA_DIR / "players.json"
if not PLAYERS_FILE.exists():
    PLAYERS_FILE.touch()

TOURNAMENTS_FILE = DATA_DIR / "tournaments.json"
if not TOURNAMENTS_FILE.exists():
    TOURNAMENTS_FILE.touch()


# Other Config

LOG_FILE = BASE_DIR / "logs" / "app.log"
