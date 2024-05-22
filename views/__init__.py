# views/__init__.py

# Import views more easily
from views.main_view import MainView, ShowPlateau
from views.player_view import PlayerView
from views.matchs_view import MatchsView
from views.tournament_view import TournamentView
from views.rapports_view import RapportsView

__all__ = [
    "MainView",
    "ShowPlateau",
    "PlayerView",
    "MatchsView",
    "TournamentView",
    "RapportsView",
]
