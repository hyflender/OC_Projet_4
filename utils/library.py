import datetime
import logging
import os
from pprint import pprint
import re
import json


def log(message):
    """
    Displays a message to the standard output and logs the message using the logging module.

    Args:
        message (str): The message to be displayed.
    """

    pprint(message)

    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(
        filename="logs/chest_management.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info(message)

    return message


def get_user_input(prompt):
    """
    Prompts the user for input and returns the input as a string.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: The user's input.
    """
    return input(prompt)


def validate_date(date_str):
    """Validate the date format and return a datetime object if valid, else None."""
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except ValueError:
        log("Invalid date format, please use DD-MM-YYYY.")
        return None


def get_valid_date(prompt):
    """Keep asking for input until a valid date is entered."""
    while True:
        date_input = get_user_input(prompt)
        date = validate_date(date_input)
        if date:
            return date


def validate_chess_id(chess_id):
    """Validate the chess id format and check its uniqueness."""
    try:
        if not re.match(r"^[A-Z]{2}\d{5}$", chess_id):
            raise ValueError(
                "Invalid format, please use 2 uppercase letters followed by 5 digits."
            )

        with open("data/players.json", "r") as file:
            players = json.load(file)
            for player in players:
                if player["chess_id"] == chess_id:
                    raise ValueError("ID already exists")

        return chess_id

    except ValueError as e:
        log(str(e))
        return None


def get_valid_chess_id(prompt):
    """Keep asking for input until a valid chess id is entered."""
    while True:
        chess_id_input = get_user_input(prompt)
        chess_id = validate_chess_id(chess_id_input)
        if chess_id:
            return chess_id


def clear_console():
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for Unix/Linux/Mac
    else:
        os.system("clear")


def get_user_choice(prompt, choices):
    while True:
        choice = get_user_input(prompt)
        if choice in choices:
            return choice
        else:
            log("Invalid choice, please try again.")

    # def configure_logger(name, file_path="debug.log"):
    #     logger = logging.getLogger(name)
    #     if not logger.handlers:  # Pour éviter les duplications
    #         logger.setLevel(logging.INFO)

    #         # Gestionnaire de fichier
    #         file_handler = logging.FileHandler(file_path, encoding="utf-8")
    #         formatter = logging.Formatter(
    #             "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    #         )
    #         file_handler.setFormatter(formatter)

    #         # Gestionnaire de flux
    #         stream_handler = logging.StreamHandler()
    #         stream_handler.setFormatter(formatter)

    #         # Ajouter les gestionnaires au logger
    #         logger.addHandler(file_handler)
    #         logger.addHandler(stream_handler)

    #     return logger
