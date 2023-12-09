import wx


class DarkTheme:
    def __init__(self):
        self.colors = {
            'fg': '#F6F6F7',
            'bg': '#0e0e0f',
            'disabledfg': '#F6F6F7',
            'selectfg': '#ffffff',
            'selectbg': '#2f60d8',
        }
        self.fonts = {
            'default': wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL),
        }
        self.images = {
            'button-rest': wx.Bitmap('button-rest.png'),
            'button-disabled': wx.Bitmap('button-disabled.png'),
            'button-pressed': wx.Bitmap('button-pressed.png'),
            'button-hover': wx.Bitmap('button-hover.png'),
        }

    def apply(self, app):
        app.SetNativeTheme('dark')
        self.set_colors()
        self.set_fonts()
        self.set_images()

    def set_colors(self):
        for color, value in self.colors.items():
            wx.SystemSettings.SetColour(color, wx.Colour(value))

    def set_fonts(self):
        for font, value in self.fonts.items():
            wx.SystemSettings.SetFont(font, value)

    def set_images(self):
        for image, value in self.images.items():
            wx.ArtProvider.SetBitmap(image, value)
