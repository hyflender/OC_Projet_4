from models.player import Player


def main():

    players = []

    while True:

        print("Welcome to Chest Club Manager")
        print("-----------------------------")
        print("Please select an option:")
        print("1. Create a new player")
        print("2. Update a player's score")
        print("3. View all players")
        print("4. Exit")

        choice = input("Enter the number of the option you want to select: ")

        if choice == "1":
            # Create a new player
            first_name = input("Enter player's first name: ")
            last_name = input("Enter player's last name: ")
            birth_date = input("Enter player's birth date (YYYY-MM-DD): ")
            chess_id = input("Enter player's chess ID: ")
            new_player = Player(first_name, last_name, birth_date, chess_id)
            players.append(new_player)
            print(f"Player {first_name} {last_name} created successfully!")

        elif choice == "2":
            # Update a player's score
            pass
        elif choice == "3":
            # View all players
            for player in players:
                print(player.__dict__)
        elif choice == "4":
            # Exit
            break


if __name__ == "__main__":
    main()
