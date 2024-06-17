import time
from views import RapportsView
from utils import clear_console, get_user_choice


class RapportsController:
    def __init__(self) -> None:
        """
        Initializes the RapportsController instance.
        Clears the console and sets up the view.
        """
        clear_console()
        self.view = RapportsView()

    def run(self) -> None:
        """
        Runs the rapports menu, displaying options and executing the selected action.
        """
        menu_actions = {
            1: self.view.generate_players_report,
            2: self.view.generate_tournaments_report,
            3: self.no_action,
            4: self.view.generate_list_players_on_tournament,
            5: self.view.generate_tournaments_report,
            6: self.exit_menu,
        }

        while True:
            self.view.display_rapports_menu()
            choice = get_user_choice(6)
            action = menu_actions.get(choice, self.invalid_choice)
            action(choice)

    def no_action(self, choice: int) -> None:
        pass

    def exit_menu(self, choice: int) -> None:
        """
        Exits the rapports menu and clears the console.

        Args:
            choice (int): The menu choice.
        """
        print("Exiting the rapports menu...")
        time.sleep(3)
        clear_console()

    def invalid_choice(self, choice: int) -> None:
        """
        Handles invalid menu choices.

        Args:
            choice (int): The invalid menu choice.
        """
        print(f"Invalid choice {choice}, please try again.")
