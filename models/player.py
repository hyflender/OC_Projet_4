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

    def update_score(self, score):
        """Updates the player's score by adding the specified score to their current score.

        Args:
            score (int): The score to be added to the player's current score.
        """
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
