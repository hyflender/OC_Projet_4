# views/__init__.py

# Import views more easily
from views.main_view import MainView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.rapports_view import RapportsView

__all__ = [
    "MainView",
    "PlayerView",
    "TournamentView",
    "RapportsView",
]
