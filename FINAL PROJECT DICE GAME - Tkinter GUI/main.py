#Noah Taylor
#Final project: FINISHED PROJECT CODE WITH GUI

import tkinter as tk
from player import Player
from game import Game

class DiceRollingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Noah's Dice Rolling Simulator")

        self.name1_entry = self.create_entry("Enter a name for Player 1:")
        self.name2_entry = self.create_entry("Enter a name for Player 2:")
        self.rounds_entry = self.create_entry("Enter the number of rounds:")

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def create_entry(self, label_text):
        label = tk.Label(self.root, text=label_text)
        label.pack()
        entry = tk.Entry(self.root)
        entry.pack()
        return entry
        
    def start_game(self):
       player1 = Player(self.name1_entry.get())
       player2 = Player(self.name2_entry.get())
       rounds = int(self.rounds_entry.get())

       game = Game([player1, player2], rounds)
       game.play()

       winner = game.get_winner()
       if winner:
            self.result_label.config(text=f"The winner is {winner.name} with a score of {winner.score}!")

   
            
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollingApp(root)
    root.mainloop()
