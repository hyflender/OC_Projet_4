from models.Player import Player
from views.player_view import PlayerView

from utils.chest import Library
from utils.data_manager import PlayersData


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.data = PlayersData()
        self.players = []
        self.players = self.data.load_players()

    def run(self):
        while True:
            self.view.display_player_menu()
            choice = Library.get_user_input(
                "Enter the number of the option you want to select: "
            )

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.update_player()
            elif choice == "3":
                self.update_score()
            elif choice == "4":
                self.view_all_players()
            elif choice == "5":
                Library.display_message("Exiting the player management menu.")
                break
            else:
                Library.display_message(
                    "Invalid choice. Please enter a number between 1 and 5."
                )

    def create_player(self):
        first_name = Library.get_user_input("Enter player's first name: ")
        last_name = Library.get_user_input("Enter player's last name: ")
        birth_date = Library.get_user_input("Enter player's birth date (YYYY-MM-DD): ")
        chess_id = Library.get_user_input("Enter player's chess ID: ")
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        Library.display_message(
            f"Player {first_name} {last_name} created successfully!"
        )
        self.data.save_players(self.players)

    def update_player(self):
        chess_id = Library.get_user_input(
            "Enter the chess ID of the player you want to update: "
        )
        player = next(
            (player for player in self.players if player.chess_id == chess_id), None
        )
        if player:
            player.first_name = Library.get_user_input("Enter the new first name: ")
            player.last_name = Library.get_user_input("Enter the new last name: ")
            player.birth_date = Library.get_user_input(
                "Enter the new birth date (YYYY-MM-DD): "
            )
            self.data.save_players(self.players)
            Library.display_message("Player updated successfully!")
        else:
            Library.display_message("Player not found.")

    def update_score(self):
        chess_id = Library.get_user_input(
            "Enter the chess ID of the player you want to update: "
        )
        player = next(
            (player for player in self.players if player.chess_id == chess_id), None
        )
        if player:
            player.score = Library.get_user_input("Enter the new score: ")
            self.data.save_players(self.players)
            Library.display_message("Score updated successfully!")
        else:
            Library.display_message("Player not found.")

    def view_all_players(self):
        if not self.players:
            Library.display_message("No players have been created yet.")
        else:
            for player in self.players:
                print(player.__dict__)
