from models.tournament import Tournament
from models.player import Player

from views.tournament_view import TournamentView
from views.player_view import PlayerView

from utils.library import log, get_user_choice, clear_console, get_user_input


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = Tournament.load_tournaments()
        self.player_view = PlayerView()
        self.players = Player.load_players()

    def create_tournament(self):
        # Method to create tournament

        # Generate unique tournament name (Tournament_XX)
        name = self.view.generate_unique_tournament_name()

        # Get tournament details
        start_date, end_date, location, description, rounds = (
            self.view.get_tournament_details()
        )
        new_tournament = Tournament(
            name, location, start_date, end_date, description, rounds
        )
        self.tournaments.append(new_tournament)
        Tournament.save_tournaments(self.tournaments)
        log("Tournament created successfully")

    def add_players_to_tournament(self):
        self.view.view_all_tournaments(self.tournaments)
        tournament_id = self.view.get_tournament_id()
        tournament = next((p for p in self.tournaments if p.id == tournament_id), None)
        print(f"Tournament selected: {tournament.name}")
        self.player_view.display_all_players(self.players)
        chess_ids = input("Enter Chess IDs to add (comma separated): ").split(",")
        chess_ids = [chess_id.strip() for chess_id in chess_ids]
        tournament.add_players_to_tournament(chess_ids)
        Tournament.save_tournaments(self.tournaments)

    def run(self):
        clear_console()
        self.view.view_all_tournaments(self.tournaments)
        while True:
            self.view.display_tournament_menu()
            choice = get_user_choice(7)

            if choice == 1:
                self.create_tournament()
            elif choice == 2:
                self.add_players_to_tournament()
            elif choice == 3:
                tournament_id = self.view.get_tournament_id()
                tournament = next(
                    (p for p in self.tournaments if p.id == tournament_id), None
                )
                tournament.start_tournament()
                Tournament.save_tournaments(self.tournaments)

            elif choice == 4:
                self.view.view_all_tournaments(self.tournaments)
                tournament_id = self.view.get_tournament_id()
                tournament = next(
                    (p for p in self.tournaments if p.id == tournament_id), None
                )

                print(f"Current Round: {tournament.current_round_number}")
                for rounds in tournament.rounds_list:
                    for m in rounds.matches:
                        player1 = Player.load_player_by_id(m.id_player1)
                        player2 = Player.load_player_by_id(m.id_player2)
                        print(
                            f"Match ID: {m.id}, {player1.first_name} {player1.last_name} "
                            f"({player1.chess_id}) vs {player2.first_name} {player2.last_name} "
                            f"({player2.chess_id}), Winner: {m.winner}"
                        )
                try:
                    match_id = int(get_user_input("Enter the match ID: "))
                    match = None
                    for rounds in tournament.rounds_list:
                        for m in rounds.matches:
                            if m.id == match_id:
                                match = m
                                break
                    if match:
                        player1 = Player.load_player_by_id(match.id_player1)
                        player2 = Player.load_player_by_id(match.id_player2)

                        print("Who won the match? : ")
                        print(
                            f"1 - {player1.first_name} {player1.last_name} ({player1.chess_id})"
                        )
                        print(
                            f"2 - {player2.first_name} {player2.last_name} ({player2.chess_id})"
                        )
                        print("3 - Match end in a draw")
                        winner = get_user_choice(3)
                        if winner == 1:
                            match.end_match(player1.chess_id, player2.chess_id)
                            print(
                                f"{player1.first_name} {player1.last_name} ({player1.chess_id}) won the match"
                            )
                        elif winner == 2:
                            match.end_match(player2.chess_id, player1.chess_id)
                            print(
                                f"{player2.first_name} {player2.last_name} ({player2.chess_id}) won the match"
                            )
                        elif winner == 3:
                            match.end_match(
                                player1.chess_id, player2.chess_id, equal=True
                            )
                            print("The match is a draw")
                        else:
                            print("Invalid winner ID")
                            continue
                        if rounds.end_round():
                            tournament.start_round()
                            

                    else:
                        print("No match found with that ID.")

                except ValueError:
                    log("Invalid match ID or winner ID")

                Tournament.save_tournaments(self.tournaments)

            elif choice == 5:
                self.view.view_all_tournaments(self.tournaments)
            elif choice == 7:
                log("Exiting the tournament management menu.")
                break
