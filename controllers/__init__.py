# controllers/__init__.py

# Import controllers more easily
from .main_controller import GlobalController
from .player_controller import PlayerController
from .tournament_controller import TournamentController


__all__ = [
    "GlobalController",
    "PlayerController",
    "TournamentController",
]
