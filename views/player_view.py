import re
from tabulate import tabulate

from utils.library import get_user_input, get_valid_date, get_valid_chess_id, log

# The menu for managing players - This class is responsible for displaying the menu for managing players.


class PlayerView:

    @staticmethod
    def display_player_menu():
        """
        Displays the menu for managing players.
        """
        print("Menu to manage players")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a new player")
        print("2. Update a player")
        print("3. Update a player's score")
        print("4. View all players")
        print("5. Go back to main menu")

    @staticmethod
    def get_player_details():
        """Get the player details from the user."""
        first_name = get_user_input("Enter the player's first name: ")
        last_name = get_user_input("Enter the player's last name: ")
        birth_date = get_valid_date("Enter the player's birth date: ")
        chess_id = get_valid_chess_id(
            "Enter the player's chess ID: ", edit=False
        )
        return first_name, last_name, birth_date, chess_id

    @staticmethod
    def get_user_chess_id():
        """Get the user chess id from the user."""
        chess_id = get_user_input("Enter the player's chess ID: ")

        while not re.match(r"^[A-Z]{2}\d{5}$", chess_id):
            chess_id = get_user_input(
                "Invalid format. Please enter a chess ID in the format AB12345: "
            )
        return chess_id

    @staticmethod
    def get_new_score():
        """Get the new score from the user."""
        new_score = int(get_user_input("Enter the new score: "))
        return new_score

    def display_player(player):
        """Display a player."""
        try:
            print(tabulate(player, headers="keys", tablefmt="rounded_outline"))
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def display_all_players(players):
        if not players:
            print("No players have been created yet.")
        else:
            log("List of players:")
            player_data = [
                {
                    "First Name": player.first_name,
                    "Last Name": player.last_name,
                    "Birth Date": player.birth_date,
                    "Chess ID": player.chess_id,
                    "Score": player.score,
                }
                for player in players
            ]
            print(tabulate(player_data, headers="keys", tablefmt="rounded_outline"))
