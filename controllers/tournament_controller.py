from models import Tournament, Player
from views import TournamentView, PlayerView

from utils import Logger, get_user_choice, clear_console, get_user_input


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = self._load_tournaments()
        self.player_view = PlayerView()
        self.players = self._load_players()
        self.message = ""

    def _load_tournaments(self):
        return Tournament.load_tournaments()

    def _load_players(self):
        return Player.load_all_players()

    def create_tournament(self):
        name = self._generate_unique_tournament_name()
        tournament_details = self._get_tournament_details()
        new_tournament = self._create_new_tournament(name, tournament_details)
        self._save_tournament(new_tournament)
        print(f"Tournament {new_tournament.name} created successfully")
        Logger.info(f"Tournament {new_tournament.name} created successfully")

    def _generate_unique_tournament_name(self):
        return self.view.generate_unique_tournament_name()

    def _get_tournament_details(self):
        return self.view.get_tournament_details()

    def _create_new_tournament(self, name, details):
        start_date, end_date, location, description, rounds = details
        return Tournament(name, location, start_date, end_date, description, rounds)

    def _save_tournament(self, tournament):
        self.tournaments.append(tournament)
        Tournament.save_tournaments(self.tournaments)

    def add_players_to_tournament(self, tournament):
        self.player_view.display_all_players(self.players)
        chess_ids = get_user_input("Enter Chess IDs to add (comma separated): ").split(
            ","
        )
        chess_ids = [chess_id.strip() for chess_id in chess_ids if chess_id.strip()]

        if not chess_ids:
            self.message = "No valid Chess IDs entered."
            Logger.warn(self.message)
            self.view.display_informations_message(self.message)
            return

        success = tournament.add_players_to_tournament(chess_ids)

        if success:
            self.message = (
                f"Players added to tournament {tournament.name} successfully."
            )
            Logger.info(self.message)
            self._save_tournament(tournament)
        else:
            self.message = (
                f"Failed to add some players to tournament {tournament.name}."
            )
            Logger.critical(self.message)

        self.view.display_informations_message(self.message)
        

    def start_tournament(self, tournament):
        tournament.start_tournament()
        Tournament._save_tournament(tournament)

    def run(self):
        while True:
            clear_console()
            self.view.view_all_tournaments(self.tournaments)
            self.view.display_tournament_menu()
            choice = get_user_choice(4)

            if choice == 1:
                self.create_tournament()
            elif choice == 2:
                self.manage_tournament()
            elif choice == 3:
                clear_console()
                self.view.view_all_tournaments(self.tournaments)
            elif choice == 4:
                print("Exiting the tournament management menu.")
                break

    def manage_tournament(self):
        """
        Select and manage a player.
        """
        clear_console()
        self.view.view_all_tournaments(self.tournaments)
        tournament_id = get_user_input(
            "Enter the ID of the tournament you want to manage: "
        )
        tournament = Tournament._load_tournament_by_id(int(tournament_id))

        if not tournament:
            self.message = "No tournament found with the provided ID."
            Logger.warn(self.message)
            self.view.display_informations_message(self.message)
            return

        while True:
            clear_console()
            self.view.display_informations_message(self.message)
            self.view.display_tournament_details(tournament)
            self.view.display_tournament_sub_menu(tournament)

            choice = get_user_choice(5)
            if choice == 1:
                Logger.info(f"Add players to tournament {tournament.name}")
                self.add_players_to_tournament(tournament)
            elif choice == 2:
                self.start_tournament(tournament)
