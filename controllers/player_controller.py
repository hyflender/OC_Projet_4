from models.Player import Player
from views.player_view import PlayerView

from utils.library import log, get_user_input, clear_console


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = Player.load_players()

    def create_player(self):
        # Method to create a new player
        first_name, last_name, birth_date, chess_id = self.view.get_player_details()
        new_player = Player(first_name, last_name, birth_date, chess_id)
        new_player.save_player()
        self.players = Player.load_players()
        log(
            f"Player {new_player.first_name} {new_player.last_name} created successfully."
        )

    def update_player(self):
        # Method to update informations of a player
        self.view.display_all_players(self.players)
        chess_id = get_user_input("Enter the player's chess ID: ")
        self.players = Player.load_players()
        for player in self.players:
            if player.chess_id == chess_id:
                first_name, last_name, birth_date, chess_id = (
                    self.view.get_player_details()
                )
                player.update_player(first_name, last_name, birth_date, chess_id)
                player.save_player()
                log(
                    f"Player {player.first_name} {player.last_name} updated successfully."
                )

    def update_score_player(self):
        # Method to update the score of a player
        self.view.display_all_players(self.players)
        chess_id = self.view.get_user_chess_id()

        self.players = Player.load_players()
        player_found = False
        for player in self.players:
            if player.chess_id == chess_id:
                new_score = self.view.get_new_score()
                player.score = new_score
                player.save_player()
                log(
                    f"Player {player.first_name} {player.last_name} updated successfully."
                )
                player_found = True
                break
        if not player_found:
            log("No player found with the given chess ID.")

    def run(self):
        clear_console()
        while True:
            # Display the player menu
            self.view.display_player_menu()
            # Get the user choice
            choice = get_user_input(
                "Enter the number of the option you want to select: "
            )

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.update_player()
            elif choice == "3":
                self.update_score_player()
            elif choice == "4":
                self.view.display_all_players(self.players)
            elif choice == "5":
                log("Exiting the player management menu.")
                break
            else:
                log("Invalid choice. Please enter a number between 1 and 5.")
