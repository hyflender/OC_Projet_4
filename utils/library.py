import datetime
import logging
import os
import re
import json


def log(message):
    """
    Displays a message to the standard output and logs the message using the logging module.

    Args:
        message (str): The message to be displayed.
    """

    print(message)

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


def get_valid_date(prompt, edit=False):
    """Prompt for a date and validate its format, keep asking until a valid date is entered."""
    while True:
        date_input = get_user_input(prompt)
        try:
            # if the user wants to edit and the date is empty, return the date
            if edit and date_input == "":
                return date_input
            datetime.datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            log("Invalid date format, please use DD-MM-YYYY.")


def get_valid_chess_id(prompt, edit=False):
    """Prompt for a chess ID, validate its format and check its uniqueness, keep asking until a valid ID is entered."""
    while True:
        chess_id = get_user_input(prompt)
        try:
            if not re.match(r"^[A-Z]{2}\d{5}$", chess_id):
                raise ValueError(
                    "Invalid format, please use 2 uppercase letters followed by 5 digits."
                )
            if not edit:
                with open("data/players.json", "r") as file:
                    players = json.load(file)
                for player in players:
                    if player["chess_id"] == chess_id:
                        raise ValueError("ID already exists")
            return chess_id
        except ValueError as e:
            log(str(e))


def clear_console():
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for Unix/Linux/Mac
    else:
        os.system("clear")


def get_user_choice(number_choices):
    while True:
        choice = get_user_input("Enter the number of the option you want to select: ")
        try:
            choice = int(choice)
            if 1 <= choice <= number_choices:
                return choice
            else:
                raise ValueError("Choice out of valid range")
        except ValueError:
            log(f"Invalid choice, please choose between 1 and {number_choices}.")


def get_user_score(prompt):
    while True:
        score = get_user_input(prompt)
        if score == "":
            return None
        if not score.isdigit():
            log("Invalid score format, please use an integer.")
        return int(score)

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
