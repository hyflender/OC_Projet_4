# The menu for managing rounds - This class is responsible for displaying the menu for managing rounds.


class RoundsView:
    def display_rounds_menu(self):
        """
        Displays the menu for managing rounds.
        """
        print("Menu to manage rounds")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Manage a round")
        print("2. View all rounds")
        print("3. Go back to main menu")
        print("----------------------------------------")

    def display_existing_rounds_menu(self):
        """
        Displays the menu for managing an existing round.
        """
        print("Menu to manage an existing round")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Start a new round")
        print("2. View round's details")
        print("3. Close Round")
        print("4. Go back to round menu")
        print("----------------------------------------")
