import wx

class Application(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Rock Paper Scissors Lizard Spock")
        self.contain = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.close_window)
        status = self.CreateStatusBar()
        self.create_menu()

    def create_menu(self):
        menu = wx.MenuBar()
        file = wx.Menu()
        file.Append(wx.ID_NEW, "New Game", "This starts a New Game of RPSLS")
        file.Append(wx.ID_EXIT, "Exit", "This closes the program")
        menu.Append(file, "File")
        self.SetMenuBar(menu)
        self.Bind(wx.EVT_MENU, self.menu_logic)

    def create_game_ui(self):
        grid = wx.GridSizer(3,5,5)
        player_one_panels = [wx.Panel(self),wx.Panel(self),wx.Panel(self),wx.Panel(self),wx.Panel(self),wx.Panel(self)]
        player_one_buttons = []
        gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        count = 0
        for x in player_one_panels:
            if x != player_one_panels[len(player_one_panels)-1]:
                player_one_buttons.append(wx.Button(x, label=gestures[count]))
                count +=1

        player_two_panels = [wx.Panel(self),wx.Panel(self),wx.Panel(self),wx.Panel(self),wx.Panel(self),wx.Panel(self)]
        player_two_buttons = []
        count = 0
        for x in player_two_panels:
            if x != player_two_panels[len(player_two_panels)-1]:
                player_two_buttons.append(wx.Button(x, label=gestures[count]))
                count +=1
        for x in player_one_panels:
            grid.Add(x)

        return grid
    def new_game(self):
        self.contain.SetSizer(self.create_game_ui(), True)

    def menu_logic(self,event):
        id = event.GetId()
        if id == wx.ID_NEW:
            self.new_game()
        elif id == wx.ID_EXIT:
            self.close_window(event)
    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()
