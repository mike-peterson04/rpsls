import wx

class Application(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Rock Paper Scissors Lizard Spock")
        contain = wx.Panel(self)
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

    def menu_logic(self,event):
        id = event.GetId()
        if id == wx.ID_NEW:
            pass
        elif id == wx.ID_EXIT:
            self.close_window(event)
    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()
