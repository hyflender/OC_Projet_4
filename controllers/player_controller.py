from typing import Optional

from models import Player
from views import PlayerView

from utils import (
    get_user_input,
    clear_console,
    get_valid_chess_id,
    get_valid_date,
    get_user_choice,
)


class PlayerController:
    """
    Controller for managing player-related operations.
    """

    def __init__(self) -> None:
        """
        Initializes the PlayerController instance.
        """
        self.view = PlayerView()
        self.players = Player.load_players()

    def create_player(self) -> None:
        """
        Creates a new player and saves it to the list of players.
        """
        first_name, last_name, birth_date, chess_id = self.view.get_player_details()
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        Player.save_players(self.players)
        print(
            f"Player {new_player.first_name} {new_player.last_name} created successfully."
        )

    def update_player(self) -> None:
        """
        Updates the information of an existing player.
        """
        self.view.display_all_players(self.players)
        player = None
        while not player:
            chess_id = get_valid_chess_id(
                "Chess ID of the player to update: ", edit=True
            )
            player = self._find_player_by_chess_id(chess_id)
            if not player:
                print("Player not found with the given chess ID. Please try again.")
        if player:
            print(
                f"Player {player.first_name} {player.last_name} ({player.chess_id}) selected."
            )
            self._update_player_details(player)
        else:
            print("Player not found with the given chess ID.")

    def update_score_player(self) -> None:
        """
        Updates the score of an existing player.
        """

        self.view.display_all_players(self.players)
        player = None
        while not player:
            chess_id = get_valid_chess_id(
                "Chess ID of the player's score to update: ", edit=True
            )
            player = self._find_player_by_chess_id(chess_id)
            if not player:
                print("Player not found with the given chess ID. Please try again.")
        if player:
            print(
                f"Player {player.first_name} {player.last_name} ({player.chess_id}) selected."
            )
            self._update_player_score(player)
        else:
            print("Player not found with the given chess ID.")

    def _find_player_by_chess_id(self, chess_id: str) -> Optional[Player]:
        """
        Finds a player by its chess ID.

        Args:
            chess_id (str): The chess ID of the player to find.

        Returns:
            Optional[Player]: The player with the given chess ID, or None if not found.
        """
        return next((p for p in self.players if p.chess_id == chess_id), None)

    def _update_player_details(self, player: Player) -> None:
        """
        Updates the details of a player.

        Args:
            player (Player): The player to update.
        """
        first_name = get_user_input("New First Name (leave blank to keep current): ")
        last_name = get_user_input("New Last Name (leave blank to keep current): ")
        birth_date = get_valid_date(
            "New Birth Date (leave blank to keep current): ", edit=True
        )

        player.update_player(first_name, last_name, birth_date)
        Player.save_players(self.players)
        print("Player updated successfully.")

    def _update_player_score(self, player: Player) -> None:
        """
        Updates the score of a player.

        Args:
            player (Player): The player to update.
        """
        new_score = self.view.get_new_user_score(
            "New Score (leave blank to keep current): "
        )
        player.update_score(new_score)
        Player.save_players(self.players)
        print("Player's score updated successfully.")

    def run(self) -> None:
        """
        Run the players management menu.
        """
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
                print("Exiting the player management menu.")
                break
