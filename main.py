from game import RockPaper
import wx
from application import Application

# def run_mvp():
#     rock = RockPaper()
#     rock.run_game()

def build_window():
    window =wx.App(False)
    frame = Application(None, -1)
    frame.Show()
    window.MainLoop()


if __name__ == '__main__':
    # run_mvp()
    build_window()

