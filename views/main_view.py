# The Main Menu View - This is the first view that the user sees when they run the program.


class MainView:

    def display_global_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("Welcome to Chess Club Manager - Main Menu")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Rapports")
        print("4. Exit")
        print("----------------------------------------")


class ShowPlateau:
    def __init__(self):
        self.plateau = self.initialiser_plateau()

    def initialiser_plateau(self):
        # Initialiser le plateau avec des cases vides
        plateau = [["   " for _ in range(8)] for _ in range(8)]

        # Symboles Unicode pour les pièces
        pieces_noires = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        pieces_blanches = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        pion_noir = "♟"
        pion_blanc = "♙"

        # Placer les pièces sur le plateau
        plateau[0] = pieces_noires
        plateau[1] = [pion_noir for _ in range(8)]
        plateau[6] = [pion_blanc for _ in range(8)]
        plateau[7] = pieces_blanches

        return plateau

    def afficher_plateau(self):
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
