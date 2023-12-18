import wx
from gui_data.wxpython_dnd import DnDFrame
from gui_data.wxpython_styles import apply_styles


class UVRApp(wx.App):
    def OnInit(self):
        self.frame = DnDFrame(None, title="Ultimate Vocal Remover")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = UVRApp()
    app.MainLoop()
