import time
from utils import (
    get_user_input,
    get_valid_date,
    get_valid_rounds,
    get_user_choice,
    clear_console,
)
from tabulate import tabulate
from models import Tournament, Player
from typing import List

# The menu for managing tournaments - This class is responsible for displaying the menu for managing tournaments.


class TournamentView:
    @staticmethod
    def display_tournament_menu() -> None:
        """
        Displays the menu for managing tournaments.
        """
        print("Menu to manage tournaments")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a new tournament")
        print("2. View and manage a selected tournament")
        print("3. View all tournaments")
        print("4. Go back to main menu")
        print("----------------------------------------")

    def display_tournament_sub_menu(self, tournament: Tournament) -> None:
        """
        Displays the menu for managing tournaments.
        """
        print(f"Menu to manage the {tournament.name}")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Add Players on a tournament")
        print(f"2. Start {tournament.name}")
        print("3. Record Match Result")
        print(f"4. View {tournament.name} details")
        print("5. Go back to main menu")
        print("----------------------------------------")

    @staticmethod
    def view_all_tournaments(tournaments: List[Tournament]) -> None:
        if not tournaments:
            print("No tournaments have been created yet.")
        else:
            tournament_data = [
                {
                    "ID": tournament.id,
                    "Name": tournament.name,
                    "Is Started": "Yes" if tournament.is_started else "No",
                    "Location": tournament.location,
                    "Start_date": tournament.start_date,
                    "End_date": tournament.end_date,
                    "Rounds": tournament.rounds,
                    "Description": tournament.description,
                    "Players": tournament.players_list,
                    "Current_round_number": f"{tournament.current_round_number}/{tournament.rounds}",
                }
                for tournament in tournaments
            ]

            print(tabulate(tournament_data, headers="keys", tablefmt="rounded_outline"))

    @staticmethod
    def get_tournament_details() -> tuple[str, str, str, str, int]:
        """
        Get the tournament details from the user.

        Prompts the user to enter the start date, end date, location,
        description, and number of rounds for the tournament. Ensures
        that the end date is after the start date.

        Returns:
            tuple: A tuple containing the start date, end date, location,
                   description, and number of rounds.
        """
        start_date = get_valid_date("Enter the start date (DD-MM-YYYY): ")
        end_date = get_valid_date("Enter the end date (DD-MM-YYYY): ")
        location = get_user_input("Enter the location of the tournament: ")
        description = get_user_input("Enter the description of the tournament: ")
        rounds = get_valid_rounds(
            "Enter the number of rounds (leave blank for default 4): "
        )

        while end_date <= start_date:
            print(
                "End date must be after the start date. Please enter the dates again."
            )
            start_date = get_valid_date("Enter the start date (DD-MM-YYYY): ")
            end_date = get_valid_date("Enter the end date (DD-MM-YYYY): ")

        return start_date, end_date, location, description, rounds

    @staticmethod
    def generate_unique_tournament_name() -> str:
        """
        Generates a unique tournament name by appending a number to the base name "Tournament_".

        This function loads all existing tournaments and checks their names to ensure the generated
        name is unique. It increments a counter until a unique name is found.

        Returns:
            str: A unique tournament name.
        """
        tournaments = Tournament.load_tournaments()
        base_name = "Tournament_"
        existing_names = {tournament.name for tournament in tournaments}
        count = 1
        while f"{base_name}{count}" in existing_names:
            count += 1
        unique_name = f"{base_name}{count}"
        print(f"Generated Tournament Name: {unique_name}")
        return unique_name

    def get_tournament_id(self) -> int:
        tournaments = Tournament.load_tournaments()
        tournament_ids = [tournament.id for tournament in tournaments]
        while True:
            tournament_id = get_user_input("Enter the ID of the tournament: ")
            try:
                tournament_id = int(tournament_id)
            except ValueError:
                print("Invalid ID. Please enter an integer.")
                continue
            if tournament_id in tournament_ids:
                return tournament_id
            else:
                print("Tournament ID not found. Please try again.")

    def display_informations_message(self, message: str) -> None:
        """
        Display return message to the user.
        """
        if message:
            print("----------------------------------------")
            print(f"{message} | Wait 3 seconds...")
            print("----------------------------------------")
            time.sleep(3)
            clear_console()
            self.message = None

        else:
            pass

    def display_tournament_details(self, tournament: Tournament) -> None:
        """
        Display the details of the tournament.
        """
        tournament_data = [
            {
                "ID": tournament.id,
                "Name": tournament.name,
                "Is Started": "Yes" if tournament.is_started else "No",
                "Is Finished": "Yes" if tournament.is_finished else "No",
                "Location": tournament.location,
                "Start date": tournament.start_date,
                "End date": tournament.end_date,
                "Rounds": tournament.rounds,
                "Description": tournament.description,
                "Current round number": f"{tournament.current_round_number}/{tournament.rounds}",
            }
        ]
        print("----------------------------------------")
        print("Tournament Details:")
        print("----------------------------------------")
        print(tabulate(tournament_data, headers="keys", tablefmt="rounded_outline"))
        print("\n")

        if tournament:
            print("----------------------------------------")
            print("Players:")
            print("----------------------------------------")

            player_data = [
                {
                    "Chess ID": player.chess_id,
                    "First Name": player.first_name,
                    "Last Name": player.last_name,
                    "Score": player.score,
                }
                for player in (
                    Player._load_player_by_chess_id(chess_id)
                    for chess_id in tournament.players_list
                )
            ]
            player_data_sorted = sorted(
                player_data, key=lambda x: x["Score"], reverse=True
            )
            if player_data_sorted:
                print(
                    tabulate(
                        player_data_sorted, headers="keys", tablefmt="rounded_outline"
                    )
                )
            else:
                print("No players found for the given tournament ID.")
                print("---------------------------------------- \n")

        if tournament:
            print("Matches:")
            match_data = []
            previous_round_index = None
            for round_index, round in enumerate(tournament.rounds_list, start=1):
                if (
                    previous_round_index is not None
                    and round_index != previous_round_index
                ):
                    match_data.append(
                        {
                            "Round": "",
                            "Round Name": "",
                            "Match ID": "",
                            "Players": "",
                            "Winner": "",
                        }
                    )
                for match in round.matches:
                    player1 = next(
                        (
                            p
                            for p in Player.load_all_players()
                            if p.chess_id == match.id_player1
                        ),
                        "Unknown",
                    )
                    player2 = next(
                        (
                            p
                            for p in Player.load_all_players()
                            if p.chess_id == match.id_player2
                        ),
                        "Unknown",
                    )
                    if match.winner == "Draw":
                        winner = "Draw"
                    else:
                        winner = next(
                            (
                                p
                                for p in Player.load_all_players()
                                if p.chess_id == match.winner
                            ),
                            "No winner yet",
                        )

                    match_data.append(
                        {
                            "Round": round_index,
                            "Round Name": round.name,
                            "Match ID": match.id,
                            "Players": f"{player1.first_name} {player1.last_name} ({player1.chess_id}) vs "
                            f"{player2.first_name} {player2.last_name} ({player2.chess_id})",
                            "Winner": (
                                f"{winner.first_name} {winner.last_name} ({winner.chess_id})"
                                if hasattr(winner, "first_name")
                                else winner
                            ),
                        }
                    )
                previous_round_index = round_index
            if match_data:
                print(tabulate(match_data, headers="keys", tablefmt="rounded_outline"))
            else:
                print("No matches found for the given tournament ID.")
        else:
            print("No tournament found with the given ID.")

    def view_tournament_players(self, id: int) -> None:
        """
        Views the players of the tournament.
        """
        tournaments = Tournament.load_tournaments()
        tournament = next((p for p in tournaments if p.id == id), None)
        if tournament:
            print("Players:")
            player_data = [
                {
                    "Chess ID": player.chess_id,
                    "First Name": player.first_name,
                    "Last Name": player.last_name,
                    "Score": player.score,
                }
                for player in (
                    Player.load_player_by_id(chess_id)
                    for chess_id in tournament.players_list
                )
            ]
            print(tabulate(player_data, headers="keys", tablefmt="rounded_outline"))
        else:
            print("No tournament found with the given ID.")

    def view_record_match_result(self, tournament_id: int) -> None:
        tournaments = Tournament.load_tournaments()
        tournament = next((p for p in tournaments if p.id == tournament_id), None)

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
                    match.end_match(player1.chess_id, player2.chess_id, equal=True)
                    print("The match is a draw")
                else:
                    print("Invalid winner ID")

                if rounds.end_round():
                    tournament.start_round()

            else:
                print("No match found with that ID.")

        except ValueError:
            print("Invalid match ID or winner ID")
        Tournament.save_tournaments(tournaments)
