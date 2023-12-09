import wx
from gui_data.wxpython_dnd2 import (CF_HDROP, CF_TEXT, CF_UNICODETEXT, DND_ALL,
                                    DND_FILES, DND_TEXT, FileGroupDescriptor,
                                    FileGroupDescriptorW, Frame, TixTk,
                                    WxPythonDnD)

# ... rest of the code ...

class UVR(wx.Frame):
    """This class represents the main window of the UVR application."""
    # Replace tkinter.Tk() with wx.Frame()
    main_window = Frame()

# ... rest of the code ...

# Replace other Tkinter code with wxPython equivalents
# ...

# ... rest of the code ...
def OnClose(self, event):
    """This function handles the event when the UVR application is closed."""
    # ... rest of the code ...
