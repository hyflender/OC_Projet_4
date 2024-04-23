# Definition of the Player class
class Player:
    def __init__(self, first_name, last_name, birth_date, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = 0

    def update_score(self, score):
        self.score += score
