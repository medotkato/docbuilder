import wx
from docbuilder import *
import argparse

class FormBuilder(wx.Frame):

    def __init__(self, parent, title, logo, fields):
        super(FormBuilder, self).__init__(parent, title=title, size=(500, 800))

        self.InitUI(title, logo, fields)
        self.Centre()

    def InitUI(self, title, logo, fields):

        # panel = wx.Panel(self)

        # Add a panel so it looks the correct on all platforms
        panel = wx.ScrolledWindow(self,wx.ID_ANY)
        panel.SetScrollbars(0, 1, 0, 0)

        sizer = wx.GridBagSizer(15,15)
        i = 0

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap(logo))
        sizer.Add(icon, pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.ALIGN_LEFT, border=5)
        text1 = wx.StaticText(panel, label=title)
        sizer.Add(text1, pos=(i, 2), flag=wx.TOP|wx.RIGHT, border=15)
        i = i + 1

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
        flag=wx.EXPAND|wx.BOTTOM, border=10)
        i = i + 1

        for field in fields.items():
            text = wx.StaticText(panel, label=field[1]['label'])
            sizer.Add(text, pos=(i, 0), flag=wx.LEFT, border=10)
            tc = wx.TextCtrl(panel, value=str(field[1]['value']), name=field[0])
            sizer.Add(tc, pos=(i, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
            i = i + 1

        button = wx.Button(panel, label="Заполнить договор", size=(500,30))
        sizer.Add(button, pos=(i, 1), span=(1, 2), flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)


def main():

    my_parser = argparse.ArgumentParser(description='Fill the .docx template with data from .yaml')

    my_parser.add_argument('-t', '--template',
                        metavar='form_template.yaml',
                        type=str,
                        help='form\'s template in .yaml file')

    args = my_parser.parse_args()

    form_template_yaml = args.template
    print (f'Building form using template from: {form_template_yaml}')

    form_template = yaml_read(form_template_yaml)

    form_name = form_template['form_name']
    form_logo_png = form_template['form_logo_png']
    form_fields = form_template['form_fields']

    app = wx.App()
    ex = FormBuilder(None, title=form_name, logo=form_logo_png, fields=form_fields)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
