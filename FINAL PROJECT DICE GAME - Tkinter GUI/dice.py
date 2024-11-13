#Noah Taylor
#Final project: Dice rolling simulator P1 dice making

import random 

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides) #rolls the die and returnsa a random number between 1 and 6

    def dice_test():
        dice = Dice() #create the object
        print(f"Rolling a dice with {dice.sides} amount of sides: {dice.roll()}")

    if __name__ == "__main__":
        dice_test()
