import json


# Definition of the Player class
class Player:
    """Represents a chess player in a tournament."""

    def __init__(self, first_name, last_name, birth_date, chess_id, score=0):
        """Initializes a new player with their first name, last name, birth date, and chess ID.
        Args:
            first_name (str): The player's first name.
            last_name (str): The player's last name.
            birth_date (date): The player's date of birth.
            chess_id (int): The unique identifier for the player in the chess system.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def update_player(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def update_score(self, score):
        """Update the score of a player by adding the given score to the current score."""
        self.score += score

    def to_dict(self):
        """Convert the Player object to a dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score,
        }

    def save_player(self):
        """Saves the player instance to the players.json file, updating if the chess_id already exists."""
        try:
            with open("data/players.json", "r") as file:
                players = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            players = []

        # Check if the player with the same chess_id already exists
        updated = False
        for i, player in enumerate(players):
            if player["chess_id"] == self.chess_id:
                players[i] = self.to_dict()  # Update the existing player
                updated = True
                break

        if not updated:
            players.append(self.to_dict())  # Add new player if not found

        with open("data/players.json", "w") as file:
            json.dump(players, file, indent=4, sort_keys=True)

    @staticmethod
    def load_players():
        """Load all players from the players.json file and convert to player instance."""
        try:
            with open("data/players.json", "r") as file:
                players = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            players = []
        return [Player(**player) for player in players]
