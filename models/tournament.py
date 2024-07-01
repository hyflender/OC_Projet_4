import json
import random
from typing import List, Dict, Any

from models import Player, Round, Match
from config import TOURNAMENTS_FILE


class Tournament:
    """
    Represents a chess tournament.
    """

    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        description: str,
        rounds: int = 4,
    ) -> None:
        self.id = Tournament.get_next_id()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.description = description
        self.players_list: List[str] = []
        self.rounds_list: List[Round] = []
        self.current_round_number: int = len(self.rounds_list)
        self.is_started: bool = False
        self.is_finished: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the tournament instance to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary containing the tournament's attributes.
        """
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": self.rounds,
            "current_round_number": self.current_round_number,
            "players_list": self.players_list,
            "rounds_list": [round.to_dict() for round in self.rounds_list],
            "description": self.description,
            "is_started": self.is_started,
            "is_finished": self.is_finished,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Tournament":
        """
        Deserializes a dictionary to a Tournament instance.

        Args:
            data (Dict[str, Any]): A dictionary containing the tournament's attributes.

        Returns:
            Tournament: A Tournament instance with the attributes from the dictionary.
        """
        tournament = Tournament(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data["description"],
            data["rounds"],
        )
        tournament.id = data.get("id", 0)
        tournament.current_round_number = data.get("current_round_number", 0)
        tournament.players_list = data.get("players_list", [])
        tournament.rounds_list = [
            Round.from_dict(round_data) for round_data in data["rounds_list"]
        ]
        tournament.is_started = data.get("is_started", False)
        tournament.is_finished = data.get("is_finished", False)
        return tournament

    @staticmethod
    def save_tournaments(tournaments: List["Tournament"]) -> None:
        """
        Saves a list of tournaments to a JSON file.

        Args:
            tournaments (List[Tournament]): A list of Tournament instances.
        """
        try:
            with TOURNAMENTS_FILE.open("w", encoding="utf-8") as file:
                json.dump(
                    [tournament.to_dict() for tournament in tournaments],
                    file,
                    indent=4,
                    sort_keys=True,
                )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def load_tournaments() -> List["Tournament"]:
        """
        Loads a list of tournaments from a JSON file.

        Returns:
            List[Tournament]: A list of Tournament instances.
        """
        try:
            with TOURNAMENTS_FILE.open("r", encoding="utf-8") as file:
                tournaments_data = json.load(file)
                return [
                    Tournament.from_dict(tournament) for tournament in tournaments_data
                ]
        except FileNotFoundError:
            return []

    @staticmethod
    def get_next_id() -> int:
        """
        Generates the next ID for a tournament.

        Returns:
            int: The next ID for a tournament.
        """
        try:
            with TOURNAMENTS_FILE.open("r", encoding="utf-8") as file:
                tournaments = json.load(file)
                return (
                    max((tournament["id"] for tournament in tournaments), default=0) + 1
                )
        except FileNotFoundError:
            return 1

    def add_players_to_tournament(self, chess_ids: List[str]) -> bool:
        """
        Adds players to the tournament.

        Args:
            chess_ids (List[str]): A list of chess IDs.

        Returns:
            bool: True if the players were added successfully, False otherwise.
        """
        players = Player.load_players()
        try:
            for chess_id in chess_ids:
                player = next((p for p in players if p.chess_id == chess_id), None)
                if player and player.chess_id not in self.players_list:
                    self.players_list.append(player.chess_id)
                    print(f"Player {player.chess_id} added to tournament {self.name}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
        return True

    def start_tournament(self) -> None:
        """
        Starts the tournament.
        """
        if self.is_started:
            print("Tournament is already started.")
            return
        elif len(self.players_list) < 2:
            print("Tournament needs at least 2 players.")
            return
        else:
            self.is_started = True
            random.shuffle(self.players_list)
            self.start_round()

    def start_round(self) -> None:
        """
        Starts a new round of the tournament.
        """
        if self.current_round_number >= self.rounds:
            self.is_finished = True
            print("Tournament is already completed.")
            return

        round_name = f"Round {self.current_round_number + 1}"
        round_instance = Round(round_name)
        # Get players objects from chess_id list
        players_instance = Player.load_players()
        players_object = [
            next((p for p in players_instance if p.chess_id == chess_id), None)
            for chess_id in self.players_list
        ]
        # Sort players by score
        players = sorted(
            players_object, key=lambda x: x.score if x is not None else -1, reverse=True
        )

        matched_players = set()
        unmatched_players = []

        # First pass: try to match players who haven't played against each other
        for i in range(len(players)):
            if players[i] in matched_players:
                continue
            for j in range(i + 1, len(players)):
                if players[j] in matched_players:
                    continue
                if self._have_played_before(players[i], players[j]):
                    continue

                match = Match(players[i], players[j])
                round_instance.matches.append(match)
                matched_players.update([players[i], players[j]])
                break
            else:
                # Collect unmatched players for second pass
                unmatched_players.append(players[i])

        # Second pass: match remaining unmatched players
        if unmatched_players:
            for i in range(len(unmatched_players)):
                if unmatched_players[i] in matched_players:
                    continue
                for j in range(i + 1, len(unmatched_players)):
                    if unmatched_players[j] in matched_players:
                        continue
                    match = Match(unmatched_players[i], unmatched_players[j])
                    print(match.to_dict())
                    round_instance.matches.append(match)
                    matched_players.update([unmatched_players[i], unmatched_players[j]])
                    break
                else:
                    print(f"Unmatched player: {unmatched_players[i].chess_id}")

        print("New round started.")
        self.rounds_list.append(round_instance)
        self.current_round_number += 1

    def _have_played_before(self, player1: Player, player2: Player) -> bool:
        for round_instance in self.rounds_list:
            for match in round_instance.matches:
                if (
                    match.id_player1 == player1.chess_id
                    and match.id_player2 == player2.chess_id
                ) or (
                    match.id_player1 == player2.chess_id
                    and match.id_player2 == player1.chess_id
                ):

                    return True

        return False
