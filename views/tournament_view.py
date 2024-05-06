# The menu for managing tournaments - This class is responsible for displaying the menu for managing tournaments.


class TournamentView:
    def display_tournament_menu(self):
        """
        Displays the menu for managing tournaments.
        """
        print("Menu to manage tournaments")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a new tournament")
        print("2. Manage an existing tournament")
        print("3. View all tournaments")
        print("4. Go back to main menu")
        print("----------------------------------------")

    def display_tournament_submenu(self):
        """
        Displays the menu for managing an existing tournament.
        """
        print("Menu to manage an existing tournament")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Start a new tournament")
        print("2. View tournament's details")
        print("3. Update Tournament")
        print("4. Go back to tournament menu")
        print("----------------------------------------")
