# config.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# DATA Files

DATA_DIR = BASE_DIR / "data"
PLAYERS_FILE = DATA_DIR / "players.json"
TOURNAMENTS_FILE = DATA_DIR / "tournaments.json"


# Other Config

LOG_FILE = BASE_DIR / "logs" / "app.log"
