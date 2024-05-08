from models.Player import Player
import os


def test_create_player():
    player = Player("John", "Doe", "2024-01-01", "AA12345")

    assert player.first_name == "John"
    assert player.last_name == "Doe"
    assert player.birth_date == "2024-01-01"
    assert player.chess_id == "AA12345"
    assert player.score == 0


def test_update_player():
    player = Player("Jane", "Doe", "2024-01-01", "AA12345")
    assert player.first_name == "Jane"
    assert player.last_name == "Doe"
    assert player.birth_date == "2024-01-01"
    assert player.chess_id == "AA12345"

    player.update_player("Jane", "Smith", "2024-01-01")

    assert player.first_name == "Jane"
    assert player.last_name == "Smith"
    assert player.birth_date == "2024-01-01"


def test_update_score():
    player = Player("Jane", "Doe", "2024-01-01", "AA12345")
    assert player.score == 0

    player.update_score(10)
    assert player.score == 10


def test_save_player():
    player = Player("Anthony", "Hopkins", "1993-01-01", "AA12345")
    player.save_player()
    assert os.path.exists("data/players.json")


def test_to_dict():
    player = Player("Anthony", "Hopkins", "1993-01-01", "AA12345")
    player_dict = player.to_dict()
    assert player_dict == {
        "birth_date": "1993-01-01",
        "chess_id": "AA12345",
        "first_name": "Anthony",
        "last_name": "Hopkins",
        "score": 0,
    }
