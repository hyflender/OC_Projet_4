from utils.library import log, get_user_input, get_valid_date
from tabulate import tabulate
from models.Tournament import Tournament

# The menu for managing tournaments - This class is responsible for displaying the menu for managing tournaments.


class TournamentView:
    @staticmethod
    def display_tournament_menu():
        """
        Displays the menu for managing tournaments.
        """
        print("Menu to manage tournaments")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a new tournament")
        print("2. Start a tournament")
        print("3. View all tournaments")
        print("4. View tournament details")
        print("5. Record Match Result")
        print("6. Go back to main menu")
        print("----------------------------------------")

    @staticmethod
    def view_all_tournaments(tournaments):
        if not tournaments:
            log("No tournaments have been created yet.")
        else:
            tournament_data = [tournament.__dict__ for tournament in tournaments]
            print(tabulate(tournament_data, headers="keys", tablefmt="rounded_outline"))

    @staticmethod
    def get_tournament_details():
        """Get the tournament details from the user."""
        start_date = get_valid_date("Enter the start date (DD-MM-YYYY): ")
        end_date = get_valid_date("Enter the end date (DD-MM-YYYY): ")
        location = get_user_input("Enter the location of the tournament: ")
        description = get_user_input("Enter the description of the tournament: ")
        rounds = get_user_input("Enter the number of rounds: ")
        return start_date, end_date, location, description, rounds

    @staticmethod
    def generate_unique_tournament_name():
        tournaments = Tournament.load_tournaments()
        base_name = "Tournament_"
        existing_names = {tournament.name for tournament in tournaments}
        count = 1
        while f"{base_name}{count}" in existing_names:
            count += 1
        unique_name = f"{base_name}{count}"
        log(f"Generated Tournament Name: {unique_name}")
        return unique_name
