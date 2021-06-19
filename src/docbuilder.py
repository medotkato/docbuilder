import argparse
import os
import yaml

def get_details_from_yaml_cp1251 (details_yaml_file: dict) -> dict:
    scriptfolder = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(f'{scriptfolder}\\{details_yaml_file}','r', encoding="cp1251") as yaml_file:
            details = yaml.safe_load(yaml_file)
    except:
        raise Exception(f'Can\'t find ({details_yaml_file}) or can\'t load it.')
    return details

def doc_filler (template_docx_filename, details_dic):
    from docxtpl import DocxTemplate
    doc = DocxTemplate(f'{template_docx_filename}')
    doc.render(details_dic)
    out_filename=template_docx_filename.replace('.docx','')
    doc.save(f'{out_filename}_filled.docx')

if __name__ == '__main__':

    my_parser = argparse.ArgumentParser(description='Fill the template with data')

    my_parser.add_argument('-t', '--template',
                        metavar='some_template.docx',
                        type=str,
                        help='docx template\'s filename')
    my_parser.add_argument('-d', '--details',
                        metavar='details.yaml',
                        type=str,
                        help='details for filling the template in')

    args = my_parser.parse_args()

    template_docx_filename = args.template
    details_yaml_filename = args.details

    doc_details = get_details_from_yaml_cp1251(details_yaml_filename)
    doc_filler (template_docx_filename, doc_details)
