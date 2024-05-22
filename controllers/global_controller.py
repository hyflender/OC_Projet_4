from utils import Logger, get_user_choice, clear_console

from controllers import PlayerController, RapportsController

from views import MainView, ShowPlateau


class GlobalController:
    def __init__(self) -> None:
        """
        Initializes the GlobalController class, clear the console, setting up the main view and the plateau.
        """
        self.view: MainView = MainView()

    def run(self) -> None:
        while True:
            Logger.info("Clearing the console")
            clear_console()

            Logger.info("Showing the plateau")
            self.show_plateau: ShowPlateau = ShowPlateau().afficher_plateau()

            Logger.info("Showing the global menu")
            self.view.display_global_menu()

            Logger.info("Getting the user choice")
            choice: int = get_user_choice(4)

            if choice == 1:
                Logger.info("Running the player controller")
                player_controller: PlayerController = PlayerController()
                player_controller.run()

            elif choice == 2:
                # Logger.info("Running the tournament controller")
                # tournament_controller: TournamentController = TournamentController()
                # tournament_controller.run()
                pass

            elif choice == 3:
                Logger.info("Running the rapports controller")
                rapports_controller: RapportsController = RapportsController()
                rapports_controller.run()

            elif choice == 4:
                Logger.info("Exiting the program")
                print("Exiting the program. See you soon !")
                break
            else:
                Logger.critical("Invalid choice")
                print("Invalid choice, please try again.")
