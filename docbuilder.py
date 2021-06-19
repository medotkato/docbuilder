import yaml, os
from docxtpl import DocxTemplate

def get_details_from_yaml_cp1251 (details_yaml_file: dict) -> dict:

    scriptfolder = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(f'{scriptfolder}\\{details_yaml_file}','r', encoding="cp1251") as yaml_file:
            details = yaml.safe_load(yaml_file)
    except:
        raise Exception(f'Can\'t find ({details_yaml_file}) or can\'t load it.')
    return details

def doc_filler (template_filename, details_dic):
    doc = DocxTemplate(f'{template_filename}.docx')
    doc.render(doc_details)
    doc.save(f'{template_filename}_filled.docx')

template_filename = 'KZVG_Contract_Template'
details_yaml_file = 'doc_cp1251.yaml'

doc_details = get_details_from_yaml_cp1251(details_yaml_file)
doc_filler (template_filename, doc_details)
