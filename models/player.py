import json
from typing import List, Optional, Dict, Union
from config import PLAYERS_FILE


class Player:
    """
    Represents a chess player.
    """

    def __init__(self, first_name: str, last_name: str, birth_date: str, chess_id: str):
        """
        Initializes a Player instance.
        """
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = 0

    def update_player(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        birth_date: Optional[str] = None,
    ) -> None:
        """
        Updates the player's information and saves the updated data to the JSON file.
        """
        if first_name:
            self.first_name = first_name.capitalize()
        if last_name:
            self.last_name = last_name.capitalize()
        if birth_date:
            self.birth_date = birth_date

        players = Player.load_all_players()
        for p in players:
            if p.chess_id == self.chess_id:
                p.first_name = self.first_name
                p.last_name = self.last_name
                p.birth_date = self.birth_date
                break

        Player.save_all_players(players)

    def update_score(self, score: Optional[int] = None) -> None:
        """
        Updates the player's score and saves the updated data to the JSON file.
        """
        if score is not None:
            self.score = float(score)
            players = Player.load_all_players()
            for p in players:
                if p.chess_id == self.chess_id:
                    p.score = self.score
            Player.save_all_players(players)

    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """
        Serializes the player instance to a dictionary.

        Returns:
            A dictionary representation of the player.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score,
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> "Player":
        """
        Deserializes a dictionary to a Player instance.

        Returns:
            A Player instance.
        """
        player = Player(
            data["first_name"],
            data["last_name"],
            data["birth_date"],
            data["chess_id"],
        )
        player.score = data.get("score", 0)
        return player

    @staticmethod
    def save_all_players(players: List["Player"]) -> None:
        """
        Saves a list of players to a JSON file.
        """
        try:
            with PLAYERS_FILE.open("w", encoding="utf-8") as file:
                json.dump(
                    [player.to_dict() for player in players],
                    file,
                    indent=4,
                    sort_keys=True,
                )
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"An error occurred while saving the players: {e}")

    @staticmethod
    def load_all_players() -> List["Player"]:
        """
        Loads a list of players from a JSON file.

        Returns:
            A list of Player instances.
        """
        try:
            with PLAYERS_FILE.open("r", encoding="utf-8") as file:
                return [
                    Player.from_dict(player_data) for player_data in json.load(file)
                ]
        except FileNotFoundError:
            print("Player data file not found. Creating a new one...")
            return []
        except json.JSONDecodeError as e:
            print(f"An error occurred while loading the players: {e}")
            return []

    @staticmethod
    def _load_player_by_chess_id(chess_id: str) -> Optional["Player"]:
        """
        Loads a player by their chess ID.

        Returns:
            A Player instance if found, None otherwise.
        """
        return next(
            (
                player
                for player in Player.load_all_players()
                if player.chess_id == chess_id
            ),
            None,
        )

    @staticmethod
    def load_players_sorted():
        players = Player.load_all_players()
        return sorted(players, key=lambda x: x.last_name)
