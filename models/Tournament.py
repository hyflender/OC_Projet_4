import json

from models.player import Player
from models.round import Round


# Definition of the Tournament class
class Tournament:

    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        description,
        rounds=4,
    ):
        self.id = Tournament.get_next_id()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.description = description
        self.players_list = []
        self.current_round_number = 0
        self.rounds_list = []

    def to_dict(self):
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
        }

    @staticmethod
    def from_dict(data):
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
        return tournament

    @staticmethod
    def save_tournaments(tournaments):
        try:
            with open("data/tournaments.json", "w") as file:
                json.dump(
                    [tournament.to_dict() for tournament in tournaments],
                    file,
                    indent=4,
                    sort_keys=True,
                )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def load_tournaments():
        try:
            with open("data/tournaments.json", "r") as file:
                tournaments_data = json.load(file)
                return [
                    Tournament.from_dict(tournament) for tournament in tournaments_data
                ]
        except FileNotFoundError:
            return []

    @staticmethod
    def get_next_id():
        try:
            with open("data/tournaments.json", "r") as file:
                tournaments = json.load(file)
                return (
                    max((tournament["id"] for tournament in tournaments), default=0) + 1
                )
        except FileNotFoundError:
            return 1

    def add_players_to_tournament(self, chess_ids):
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
        
    # def start_next_round(self):
    #     """Starts the next round in the tournament."""
    #     self.current_round_number += 1
    #     new_round = Round(self.current_round_number)
    #     self.rounds.append(new_round)

    # def finalize_tournament(self):
    #     """Finalizes the tournament, concluding any necessary wrap-up actions."""
    #     pass
