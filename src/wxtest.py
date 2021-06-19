import wx
from docbuilder import *
import wx.lib.scrolledpanel as scrolled

# app = wx.App()
# frame = wx.Frame(None, title='KZVG: Договорник 3000', size=(500, 700))
# frame = wx.Frame(None, style= wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
# frame.Center()
# frame.Show()


# app.MainLoop()

class Example(wx.Frame):

    def __init__(self, parent, title, fields_names):
        super(Example, self).__init__(parent, title=title, size=(500, 800))

        self.InitUI(fields_names)
        self.Centre()

    def InitUI(self, fields_names):

        # panel = wx.Panel(self)

        # Add a panel so it looks the correct on all platforms
        panel = wx.ScrolledWindow(self,wx.ID_ANY)
        panel.SetScrollbars(1, 1, 1, 1)

        sizer = wx.GridBagSizer(15,15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('res/PNG_210619_kzvg-logo-name-transp.png'))
        sizer.Add(icon, pos=(0, 0), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT, border=5)

        text1 = wx.StaticText(panel, label="KZVG Договорник 3000")
        sizer.Add(text1, pos=(0, 2), flag=wx.TOP|wx.RIGHT|wx.BOTTOM, border=15)

        # line = wx.StaticLine(panel)
        # sizer.Add(line, pos=(1, 0), span=(1, 5),
        #     flag=wx.EXPAND|wx.BOTTOM, border=10)

        i = 1
        for field_name in fields_names:
            text = wx.StaticText(panel, label=field_name)
            sizer.Add(text, pos=(i, 0), flag=wx.LEFT, border=10)
            tc = wx.TextCtrl(panel)
            sizer.Add(tc, pos=(i, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
            i = i+1

        button4 = wx.Button(panel, label="Заполнить")
        sizer.Add(button4, pos=(i, 2), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)


def main():


    details_yaml_filename = 'doc_cp1251.yaml'
    doc_details = get_details_from_yaml_cp1251(details_yaml_filename)

    foo = doc_details.keys()
    app = wx.App()
    ex = Example(None, title="KZVG: Договорник 3000", fields_names=foo)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
