from utils.chest import Library

from views.main_view import MainView

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from GUI.chest_gui import start_chest_gui


class GlobalController:
    def __init__(self):
        self.view = MainView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def run(self):
        while True:
            self.view.display_global_menu()
            choice = Library.get_user_input(
                "Enter the number of the option you want to select: "
            )

            if choice == "1":
                self.player_controller.run()
            elif choice == "2":
                self.tournament_controller.run()
            elif choice == "6":
                start_chest_gui()
                break
            elif choice == "7":
                Library.display_message("Exiting the player management menu.")
                break
            else:
                Library.display_message(
                    "Invalid choice. Please enter a number between 1 and 4."
                )
