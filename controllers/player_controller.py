from models.Player import Player
from views.player_view import PlayerView

from utils.chest import Library
import json


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = []
        self.load_players()

    def run(self):
        while True:
            self.view.display_player_menu()
            choice = Library.get_user_input(
                "Enter the number of the option you want to select: "
            )

            if choice == "1":
                self.create_player()
            elif choice == "2":
                pass
            elif choice == "3":
                self.view_all_players()
            elif choice == "4":
                Library.display_message("Exiting the player management menu.")
                break
            else:
                Library.display_message(
                    "Invalid choice. Please enter a number between 1 and 4."
                )

    def create_player(self):
        first_name = Library.get_user_input("Enter player's first name: ")
        last_name = Library.get_user_input("Enter player's last name: ")
        birth_date = Library.get_user_input(
            "Enter player's birth date (YYYY-MM-DD): "
        )
        chess_id = Library.get_user_input("Enter player's chess ID: ")
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        Library.display_message(
            f"Player {first_name} {last_name} created successfully!"
        )
        self.save_players()

    def view_all_players(self):
        if not self.players:
            Library.display_message("No players have been created yet.")
        else:
            for player in self.players:
                print(player.__dict__)

    def save_players(self):
        with open("data/players.json", "w") as file:
            json.dump([player.to_dict() for player in self.players], file)

    def load_players(self):
        try:
            with open("players.json", "r") as file:
                players_data = json.load(file)
                self.players = [Player(**data) for data in players_data]
        except FileNotFoundError:
            self.players = []
