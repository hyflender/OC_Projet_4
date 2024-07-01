from views import RapportsView
from utils import clear_console, get_user_choice, display_message


class RapportsController:
    def __init__(self):
        clear_console()
        self.view = RapportsView()

    def run(self):
        while True:
            self.view.display_rapports_menu()
            choice = get_user_choice(5)

            if choice == 1:
                # List of all players in alphabetical order
                self.view.generate_players_report()
            elif choice == 2:
                # List of all tournaments details
                self.view.generate_tournaments_report()
            elif choice == 3:
                # List of tournament players in alphabetical order
                self.view.generate_list_players_on_tournament()
            elif choice == 4:
                # Rapport flake8-html dans un répertoire "flake8_rapport"
                self.view.generate_flake8_report()
            elif choice == 5:
                display_message("Exiting the rapports menu.")
                clear_console()
                break
