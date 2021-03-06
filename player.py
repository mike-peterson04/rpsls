class Player:
    def __init__(self):
        self.name = ""
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0

    def play_game(self):
        # ask user to pick gesture
        count = 1
        print(f"it is {self.name}'s turn")
        for gesture in self.gestures:
            print(f"to choose {gesture} press {count}:")
            count += 1
            # input validation
        while True:
            try:
                result = int(input())
                if 0 < result <= len(self.gestures):
                    return self.gestures[result-1]
                else:
                    print(f"Whoops I need a number between 1 and {len(self.gestures)} lets try again")
            except ValueError:
                print(f"Whoops I need a number between 1 and {len(self.gestures)} lets try again:")
