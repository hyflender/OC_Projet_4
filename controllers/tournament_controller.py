from models.tournament import Tournament
from models.player import Player

from views.tournament_view import TournamentView
from views.player_view import PlayerView

from utils.library import log, get_user_choice, clear_console


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = Tournament.load_tournaments()
        self.player_view = PlayerView()
        self.players = Player.load_players()

    def create_tournament(self):
        # Method to create tournament

        # Generate unique tournament name (Tournament_XX)
        name = self.view.generate_unique_tournament_name()

        # Get tournament details
        start_date, end_date, location, description, rounds = (
            self.view.get_tournament_details()
        )
        new_tournament = Tournament(
            name, location, start_date, end_date, description, rounds
        )
        self.tournaments.append(new_tournament)
        Tournament.save_tournaments(self.tournaments)
        log("Tournament created successfully")

    def add_players_to_tournament(self):
        self.view.view_all_tournaments(self.tournaments)
        tournament_id = self.view.get_tournament_id()
        tournament = next((p for p in self.tournaments if p.id == tournament_id), None)
        print(f"Tournament selected: {tournament.name}")
        self.player_view.display_all_players(self.players)
        chess_ids = input("Enter Chess IDs to add (comma separated): ").split(",")
        chess_ids = [chess_id.strip() for chess_id in chess_ids]
        tournament.add_players_to_tournament(chess_ids)
        Tournament.save_tournaments(self.tournaments)

    def run(self):
        clear_console()
        self.view.view_all_tournaments(self.tournaments)
        while True:
            self.view.display_tournament_menu()
            choice = get_user_choice(7)

            if choice == 1:
                self.create_tournament()
            elif choice == 2:
                self.add_players_to_tournament()
            elif choice == 3:
                tournament_id = self.view.get_tournament_id()
                tournament = next(
                    (p for p in self.tournaments if p.id == tournament_id), None
                )
                tournament.start_tournament()
                Tournament.save_tournaments(self.tournaments)

            
            elif choice == 5:
                self.view.view_all_tournaments(self.tournaments)
            elif choice == 6:
                log("Exiting the tournament management menu.")
                break
