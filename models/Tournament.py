import json


# Definition of the Tournament class
class Tournament:
    """Represents a chess tournament, including its details and progress."""

    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        rounds=4,
        description="",
        current_round_number=0,
        players=[],
    ):
        """Initializes a new tournament with its basic details.

        Args:
            name (str): The name of the tournament.
            location (str): The location where the tournament is held.
            start_date (date): The starting date of the tournament.
            end_date (date): The ending date of the tournament.
            rounds (int): The number of rounds in the tournament.
            description (str): The description of the tournament.
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.current_round_number = current_round_number
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": self.rounds,
            "players": self.players,
            "current_round_number": self.current_round_number,
        }

    # def add_player(self, player):
    #     """Adds a player to the tournament.

    #     Args:
    #         player (Player): The player to be added to the tournament.
    #     """
    #     self.players.append(player)

    # def start_next_round(self):
    #     """Starts the next round in the tournament."""
    #     self.current_round_number += 1
    #     new_round = Round(self.current_round_number)
    #     self.rounds.append(new_round)

    # def finalize_tournament(self):
    #     """Finalizes the tournament, concluding any necessary wrap-up actions."""
    #     pass

    def save_tournament(self):
        """Saves the tournament instance to the tournaments.json file, updating if the name already exists."""
        try:
            with open("data/tournaments.json", "r") as file:
                tournaments = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tournaments = []

        # Check if the tournament with the same name already exists
        updated = False
        for i, tournament in enumerate(tournaments):
            if tournament["name"] == self.name:
                tournaments[i] = self.to_dict()  # Update the existing tournament
                updated = True
                break

        if not updated:
            tournaments.append(self.to_dict())  # Add new tournament if not found

        with open("data/tournaments.json", "w") as file:
            json.dump(tournaments, file, indent=4, sort_keys=True)

    @staticmethod
    def load_tournaments():
        try:
            with open("data/tournaments.json", "r") as file:
                tournaments_data = json.load(file)
                tournaments = [Tournament(**data) for data in tournaments_data]
                return tournaments
        except FileNotFoundError:
            print("No tournaments data found")
        except json.JSONDecodeError:
            print("Error decoding JSON from file")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
