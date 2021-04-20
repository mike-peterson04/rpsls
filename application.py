import wx

class Application(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Rock Paper Scissors Lizard Spock")
        contain = wx.Panel(self)
        exit = wx.Button(contain, label="exit")
        self.Bind(wx.EVT_BUTTON, self.close_button, exit)
        self.Bind(wx.EVT_CLOSE, self.close_window)

    def close_button(self,event):
        self.Close(True)

    def close_window(self,event):
        self.Destroy()