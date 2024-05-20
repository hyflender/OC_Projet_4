from utils import log, get_user_input, get_valid_date, get_valid_rounds
from tabulate import tabulate
from models.tournament import Tournament

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
        print("2. Add Players on a tournament")
        print("3. Start a tournament")
        print("4. Record Match Result")
        print("5. View all tournaments")
        print("6. View tournament details")
        print("7. Go back to main menu")
        print("----------------------------------------")

    @staticmethod
    def view_all_tournaments(tournaments):
        if not tournaments:
            log("No tournaments have been created yet.")
        else:

            tournament_data = [{
                'ID': tournament.id,
                'Name': tournament.name,
                'Is Started': "Yes" if tournament.tournament_started else "No",
                'Location': tournament.location,
                'Start_date': tournament.start_date,
                'End_date': tournament.end_date,
                'Rounds': tournament.rounds,
                'Description': tournament.description,
                'Players': tournament.players_list,
                'Current_round_number': f"{tournament.current_round_number}/{tournament.rounds}"
            } for tournament in tournaments]

            print(tabulate(tournament_data, headers="keys", tablefmt="rounded_outline"))

    @staticmethod
    def get_tournament_details():
        """Get the tournament details from the user."""
        start_date = get_valid_date("Enter the start date (DD-MM-YYYY): ")
        end_date = get_valid_date("Enter the end date (DD-MM-YYYY): ")
        location = get_user_input("Enter the location of the tournament: ")
        description = get_user_input("Enter the description of the tournament: ")
        rounds = get_valid_rounds("Enter the number of rounds (blank for default 4): ")
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

    def get_tournament_id(self):
        tournaments = Tournament.load_tournaments()
        tournament_ids = [tournament.id for tournament in tournaments]
        while True:
            tournament_id = get_user_input("Enter the ID of the tournament: ")
            try:
                tournament_id = int(tournament_id)
            except ValueError:
                print("Invalid ID. Please enter an integer.")
                continue
            if tournament_id in tournament_ids:
                return tournament_id
            else:
                print("Tournament ID not found. Please try again.")

