from tabulate import tabulate
from models.Tournament import Tournament
from views.tournament_view import TournamentView

from utils.data_manager import TournamentsData

from utils.chest import Library


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.data = TournamentsData()
        self.tournaments = []
        self.tournaments = self.data.load_tournaments()

    def run(self):

        while True:
            self.view.display_tournament_menu()
            choice = Library.get_user_input(
                "Enter the number of the option you want to select: "
            )

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.submenu()
            elif choice == "3":
                self.view_all_tournaments()
            elif choice == "4":
                self.view.display_message("Exiting the tournament management menu.")
                break
            else:
                self.view.display_message(
                    "Invalid choice. Please enter a number between 1 and 4."
                )

    def submenu(self):
        while True:
            self.view.display_tournament_submenu()
            choice = Library.get_user_input(
                "Enter the number of the option you want to select: "
            )
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                self.view.display_message("Exiting the tournament management menu.")
                break
            else:
                self.view.display_message(
                    "Invalid choice. Please enter a number between 1 and 4."
                )

    def create_tournament(self):
        Library.display_message("Creating a new tournament")
        name = Library.get_user_input("Enter the name of the tournament: ")
        start_date = Library.get_user_input("Enter the start date of the tournament: ")
        end_date = Library.get_user_input("Enter the end date of the tournament: ")
        location = Library.get_user_input("Enter the location of the tournament: ")
        new_tournament = Tournament(name, location, start_date, end_date)
        self.tournaments.append(new_tournament)
        self.data.save_tournaments(self.tournaments)
        Library.display_message("Tournament created successfully")

    def view_all_tournaments(self):
        if not self.tournaments:
            Library.display_message("No tournaments have been created yet.")
        else:
            tournament_data = [tournament.__dict__ for tournament in self.tournaments]
            print(tabulate(tournament_data, headers="keys", tablefmt="rounded_outline"))
