from game import RockPaper


def run_mvp():
    rock = RockPaper()
    rock.game_set()
    rock.run_game()
if __name__ == '__main__':
    run_mvp()