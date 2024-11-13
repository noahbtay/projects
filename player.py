#Noah Taylor
#Final project: Dice rolling simulator P2 player making

from dice import Dice

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0 #starts  with score at 0

    def roll_dice(self):
        dice = Dice()
        roll = dice.roll()

        print(f"{self.name} rolled a {roll}") #prints what player 1 or 2 rolled
        self.score += roll #adds the result of the roll to score

    def player_test():
        name = input("Enter the players name: ")
        player = Player(name)
        player.roll_dice()
        

    if __name__ == "__main__":
        player_test()
        
