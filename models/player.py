import json


# Definition of the Player class
class Player:

    def __init__(self, first_name, last_name, birth_date, chess_id):

        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = 0

    def update_player(self, first_name=None, last_name=None, birth_date=None):
        if first_name:
            self.first_name = first_name.capitalize()
        if last_name:
            self.last_name = last_name.capitalize()
        if birth_date:
            self.birth_date = birth_date

    def update_score(self, score=None):
        if score:
            self.score = score

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score,
        }

    @staticmethod
    def from_dict(data):
        player = Player(
            data["first_name"], data["last_name"], data["birth_date"], data["chess_id"]
        )
        player.score = data.get("score", 0)
        return player

    @staticmethod
    def save_players(players):
        try:
            with open("data/players.json", "w") as file:
                json.dump(
                    [player.to_dict() for player in players],
                    file,
                    indent=4,
                    sort_keys=True,
                )
        except (FileNotFoundError, json.JSONDecodeError):
            print("An error occurred while saving the players.")

    @staticmethod
    def load_players():
        try:
            with open("data/players.json", "r") as file:
                return [
                    Player.from_dict(player_data) for player_data in json.load(file)
                ]
        except FileNotFoundError:
            return []
