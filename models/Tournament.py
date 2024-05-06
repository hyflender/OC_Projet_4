# Definition of the Tournament class
class Tournament:
    """Represents a chess tournament, including its details and progress."""

    def __init__(self, name, location, start_date, end_date, rounds=4, current_round_number=0, players=[]):
        """Initializes a new tournament with its basic details.

        Args:
            name (str): The name of the tournament.
            location (str): The location where the tournament is held.
            start_date (date): The starting date of the tournament.
            end_date (date): The ending date of the tournament.
            rounds (int): The number of rounds in the tournament.
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.current_round_number = current_round_number

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
