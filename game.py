from computer import Computer
from human import Human


class RockPaper:
    def __init__(self):
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
            except:
                print("oops we need a number between 1 and 3 please try again")
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            pass
        #todo create class and methods
