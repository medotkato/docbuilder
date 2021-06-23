import wx
from docbuilder import *
import argparse
import re
from datetime import datetime

class FormBuilderApp (wx.App):

    def __init__ (self, form_config):

        super(FormBuilderApp, self).__init__()

        form_name = form_config['form_name']
        form_logo_png = form_config['form_logo_png']
        form_fields = form_config['form_fields']

        self.frame = FormBuilderFrame(None, title=form_name, logo=form_logo_png, fields=form_fields)
        self.SetTopWindow(self.frame)
        self.frame.Show()

class FormBuilderFrame(wx.Frame):

    def __init__(self, parent, title, logo, fields):
        super(FormBuilderFrame, self).__init__(parent, title=title, size=(500, 800))
        self.InitUI(title, logo, fields) # create UI
        self.Centre() # put the form in the center of the screen

    def InitUI(self, title, logo, fields):

        # Add a scrolled self.panel so it looks the correct on all platforms
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(0, 1, 0, 0)

        sizer = wx.GridBagSizer(10,10)
        i = 0

        icon = wx.StaticBitmap(self.panel, bitmap=wx.Bitmap(logo))
        sizer.Add(icon, pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.ALIGN_LEFT, border=5)
        text1 = wx.StaticText(self.panel, label=title)
        sizer.Add(text1, pos=(i, 2), flag=wx.TOP|wx.RIGHT, border=15)
        i = i + 1

        line = wx.StaticLine(self.panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
        flag=wx.EXPAND|wx.BOTTOM, border=10)
        i = i + 1

        for field in fields.items():
            field_label = field[1]['label']
            field_value = field[1]['value']
            field_name = field[0]
            tc_name = f"{field_name}::{field_label}"

            text = wx.StaticText(self.panel, label=field_label)
            sizer.Add(text, pos=(i, 0), flag=wx.LEFT|wx.ALIGN_RIGHT, border=10)

            tc = wx.TextCtrl(self.panel, value=str(field_value), name=tc_name)
            sizer.Add(tc, pos=(i, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
            i = i + 1

        button = wx.Button(self.panel, label="Заполнить договор", size=(500,30))
        sizer.Add(button, pos=(i, 1), span=(1, 2), flag=wx.BOTTOM|wx.RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Fill_Click, id=button.GetId())

        sizer.AddGrowableCol(2)

        self.panel.SetSizer(sizer)
        sizer.Fit(self)

    def grab_data_dic(self):
        data_out_dic = dict()
        sizer = self.panel.GetSizer()
        children = sizer.GetChildren()
        for child in children:
            widget = child.GetWindow()
            if isinstance(widget, wx.TextCtrl):
                field_name, field_label = re.split('::', widget.GetName())
                field_value = widget.GetValue()
                data_out_dic.update({field_name: {'label': field_label, 'value': field_value}})
        return data_out_dic

    def OnButton_Fill_Click (self, event):

        yaml_out_dic = self.grab_data_dic()
        data_out_dic = values_extractor(yaml_out_dic)

        now = datetime.now()
        dt_string = now.strftime("%y%m%d-%H%M%S")

        in_folder = 'in/'
        out_folder = 'out/'
        out_folder_data_yaml = f'{out_folder}data_yaml/'
        out_folder_docx = f'{out_folder}docx/'

        data_out_filename = f'{out_folder_data_yaml}{dt_string}_Contract_data.yaml'
        docx_out_filename = f'{out_folder_docx}{dt_string}_Contract_filled.docx'
        docx_template_filename = f'{in_folder}/Template.docx'

        yaml_write(data_out_filename, data_out_dic)
        doc_builder(docx_template_filename, data_out_dic, docx_out_filename)

        return True


def main():

    my_parser = argparse.ArgumentParser(description='Fill the .docx template with data from .yaml')

    my_parser.add_argument('-c', '--config',
                        metavar='form_config.yaml',
                        type=str,
                        help='form\'s config in .yaml file')

    args = my_parser.parse_args()

    form_config_yaml = args.config

    print (f'Building form using template from: {form_config_yaml}')

    form_config = yaml_read(form_config_yaml)

    app = FormBuilderApp(form_config)
    app.MainLoop()

if __name__ == '__main__':
    main()
