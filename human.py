from player import Player



class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("What is this players name?")

