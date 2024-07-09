import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose Rock, Paper or Scissors:", font=("Arial", 14)).pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", width=10, command=lambda: self.play("Rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", width=10, command=lambda: self.play("Paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", width=10, command=lambda: self.play("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Player: 0, Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.player_score = 0
        self.computer_score = 0

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(player_choice, computer_choice)

        self.result_label.config(text=f"You chose {player_choice}, Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"Player: {self.player_score}, Computer: {self.computer_score}")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
