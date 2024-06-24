from models.player import Player


class Match:
    _id_counter = 0

    def __init__(self, id_player1, id_player2, winner=None):
        self.id = Match.get_next_id()
        self.id_player1 = id_player1.chess_id
        self.id_player2 = id_player2.chess_id
        self.winner = winner

    def to_dict(self):
        return {
            "id": self.id,
            "id_player1": self.id_player1,
            "id_player2": self.id_player2,
            "winner": self.winner,
        }

    @staticmethod
    def from_dict(data):
        player1 = Player.load_player_by_id(data["id_player1"])
        player2 = Player.load_player_by_id(data["id_player2"])
        match = Match(player1, player2, data["winner"])
        
        return match

    @staticmethod
    def reset_id_counter():
        Match._id_counter = 0

    @staticmethod
    def get_next_id():
        Match._id_counter += 1
        return Match._id_counter

    def end_match(self, winner, looser, equal=None):
        if self.winner is not None:
            raise ValueError("Match has already ended.")
        self.winner = winner
        self.looser = looser
        self.equal = equal
        players = Player.load_players()
        player_winner = next(
            (player for player in players if player.chess_id == self.winner), None
        )
        player_looser = next(
            (player for player in players if player.chess_id == self.looser), None
        )

        if self.equal:
            player_winner.score += 0.5
            player_looser.score += 0.5
            self.winner = "Draw"
        else:
            player_winner.score += 1

        Player.save_players(players)
