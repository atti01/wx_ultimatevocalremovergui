import wx
from wx.lib.agw import pybusyinfo as PBI


class DnDEvent:
    pass

class DnDWrapper:
    def _require(self, wxroot):
        pass

    def _substitute_dnd(self, *args):
        pass

    def _dnd_bind(self, what, sequence, func, add, needcleanup=True):
        pass

    def dnd_bind(self, sequence=None, func=None, add=None):
        pass

    def drag_source_register(self, button=None, *dndtypes):
        pass

    def drag_source_unregister(self):
        pass

    def drop_target_register(self, *dndtypes):
        pass

    def drop_target_unregister(self):
        pass

    def platform_independent_types(self, *dndtypes):
        pass

    def platform_specific_types(self, *dndtypes):
        pass

    def get_dropfile_tempdir(self):
        pass

    def set_dropfile_tempdir(self, tempdir):
        pass

class Frame(wx.Frame, DnDWrapper):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.TkdndVersion = self._require(self)

class TixTk(wx.TixTk, DnDWrapper):
    def __init__(self, *args, **kw):
        wx.TixTk.__init__(self, *args, **kw)
        self.TkdndVersion = self._require(self)
