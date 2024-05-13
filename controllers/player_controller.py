from models.player import Player
from views.player_view import PlayerView

from utils.library import (
    log,
    get_user_input,
    clear_console,
    get_valid_chess_id,
    get_valid_date,
    get_user_score,
    get_user_choice,
)


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = Player.load_players()

    def create_player(self):
        # Method to create a new player
        first_name, last_name, birth_date, chess_id = self.view.get_player_details()
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        Player.save_players(self.players)
        log(
            f"Player {new_player.first_name} {new_player.last_name} created successfully."
        )

    def update_player(self):
        # Method to update informations of a player
        self.view.display_all_players(self.players)
        chess_id = get_valid_chess_id("Chess ID of the player to update: ", edit=True)
        player = next((p for p in self.players if p.chess_id == chess_id), None)
        if player:
            log(
                f"Player {player.first_name} {player.last_name} ({player.chess_id}) selected."
            )
            first_name = get_user_input(
                "New First Name (leave blank to keep current): "
            )
            last_name = get_user_input("New Last Name (leave blank to keep current): ")
            birth_date = get_valid_date(
                "New Birth Date (leave blank to keep current): ", edit=True
            )
            player.update_player(first_name, last_name, birth_date)
            Player.save_players(self.players)
            log("Player updated successfully.")
        else:
            log("Player not found with the given chess ID.")

    def update_score_player(self):
        # Method to update the score of a player

        self.view.display_all_players(self.players)
        chess_id = get_valid_chess_id(
            "Chess ID of the player's score to update: ", edit=True
        )
        player = next((p for p in self.players if p.chess_id == chess_id), None)
        if player:
            log(
                f"Player {player.first_name} {player.last_name} ({player.chess_id}) selected."
            )
            new_score = get_user_score("New Score (leave blank to keep current): ")
            player.update_score(new_score)
            Player.save_players(self.players)
            log("Player's score updated successfully.")
        else:
            log("Player not found with the given chess ID.")

    def run(self):
        clear_console()
        while True:
            # Display list of players
            self.view.display_all_players(self.players)
            # Display the player menu
            self.view.display_player_menu()
            # Get the user choice
            choice = get_user_choice(5)

            if choice == 1:
                self.create_player()
            elif choice == 2:
                self.update_player()
            elif choice == 3:
                self.update_score_player()
            elif choice == 4:
                self.view.display_all_players(self.players)
            elif choice == 5:
                log("Exiting the player management menu.")
                break
