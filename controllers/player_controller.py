from models import Player
from views import PlayerView
from utils import (
    Logger,
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
        self.players = Player.load_all_players()
        self.message = None

    def create_player(self) -> None:
        """
        Creates a new player and saves it to the list of players.
        """
        try:
            first_name, last_name, birth_date, chess_id = (
                self.view.get_new_player_informations()
            )
            new_player = Player(first_name, last_name, birth_date, chess_id)
            self.players.append(new_player)
            Player.save_all_players(self.players)
            success_message = f"Player {new_player.first_name} {new_player.last_name} created successfully."
            Logger.info(success_message)
            self.message = success_message
        except ValueError as ve:
            error_message = f"Validation error: {ve}"
            Logger.critical(error_message)
            self.message = error_message
        except Exception as e:
            error_message = f"Error creating player: {e}"
            Logger.critical(error_message)
            self.message = error_message

    def update_player_details(self, player: Player) -> None:
        """
        Updates the details of a player.

        Args:
            player (Player): The player to update.
        """
        if not player:
            self.message = "Player not found with the given chess ID."
            Logger.warn(self.message)
            return

        try:
            first_name = get_user_input(
                "New First Name (leave blank to keep current): "
            )
            last_name = get_user_input("New Last Name (leave blank to keep current): ")
            birth_date = get_valid_date(
                "New Birth Date (leave blank to keep current): ", allow_empty=True
            )

            player.update_player(first_name, last_name, birth_date)
            self.message = (
                f"Player {player.first_name} {player.last_name} updated successfully."
            )
            Logger.info(self.message)
        except ValueError as ve:
            self.message = f"Validation error: {ve}"
            Logger.critical(self.message)
        except Exception as e:
            self.message = f"Error updating player: {e}"
            Logger.critical(self.message)

    def update_player_score(self, player: Player) -> None:
        """
        Update the score of an existing player.

        This method prompts the user to enter a new score for the specified player.
        If a new score is provided, it updates the player's score and logs the update.
        If no player is found with the given chess ID, it logs a warning message.

        Args:
            player (Player): The player whose score is to be updated.
        """
        if not player:
            self.message = "Player not found with the given chess ID."
            Logger.warn(self.message)
            return

        try:
            new_score = self.view.get_new_user_score(
                "New Score (leave blank to keep current): "
            )
            if new_score is not None:
                player.update_score(new_score)
                self.message = (
                    f"Player {player.first_name} {player.last_name} "
                    f"({player.chess_id}) score updated to {player.score}."
                )
                Logger.info(self.message)
            else:
                self.message = "Player's score remains unchanged."
                Logger.info(self.message)
        except ValueError as ve:
            self.message = f"Validation error: {ve}"
            Logger.critical(self.message)
        except Exception as e:
            self.message = f"Error updating player's score: {e}"
            Logger.critical(self.message)

    def run(self) -> None:
        """
        Run the players management menu.
        """
        clear_console()
        self.view.display_informations_message(self.message)
        while True:
            try:
                Logger.info("Displaying list of players")
                self.view.display_all_players(self.players)
                Logger.info("Displaying the player menu")
                self.view.display_player_menu()
                Logger.info("Getting the user choice")
                choice = get_user_choice(5)

                if choice == 1:
                    Logger.info("User choice 1: Creating a new player")
                    self.create_player()
                elif choice == 2:
                    Logger.info("User choice 2: Managing a player")
                    self.manage_submenu()
                elif choice == 3:
                    Logger.info("User choice 3: Displaying all players")
                    self.view.display_all_players(self.players)
                elif choice == 4:
                    Logger.info("User choice 4: Exiting the player management menu.")
                    break
                else:
                    Logger.warn("Invalid choice selected")
                    self.view.display_informations_message(
                        "Invalid choice, please try again."
                    )
            except Exception as e:
                Logger.critical(f"An error occurred in the player management menu: {e}")
                self.view.display_informations_message(
                    "An unexpected error occurred. Please try again."
                )

    def manage_submenu(self) -> None:
        """
        Select and manage a player.
        """
        clear_console()
        self.view.display_all_players(self.players)
        chess_id = get_valid_chess_id(
            "Please enter the Chess ID of the player you wish to manage: ",
            check_uniqueness=False,
        )
        selected_player = Player._load_player_by_chess_id(chess_id)

        if not selected_player:
            self.message = "No player found with the provided Chess ID."
            Logger.warn(self.message)
            self.view.display_informations_message(self.message)
            return

        while True:
            clear_console()
            self.view.display_informations_message(self.message)
            self.view.display_player_informations(selected_player)
            self.view.display_sub_player_menu(selected_player)

            choice = get_user_choice(3)
            if choice == 1:
                Logger.info(f"Editing details for player {selected_player.chess_id}")
                self.update_player_details(selected_player)
            elif choice == 2:
                Logger.info(f"Editing score for player {selected_player.chess_id}")
                self.update_player_score(selected_player)
            elif choice == 3:
                Logger.info(f"Exiting management for player {selected_player.chess_id}")
                break
            else:
                Logger.warn(f"Invalid choice {choice} in player management submenu")
                self.view.display_informations_message(
                    "Invalid choice, please try again."
                )
