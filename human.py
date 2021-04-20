from player import Player



class Human(Player):
    def __init__(self):
        super().__init__()
        # Allow player to name themself
        self.name = input("What is this players name?")

