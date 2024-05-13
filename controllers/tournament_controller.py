from models.tournament import Tournament
from views.tournament_view import TournamentView

from utils.library import log, get_user_choice, clear_console


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = Tournament.load_tournaments()

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
        tournament = self.tournaments[tournament_id]
        print(tournament.id)
        pass

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
                self.view.view_all_tournaments(self.tournaments)
            elif choice == 6:
                log("Exiting the tournament management menu.")
                break
