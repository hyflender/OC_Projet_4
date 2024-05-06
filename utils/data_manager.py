from models.Player import Player
import json


class PlayersData:
    def __init__(self):
        """
        Initializes the PlayersData class with an empty list of players.
        """
        self.players = []

    def save_players(self, players):
        """
        Saves a list of Player objects to a JSON file.

        Args:
            players (list): A list of Player objects to be saved.
        """
        with open("data/players.json", "w") as file:
            json.dump(
                [player.to_dict() for player in players],
                file,
                sort_keys=True,
                indent=4,
            )

    @staticmethod
    def load_players():
        """
        Loads players from a JSON file and returns a list of Player objects.

        Returns:
            list: A list of Player objects if the file is found and properly formatted.
            None: If an error occurs, such as file not found or JSON decode error.

        Raises:
            FileNotFoundError: If the 'data/player.json' file does not exist.
            json.JSONDecodeError: If the JSON file is not properly formatted.
            Exception: For any other exceptions that may occur.
        """
        try:
            with open("data/players.json", "r") as file:
                players_data = json.load(file)
                players = [Player(**data) for data in players_data]
                return players
        except FileNotFoundError:
            print("No players data found")
        except json.JSONDecodeError:
            print("Error decoding JSON from file")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
