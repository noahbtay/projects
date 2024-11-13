#Noah Taylor
#Final project: Dice rolling simulator P3 bring it all together in the game

from player import Player

class Game:
    def __init__(self, players, rounds=1):
        self.players = players
        self.rounds = rounds #sets number of rounds per game

    def play(self):
        for i in range(self.rounds):
            for player in self.players:
                player.roll_dice()

    def get_winner(self):
        highest_score = 0
        winner = None
        for player in self.players:
            if player.score > highest_score:
                highest_score = player.score
                winner = player #updates winner if current player is winning
        return winner

    def test_game():
        name1 = input("Enter name for Player 1: ")
        name2 = input("Enter name for Player 2: ")
        rounds = int(input("Enter the number of rounds for this game: "))

        player1 = Player(name1)
        player2 = Player(name2)

        game = Game([player1, player2], rounds) #creates game with 5 rounds
        game.play() #start the game

        winner = game.get_winner()
        if winner:
            print(f"The winner of this game is {winner.name} and they scored {winner.score}!")

    if __name__ == "__main__":
        game_test()
