import tkinter as tk
from tkinter import messagebox


class ChessApp:
    def __init__(self, root):
        self.root = root
        root.title("Chess Club Manager")

        # Créer un menu principal
        menu = tk.Menu(root)
        root.config(menu=menu)

        # Ajouter des items au menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=root.quit)

        # Ajouter des widgets
        self.label = tk.Label(root, text="Welcome to Chess Club Manager")
        self.label.pack(pady=10)

        self.manage_players_button = tk.Button(
            root, text="Manage Players", command=self.manage_players
        )
        self.manage_players_button.pack()

    def manage_players(self):
        messagebox.showinfo("Info", "Manage Players clicked")


def start_chest_gui():
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
