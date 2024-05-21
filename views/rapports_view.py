# The menu for create rapports - This class is responsible for displaying the menu for creating rapports.
from config import TEMPLATE_DIR, REPORT_DIR
from jinja2 import Environment, FileSystemLoader
import webbrowser

from models import Player


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
        print("2. Create a rapport tournament (List all tournaments)")
        print("3. Create a rapport match (List all matches)")
        print("7. Go back to main menu")
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
