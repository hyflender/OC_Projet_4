from utils.library import log, get_user_choice, clear_console

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from views.main_view import MainView, ShowPlateau


class GlobalController:
    def __init__(self):
        """
        Initializes the GlobalController class, setting up the main view.
        """
        self.view = MainView()

    def run(self):
        while True:
            # Clear the console
            clear_console()
            # Show the Chess Plateau
            ShowPlateau().afficher_plateau()
            # Display the global menu
            self.view.display_global_menu()
            # Get the user choice
            choice = get_user_choice(7)

            if choice == 1:
                self.player_controller = PlayerController()
                self.player_controller.run()
            elif choice == 2:
                self.tournament_controller = TournamentController()
                self.tournament_controller.run()

            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                break
            elif choice == 7:
                log("Exiting the program. See you soon !")
                break
            else:
                log("Invalid choice. Please enter a number between 1 and 7.")
