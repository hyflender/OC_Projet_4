import datetime
import logging
import os
import re
import json
from config import LOG_FILE

LOG_DIR = LOG_FILE.parent

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def log(message: str) -> None:
    """
    Displays a message to the standard output and logs the message using the logging module.

    Args:
        message (str): The message to be displayed.
    """

    print(message)
    logging.info(message)


def get_user_input(prompt: str) -> str:
    """
    Prompts the user for input and returns the input as a string.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: The user's input.
    """
    return input(prompt)


def get_valid_date(prompt: str, edit: bool = False) -> str:
    """
    Prompts the user for a date input and validates its format. If the input is invalid,
    the user is repeatedly asked until a valid date is provided. Allows for an empty input
    if the 'edit' flag is set, which can be used to skip changing a date during an edit
    operation.

    Args:
        prompt (str): The prompt message to display to the user.
        edit (bool): If True, allows an empty string to be returned without validation.
        This is useful for edit operations where no change is desired.

    Returns:
        str: A valid date string in the format 'DD-MM-YYYY', or an empty string if 'edit'
        is True and the user inputs nothing.
    """
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


def get_valid_chess_id(prompt: str, edit: bool = False) -> str:
    """
    Validates a chess ID from the user, ensuring it follows the format: two uppercase letters followed by five digits.
    If 'edit' is False, it also checks for the ID's uniqueness in the system.

    Args:
        prompt (str): The message to display for user input.
        edit (bool): Indicates if the ID is being edited (True) or created (False). Skips uniqueness check if True.

    Returns:
        str: A valid chess ID meeting format and uniqueness requirements.
    """
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


def clear_console() -> None:
    """
    Clears the console screen based on the operating system.

    Uses 'cls' command for Windows and 'clear' for Unix/Linux/Mac.
    """
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for Unix/Linux/Mac
    else:
        os.system("clear")


def get_user_choice(number_choices: int) -> int:
    """
    Prompt the user to enter a choice within a specified range and validate it.

    Args:
        number_choices (int): The maximum valid choice number.

    Returns:
        int: The validated choice entered by the user.
    """
    while True:
        choice = get_user_input("Enter the number of the option you want to select: ")
        try:
            choice = int(choice)
            if 1 <= choice <= number_choices:
                return choice
            else:
                log(
                    f"Choice out of valid range, please choose between 1 and {number_choices}."
                )
        except ValueError:
            log(f"Invalid choice, please choose between 1 and {number_choices}.")


def get_valid_rounds(prompt: str) -> int:
    """
    Prompt the user to enter the number of rounds for a tournament, ensuring it is a valid integer.
    If the input is empty, defaults to 4 rounds.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        int: The number of rounds, defaulting to 4 if no input is provided.
    """
    while True:
        rounds = get_user_input(prompt)
        if rounds.isdigit():
            return int(rounds)
        if rounds == "":
            return 4
        log("Invalid rounds format, please use an integer.")
