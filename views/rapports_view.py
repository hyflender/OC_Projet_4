import subprocess
from tabulate import tabulate
from config import BASE_DIR, TEMPLATE_DIR, REPORT_DIR, FLAKE8_REPORT_DIR
from jinja2 import Environment, FileSystemLoader
import webbrowser

from models import Player, Tournament


class RapportsView:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    def display_rapports_menu(self):
        """
        Displays the menu for creating rapports.
        """
        print("Menu to create rapports")
        print("----------------------------------------")
        print("Please select an option:")
        print("1. Create a rapport players (List all players in alphabetical order)")
        print("2. Create a rapport tournament (List all tournaments details)")
        print(
            "3. Create a rapport list players on tournament (List all players present on a tournament)"
        )
        print("4. Generate a Flake8 report")
        print("5. Go back to main menu")
        print("----------------------------------------")

    def generate_players_report(self):
        """
        Generates an HTML report of all players sorted alphabetically by first name.
        """
        players = sorted(Player.load_players(), key=lambda x: x.last_name)
        template = self.env.get_template("players_report_template.html")
        html_content = template.render(players=players)

        # Save the rendered HTML to a file
        with open(REPORT_DIR / "players_report.html", "w") as f:
            f.write(html_content)
        print("Players report generated successfully.")

        # Print player information in the terminal
        print("\nPlayer List:")
        for player in players:
            print(
                f"{player.last_name} {player.first_name} - Chess ID: {player.chess_id}"
            )

        report_path = REPORT_DIR / "players_report.html"
        print("----------------------------------------")
        print(f"Players report saved to: {report_path}")
        print("----------------------------------------")

        # Open the generated HTML report file in the default web browser
        webbrowser.open(str(report_path))

    def generate_tournaments_report(self):
        """
        Generates an HTML report of all tournaments.
        """
        tournaments = Tournament.load_tournaments()
        tournaments_dict = [tournament.to_dict() for tournament in tournaments]
        template = self.env.get_template("tournaments_report_template.html")
        html_content = template.render(tournaments=tournaments_dict)

        # Save the rendered HTML to a file
        with open(REPORT_DIR / "tournaments_report.html", "w") as f:
            f.write(html_content)
        print("Tournaments report generated successfully.")

        # Print tournaments information in the terminal
        print("\nTournament List:")
        for tournament in tournaments:
            print(
                f"{tournament.id} {tournament.name} - {tournament.start_date} / {tournament.end_date}"
            )

        report_path = REPORT_DIR / "tournaments_report.html"
        print("----------------------------------------")
        print(f"Tournaments report saved to: {report_path}")
        print("----------------------------------------")

        # Open the generated HTML report file in the default web browser
        webbrowser.open(str(report_path))

    def generate_list_players_on_tournament(self):
        """
        Generates an HTML report of all players present on a tournament.
        """
        tournaments = Tournament.load_tournaments()
        tournaments_dict = [tournament.to_dict() for tournament in tournaments]

        for tournament in tournaments:
            player_list = []
            for player_id in tournament.players_list:
                player = Player.load_player_by_id(player_id)
                if player not in player_list:
                    player_list.append(player.to_dict())
            for tournament_dict in tournaments_dict:
                if tournament_dict["id"] == tournament.id:
                    tournament_dict["players"] = player_list

        template = self.env.get_template("list_players_on_tournament.html")
        html_content = template.render(tournaments=tournaments_dict)

        # Save the rendered HTML to a file
        with open(REPORT_DIR / "list_players_on_tournament.html", "w") as f:
            f.write(html_content)
        print("List players on tournament report generated successfully.")

        # Print tournaments information in the terminal
        print("\nList players on tournament:\n")
        for tournament in tournaments:
            print(
                f"{tournament.id} {tournament.name} - {tournament.start_date} / {tournament.end_date}"
            )
            data = [["First Name", "Last Name", "Chess ID", "Score"]]
            for player_id in tournament.players_list:
                player = Player.load_player_by_id(player_id)
                data.append(
                    [player.first_name, player.last_name, player.chess_id, player.score]
                )
            print(tabulate(data, headers="firstrow", tablefmt="rounded_outline"))
            print("\n")

        report_path = REPORT_DIR / "list_players_on_tournament.html"
        print("----------------------------------------")
        print(f"List players on tournament report saved to: {report_path}")
        print("----------------------------------------")

        # Open the generated HTML report file in the default web browser
        webbrowser.open(str(report_path))

    def generate_flake8_report(self):
        """Generates an HTML Flake8 report for the project."""
        try:
            subprocess.run(
                [
                    "flake8",
                    "--format=html",
                    "--htmldir=" + str(FLAKE8_REPORT_DIR),
                    str(BASE_DIR),
                ],
                check=True,
            )
            print("----------------------------------------")
            print(f"Flake8 report saved to: {FLAKE8_REPORT_DIR}")
            print("----------------------------------------")

            # Open the generated HTML report file in the default web browser
            webbrowser.open(str(FLAKE8_REPORT_DIR) + "/index.html")

        except subprocess.CalledProcessError as e:
            print("Error generating the Flake8 report:", e)
