from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now().isoformat()
        self.end_time = None
        self.matches = []

    def are_all_matches_completed(self):
        return all(match.winner is not None for match in self.matches)

    def end_round(self):
        if self.are_all_matches_completed():
            self.end_time = datetime.now().isoformat()
            print("Round ended successfully.")
            return True
        else:
            print("Not all matches are completed yet.")
            return False

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.to_dict() for match in self.matches],
        }

    @staticmethod
    def from_dict(data):
        round_instance = Round(data["name"])
        round_instance.start_time = data["start_time"]
        round_instance.end_time = data["end_time"]
        round_instance.matches = [
            Match.from_dict(match_data) for match_data in data["matches"]
        ]
        return round_instance
