from models.player import Player


class PlayerController:
    def __init__(self, view, model):
        self.view = view
        self.players = model

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_input(
                "Enter the number of the option you want to select: "
            )

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.update_player_score()
            elif choice == "3":
                self.view_all_players()
            elif choice == "4":
                self.view.display_message("Exiting the player management menu.")
                break
            else:
                self.view.display_message(
                    "Invalid choice. Please enter a number between 1 and 4."
                )

    def create_player(self):
        first_name = self.view.get_user_input("Enter player's first name: ")
        last_name = self.view.get_user_input("Enter player's last name: ")
        birth_date = self.view.get_user_input(
            "Enter player's birth date (YYYY-MM-DD): "
        )
        chess_id = self.view.get_user_input("Enter player's chess ID: ")
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        self.view.display_message(
            f"Player {first_name} {last_name} created successfully!"
        )

    def view_all_players(self):
        if not self.players:
            self.view.display_message("No players have been created yet.")
        else:
            for player in self.players:
                self.view.display_player(player)
