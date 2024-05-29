import re
import time
from typing import List, Optional
from tabulate import tabulate
from models import Player

from utils import (
    get_user_input,
    get_valid_date,
    get_valid_chess_id,
    clear_console,
)


class PlayerView:
    """
    The PlayerView class is responsible for displaying the menu for managing players
    and collecting player information from the user.
    """

    @staticmethod
    def display_player_menu() -> None:
        """
        Displays the menu for managing players.
        """
        print("Menu to manage players")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a new player")
        print("2. Manage a player")
        print("3. View all players")
        print("4. Go back to main menu")

    def display_sub_player_menu(self, player: Player) -> None:
        """
        Displays the sub menu for managing a player.
        """
        print("\n Sub menu to manage a player")
        print("----------------------------------------")
        print("Please select an option:")
        print(f"1. Edit {player.first_name} {player.last_name} details")
        print(
            f"2. Edit {player.first_name} {player.last_name} score (actual score: {player.score})"
        )
        print("3. Go back to the main menu")

    @staticmethod
    def get_new_player_informations() -> tuple[str, str, str, str]:
        """
        Prompts the user to enter the details of a player.

        Returns:
            tuple: A tuple containing the first name, last name, birth date, and chess ID of the player.
        """
        first_name = get_user_input(
            "Enter the player's first name: ", allow_empty=False
        )
        last_name = get_user_input("Enter the player's last name: ", allow_empty=False)
        birth_date = get_valid_date(
            "Enter the player's birth date: ", allow_empty=False
        )
        chess_id = get_valid_chess_id(
            "Enter the player's chess ID: ", check_uniqueness=True
        )
        return first_name, last_name, birth_date, chess_id

    @staticmethod
    def get_user_chess_id() -> str:
        """
        Prompts the user to enter a chess ID and validates its format.

        Returns:
            str: The validated chess ID.
        """
        chess_id = get_user_input("Enter the player's chess ID: ")
        while not re.match(r"^[A-Z]{2}\d{5}$", chess_id):
            chess_id = get_user_input(
                "Invalid format. Please enter a chess ID in the format AB12345: "
            )
        return chess_id

    @staticmethod
    def get_new_user_score(prompt: str) -> Optional[int]:
        """
        Prompt the user to enter a score, validate it as an integer, and return it.

        Args:
            prompt (str): The prompt message to display to the user.

        Returns:
            int or None: The score entered by the user as an integer, or None if no input is provided.
        """
        while True:
            score = get_user_input(prompt)
            if score == "":
                return None
            if score.isdigit():
                return int(score)
            print("Invalid score format, please use an integer.")

    @staticmethod
    def display_all_players(players: List[Player]) -> None:
        """
        Display the details of all players.

        Args:
            players (List[Dict]): A list of dictionaries, each containing the details of a player.
        """
        if not players:
            print("No players have been created yet.")
        else:
            print("List of players:")
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

    def display_player_informations(self, player: Player) -> None:
        """
        Display the details of a player.
        """
        player_data = []
        if not player:
            print("No player found.")
        else:
            player_data = [
                {
                    "First Name": player.first_name,
                    "Last Name": player.last_name,
                    "Birth Date": player.birth_date,
                    "Chess ID": player.chess_id,
                    "Score": player.score,
                }
            ]
        return print(tabulate(player_data, headers="keys", tablefmt="rounded_outline"))

    def display_informations_message(self, message: str) -> None:
        """
        Display return message to the user.
        """

        if message:
            print("----------------------------------------")
            print(f"{message} | Wait 3 seconds...")
            print("----------------------------------------")
            time.sleep(3)
            clear_console()
            self.message = None

        else:
            pass
