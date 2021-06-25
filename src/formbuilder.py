import wx
import yaml_handler
import docbuilder
import argparse
import re
from datetime import datetime

class FormBuilderApp (wx.App):

    def __init__ (self, app_config, doc_config):

        super(FormBuilderApp, self).__init__()

        self.frame = FormBuilderFrame(None, app_config, doc_config)
        self.SetTopWindow(self.frame)
        self.frame.Show()

class FormBuilderFrame(wx.Frame):

    def __init__(self, parent, app_config, doc_config):
        app_title = app_config['app_name']['value']
        super(FormBuilderFrame, self).__init__(parent, title=app_title, size=(500, 800))
        self.InitUI(app_config, doc_config) # create UI
        self.Centre() # put the form in the center of the screen

    def InitUI(self, app_config, doc_config):

        doc_name = doc_config['doc_title']['value']
        doc_fields = doc_config['doc_fields']['value']
        app_logo_path = app_config['res_folder']['value'] + app_config['app_logo']['value']
        button_label = doc_config['form_button_label']['value']

        # Add a scrolled self.panel so it looks the correct on all platforms
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(0, 1, 0, 0)

        sizer = wx.GridBagSizer(10,10)
        i = 0

        icon = wx.StaticBitmap(self.panel, bitmap=wx.Bitmap(app_logo_path))
        sizer.Add(icon, pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.ALIGN_LEFT, border=5)
        text1 = wx.StaticText(self.panel, label=doc_name)
        sizer.Add(text1, pos=(i, 1), flag=wx.TOP|wx.LEFT, border=15)
        i = i + 1

        line = wx.StaticLine(self.panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
        flag=wx.EXPAND|wx.BOTTOM, border=10)
        i = i + 1

        for field in doc_fields.items():
            field_label = field[1]['label']
            field_value = field[1]['value']
            field_name = field[0]
            tc_name = f"{field_name}::{field_label}"

            text = wx.StaticText(self.panel, label=field_label)
            sizer.Add(text, pos=(i, 0), flag=wx.LEFT|wx.ALIGN_RIGHT, border=10)

            tc = wx.TextCtrl(self.panel, value=str(field_value), name=tc_name)
            sizer.Add(tc, pos=(i, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
            i = i + 1

        button = wx.Button(self.panel, label=button_label, size=(500,30))
        sizer.Add(button, pos=(i, 1), span=(1, 2), flag=wx.BOTTOM|wx.RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnButton_Fill_Click (event, app_config, doc_config), id=button.GetId())

        sizer.AddGrowableCol(2)

        self.panel.SetSizer(sizer)
        sizer.Fit(self)

    def grab_fields_data(self) -> dict:
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

    def OnButton_Fill_Click (self, event, app_config, doc_config):


        data_out_dic = self.grab_fields_data()
        docx_data_out_dic = docbuilder.values_extractor(data_out_dic)

        now = datetime.now()
        dt_string = now.strftime("%y%m%d-%H%M%S")

        out_folder_data = app_config['out_folder_data']['value']
        out_folder_docx = app_config['out_folder_docx']['value']
        docx_template_path = app_config['in_folder']['value'] + doc_config['doc_template']['value']

        data_out_path = f'{out_folder_data}{dt_string}_data.yaml'
        docx_out_path = f'{out_folder_docx}{dt_string}_document_filled.docx'

        yaml_handler.yaml_write(data_out_path, data_out_dic)
        docbuilder.docbuilder(docx_template_path, docx_data_out_dic, docx_out_path)

        return True


def main():

    my_parser = argparse.ArgumentParser(description='Fill the .docx template with data from .yaml')

    my_parser.add_argument('-c', '--config',
                        metavar='config.yaml',
                        type=str,
                        help='application\'s config in .yaml file')

    args = my_parser.parse_args()

    app_config_path = args.config

    print (f'Starting app with config from: {app_config_path}')
    app_config = yaml_handler.yaml_read(app_config_path)

    doc_config_path = app_config['in_folder']['value'] + app_config['doc_config_default']['value']

    print (f'Building form using template from: {doc_config_path}')

    doc_config = yaml_handler.yaml_read(doc_config_path)

    app = FormBuilderApp(app_config, doc_config)
    app.MainLoop()

if __name__ == '__main__':
    main()
