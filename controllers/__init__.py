# controllers/__init__.py

# Import controllers more easily
from controllers.global_controller import GlobalController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.rapports_controller import RapportsController


__all__ = [
    "GlobalController",
    "PlayerController",
    "TournamentController",
    "RapportsController",
]
