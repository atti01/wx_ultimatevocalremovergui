import wx
import wx.lib.newevent


class DnDFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drop_target = DnDDropTarget(self)
        self.SetDropTarget(self.drop_target)

class DnDDropTarget(wx.DropTarget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.data_object = wx.TextDataObject()
        self.SetDataObject(self.data_object)

    def OnEnter(self, x, y, d):
        return wx.DragCopy

    def OnLeave(self):
        pass

    def OnDrop(self, x, y):
        return True

    def OnData(self, x, y, d):
        if self.GetData():
            data = self.data_object.GetText()
            wx.PostEvent(self.window, DnDEvent(data=data))
        return d
