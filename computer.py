from player import Player
import random

class Computer(Player):
    def __init__(self, name = "Computer"):
        super().__init__()
        self.name = name

    # override play_game method for computer players to pick random gesture
    def play_game(self):

        return self.gestures[random.randint(1, len(self.gestures)) - 1]
