from utils.library import log, get_user_input
import unittest.mock as mock


def test_log():
    log("test message log")
    assert True


def test_get_user_input():
    with mock.patch("builtins.input", return_value="test message"):
        user_input = get_user_input("Enter a test message: ")
        assert user_input == "test message"
