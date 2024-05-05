import logging
import os
from pprint import pprint


class Library:
    @staticmethod
    def display_message(message):
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

    def get_user_input(prompt):
        """
        Prompts the user for input and returns the input as a string.

        Args:
            prompt (str): The prompt message to display to the user.

        Returns:
            str: The user's input.
        """
        return input(prompt)

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
