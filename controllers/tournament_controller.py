from models.Tournament import Tournament
from views.tournament_view import TournamentView

from utils.library import log, get_user_choice, clear_console


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = Tournament.load_tournaments()

    def create_tournament(self):
        # Method to create tournament

        name = self.view.generate_unique_tournament_name()
        start_date, end_date, location, description, rounds = (
            self.view.get_tournament_details()
        )
        if not rounds:
            rounds = 4
        new_tournament = Tournament(
            name, location, start_date, end_date, rounds, description
        )
        new_tournament.save_tournament()
        self.tournaments = Tournament.load_tournaments()
        log("Tournament created successfully")

    def run(self):
        clear_console()
        while True:
            self.view.display_tournament_menu()
            choice = get_user_choice(
                "Enter the number of the option you want to select: ",
                ["1", "2", "3", "4"],
            )

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                pass
            elif choice == "3":
                clear_console()
                self.view.view_all_tournaments(self.tournaments)
            elif choice == "4":
                log("Exiting the tournament management menu.")
                break
            else:
                log("Invalid choice. Please enter a number between 1 and 4.")
