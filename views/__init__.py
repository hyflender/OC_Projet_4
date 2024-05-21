# views/__init__.py

# Import views more easily
from views.main_view import MainView
from views.player_view import PlayerView
from views.matchs_view import MatchsView
from views.tournament_view import TournamentView

__all__ = [
    "MainView",
    "PlayerView",
    "MatchsView",
    "TournamentView",
]
