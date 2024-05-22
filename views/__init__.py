# views/__init__.py

# Import views more easily
from .main_view import MainView, ShowPlateau
from .player_view import PlayerView
from .matchs_view import MatchsView
from .tournament_view import TournamentView
from .rapports_view import RapportsView

__all__ = [
    "MainView",
    "ShowPlateau",
    "PlayerView",
    "MatchsView",
    "TournamentView",
    "RapportsView",
]
