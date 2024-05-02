# menu.py


class PlayerView:
    def display_menu(self):
        print("Menu to manage players")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a new player")
        print("2. Update a player's score")
        print("3. View all players")
        print("4. Exit")

    def get_user_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)

    def display_player(self, player):
        print(player.__dict__)
