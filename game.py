from computer import Computer
from human import Human


class RockPaper:
    def __init__(self):
        # determine if single player, multiplayer or simulation
        self.games_to_play = 3
        print("Press 1 for single player:")
        print("Press 2 for head to head play")
        print("Press 3 to watch computers duel")
        #input validation
        while True:
            try:
                choice = int(input())
                if choice < 1 or choice > 3:
                    print("oops we need a number between 1 and 3 please try again")
                else:
                    break
            except ValueError:
                print("oops we need a number between 1 and 3 please try again")
        #creating the players
        if choice == 1:
            self.player_one = Human()
            self.player_two = Computer("Player 2")
            self.game_set()

        elif choice == 2:
            self.player_one = Human()
            self.player_two = Human()
            self.game_set()
        else:
            self.player_one = Computer("Player 1")
            self.player_two = Computer("Player 2")
            self.game_set()

    def game_set(self):
        #determining how many times the players want to play
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

    def run_game(self):
        # running the actual game
        win_conditions = {
            "RockScissors": "Rock crushes Scissors",
            "RockLizard": "Rock crushes Lizard",
            "ScissorsPaper": "Scissors cuts Paper",
            "ScissorsLizard": "Scissors decapitate a Lizard",
            "PaperRock": "Paper covers Rock",
            "PaperSpock": "Paper disproves Spock",
            "LizardSpock": "Lizard poisons Spock",
            "LizardPaper": "Lizard eats Paper",
            "SpockScissors": "Spock Smashes Scissors",
            "SpockRock": "Spock Vaporizes Rock"
        }
        win_number = (self.games_to_play - 1)/2 + 1
        # check to see if any player has met the win condition
        while self.player_one.score < win_number and self.player_two.score < win_number:
            p1_choice = self.player_one.play_game()
            p2_choice = self.player_two.play_game()
            if p1_choice == p2_choice:
                print("you tied this round")
            elif p1_choice+p2_choice in win_conditions:
                print(f"{self.player_one.name} wins as their {win_conditions[p1_choice+p2_choice]}")
                self.player_one.score += 1
            else:
                print(f"{self.player_two.name} wins as their {win_conditions[p2_choice + p1_choice]}")
                self.player_two.score += 1
        self.game_win()

    def game_win(self):
        # print congratulations message
        if self.player_one.score > self.player_two.score:
            print(f"Congratulations to {self.player_one.name} who triumphed over {self.player_two.name}")
            print(f"With a score of  {self.player_one.score} to {self.player_two.score}")
        elif self.player_two.score > self.player_one.score:
            print(f"Congratulations to {self.player_two.name} who triumphed over {self.player_one.name}")
            print(f"With a score of  {self.player_two.score} to {self.player_one.score}")
        else:
            print(f"something went wrong: for error tracking {self.player_one.score}, {self.player_two.score} ")

