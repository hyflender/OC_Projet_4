from models.player import Player


class Match:
    def __init__(self, id_player1, id_player2, winner=None):
        self.id_player1 = id_player1.chess_id
        self.id_player2 = id_player2.chess_id
        self.winner = winner

    def to_dict(self):
        return {
            "id_player1": self.id_player1,
            "id_player2": self.id_player2,
            "winner": self.winner,
        }

    @staticmethod
    def from_dict(data):
        player1 = Player.load_player_by_id(data["id_player1"])
        player2 = Player.load_player_by_id(data["id_player2"])
        return Match(player1, player2, data["winner"])

    def end_match(self, winner):
        self.winner = winner


