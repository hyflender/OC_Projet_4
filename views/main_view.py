from test.plateau import Plateau

# The Main Menu View - This is the first view that the user sees when they run the program.


class MainView:
    def __init__(self) -> None:
        # Show the graphical game board
        self.plateau = Plateau()
        self.plateau.afficher_plateau()

    def display_global_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("Welcome to Chess Club Manager - Main Menu")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Manage Rounds")
        print("4. Manage Matches")
        print("5. Generate Rapports")
        print("6. Want a beautiful GUI ?")
        print("7. Exit")
        print("----------------------------------------")
