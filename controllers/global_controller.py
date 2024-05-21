from utils import Logger, get_user_choice, clear_console

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from views.main_view import MainView, ShowPlateau


class GlobalController:
    def __init__(self):
        """
        Initializes the GlobalController class, clear the console, setting up the main view and the plateau.
        """
        clear_console()
        self.view = MainView()
        self.show_plateau = ShowPlateau().afficher_plateau()

    def run(self):
        while True:
            # Display the global menu
            self.view.display_global_menu()
            # Get the user choice
            choice = get_user_choice(4)

            if choice == 1:
                Logger.info("Running the player controller")
                player_controller = PlayerController()
                player_controller.run()

            elif choice == 2:
                Logger.info("Running the tournament controller")
                tournament_controller = TournamentController()
                tournament_controller.run()

            elif choice == 4:
                print("Exiting the program. See you soon !")
                break
            else:
                break
