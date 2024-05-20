from utils import Logger


class MainView:
    """
    The Main Menu View - This is the first view that the user sees when they run the program.
    """

    def display_global_menu(self) -> None:
        """
        Displays the main menu options to the user.
        """

        Logger.info("Show the display_global_menu(self) method")

        print("Welcome to Chess Club Manager - Main Menu")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Rapports")
        print("4. Exit")
        print("----------------------------------------")


class ShowPlateau:
    """
    Class for displaying the chessboard in the console.
    """

    def __init__(self) -> list:
        self.plateau = self.initialiser_plateau()

    def initialiser_plateau(self):
        """
        Initializes the chessboard with pieces in their starting positions.
        """
        plateau = [["   " for _ in range(8)] for _ in range(8)]

        # Unicode symbols for the pieces
        pieces_noires = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        pieces_blanches = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        pion_noir = "♟"
        pion_blanc = "♙"

        # Place the pieces on the board
        plateau[0] = pieces_noires
        plateau[1] = [pion_noir for _ in range(8)]
        plateau[6] = [pion_blanc for _ in range(8)]
        plateau[7] = pieces_blanches

        return plateau

    def afficher_plateau(self) -> None:
        """
        Displays the chessboard in the console.
        """
        print("    a   b   c   d   e   f   g   h")
        print(" +----------------------------------+")
        for i in range(8):
            ligne = f"{8-i} |"  # Numéro de la ligne au début
            for j in range(8):
                # Appliquer un fond alterné pour chaque case
                back_color = "\033[47m" if (i + j) % 2 == 0 else "\033[40m"
                text_color = "\033[30m" if (i + j) % 2 == 0 else "\033[37m"
                piece = self.plateau[i][j]
                piece = " " + piece + " " if piece.strip() else "   "
                ligne += f"{back_color}{text_color}{piece} \033[0m"
            ligne += f"| {8-i}"
            print(ligne)
        print("    a   b   c   d   e   f   g   h")
        print(" +----------------------------------+")
