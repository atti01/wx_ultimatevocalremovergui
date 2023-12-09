import wx

TkdndVersion = None
ARM = 'arm'

class DropTarget(wx.PyDropTarget):
    def __init__(self):
        super().__init__()
        self.data = wx.CustomDataObject("drag_data")
        self.SetDataObject(self.data)

    def OnEnter(self, x, y, d):
        return wx.DragCopy

    def OnLeave(self):
        pass

    def OnDrop(self, x, y):
        return True

    def OnData(self, x, y, d):
        if self.GetData():
            data = self.data.GetData()
            # process data
        return d

class DragSource(wx.PyDropSource):
    def __init__(self, data):
        super().__init__()
        self.data = wx.CustomDataObject("drag_data")
        self.data.SetData(data)
        self.SetData(self.data)

    def GiveFeedback(self, effect):
        return True

def register_drag_source(widget, data):
    drag_source = DragSource(data)
    drag_source.DoDragDrop()

def register_drop_target(widget):
    drop_target = DropTarget()
    widget.SetDropTarget(drop_target)
