# controllers/__init__.py

# Import controllers more easily
from .player_controller import PlayerController
from .tournament_controller import TournamentController


__all__ = [
    "PlayerController",
    "TournamentController",
]
