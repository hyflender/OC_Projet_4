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
                # Liste de tous les joueurs par ordre alphabétique
                self.view.generate_players_report()
            elif choice == 2:
                # Liste de tous les tournois
                pass
            elif choice == 3:
                # nom et dates d'un tournoi donné
                pass
            elif choice == 4:
                # Liste des joueurs du tournoi par ordre alphabétique
                pass
            elif choice == 5:
                # Liste de tous les tours du tournoi et de tous les matchs du tour
                pass
            elif choice == 6:
                # Rapport flake8-html dans un répertoire "flake8_rapport"
                pass
            elif choice == 7:
                print("Exiting the rapports menu.")
                break
