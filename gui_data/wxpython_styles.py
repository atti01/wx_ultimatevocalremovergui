import platform

import wx
import wx.lib.agw.artmanager as art


def apply_styles(widget):
    if platform.system() == 'Darwin':
        colors = {
            'fg': '#F6F6F7',
            'bg': '#0e0e0f',
            'disabledfg': '#F6F6F7',
            'selectfg': '#F6F6F7',
            'selectbg': '#003b50'
        }
        font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic")
    else:
        colors = {
            'fg': '#F6F6F7',
            'bg': '#0e0e0f',
            'disabledfg': '#F6F6F7',
            'selectfg': '#F6F6F7',
            'selectbg': '#003b50'
        }
        font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

    widget.SetBackgroundColour(colors['bg'])
    widget.SetForegroundColour(colors['fg'])
    widget.SetFont(font)

# Test the function on a sample widget
app = wx.App()
frame = wx.Frame(None, -1, 'test')
panel = wx.Panel(frame)
apply_styles(panel)
frame.Show()
app.MainLoop()
