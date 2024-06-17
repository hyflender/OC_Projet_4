from utils import Logger, get_user_choice, clear_console
from controllers import PlayerController, TournamentController, RapportsController
from views import MainView, ShowPlateau


class GlobalController:
    def __init__(self) -> None:
        """
        Initializes the GlobalController class.
        """
        self.view: MainView = MainView()
        self.controllers = {
            1: PlayerController,
            2: TournamentController,
            3: RapportsController,
        }

    def run(self) -> None:
        while True:
            self._clear_and_display()

            choice: int = get_user_choice(4)
            if choice in self.controllers:
                self._run_controller(choice)
            elif choice == 4:
                Logger.info("Exiting the program")
                print("Exiting the program. See you soon !")
                break
            else:
                Logger.critical("Invalid choice")
                print("Invalid choice, please try again.")

    def _clear_and_display(self) -> None:
        Logger.info("Clearing the console")
        clear_console()
        Logger.info("Showing the plateau")
        ShowPlateau().afficher_plateau()
        Logger.info("Showing the global menu")
        self.view.display_global_menu()

    def _run_controller(self, choice: int) -> None:
        Logger.info(
            f"Running the {self.controllers[choice].__name__.lower()} controller"
        )
        controller = self.controllers[choice]()
        controller.run()
