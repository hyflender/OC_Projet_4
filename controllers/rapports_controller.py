from views import RapportsView

from utils import clear_console, get_user_choice


class RapportsController:
    def __init__(self):
        clear_console()
        self.view = RapportsView()

    def run(self):
        while True:
            self.view.display_rapports_menu()
            choice = get_user_choice(7)

            if choice == 1:
                # List of all players in alphabetical order
                self.view.generate_players_report()
            elif choice == 2:
                # List of all tournaments
                self.view.generate_tournaments_report()
            elif choice == 3:
                # nom et dates d'un tournoi donné
                pass
            elif choice == 4:
                # List of tournament players in alphabetical order
                self.view.generate_list_players_on_tournament()
            elif choice == 5:
                # List of all the matches of a tournament
                self.view.generate_tournaments_report()
            elif choice == 6:
                # Rapport flake8-html dans un répertoire "flake8_rapport"
                self.view.generate_flake8_report()
            elif choice == 7:
                print("Exiting the rapports menu.")
                clear_console()
                break
