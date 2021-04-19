from computer import Computer
from human import Human


class RockPaper:
    def __init__(self):
        self.games_to_play = 3
        print("Press 1 for single player:")
        print("Press 2 for head to head play")
        print("Press 3 to watch computers duel")
        while True:
            try:
                choice = int(input())
                if choice < 1 or choice > 3:
                    print("oops we need a number between 1 and 3 please try again")
                else:
                    break
            except ValueError:
                print("oops we need a number between 1 and 3 please try again")
        if choice == 1:
            self.player_one = Human()
            self.player_two = Computer()
            self.game_set()

        elif choice == 2:
            self.player_one = Human()
            self.player_two = Human()
            self.game_set()
        else:
            self.player_one = Computer()
            self.player_two = Computer()
            self.game_set()

    def game_set(self):
        while True:
            try:
                print("How many games do you wish to play")
                game_choice = int(input("please enter a number 3 or larger (it must be an odd number)"))

                if game_choice % 2 == 0 or game_choice < 3:
                    print("Oops we need and odd number greater and 3 lets try again")
                else:
                    self.games_to_play = game_choice
                    break
            except ValueError:
                print("Oops we need and odd number greater and 3 lets try again")
