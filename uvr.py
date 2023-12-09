import wx
from gui_data.wxpython.theme.dark import DarkTheme
from gui_data.wxpython.wxpythonDnD import (register_drag_source,
                                           register_drop_target)


class UVR(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.theme = DarkTheme()
        self.theme.apply(self)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        register_drag_source(self, "drag_data")
        register_drop_target(self)

    def OnClose(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    uvr = UVR(None, -1, 'Ultimate Vocal Remover')
    uvr.Show()
    app.MainLoop()
