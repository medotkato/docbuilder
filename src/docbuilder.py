import argparse
import os
import yaml

def yaml_reader (yaml_file: str) -> dict:
    scriptfolder = os.path.dirname(os.path.abspath(__file__))
    print (f'scriptfolder is {scriptfolder}')
    try:
        with open(f'{scriptfolder}\\{yaml_file}','r', encoding="cp1251") as yaml_file:
            details = yaml.safe_load(yaml_file)
    except:
        raise Exception(f'Can\'t find ({yaml_file}) or can\'t load it.')
    return details

def doc_filler (template_docx_filename, details_dic):
    from docxtpl import DocxTemplate
    doc = DocxTemplate(f'{template_docx_filename}')
    doc.render(details_dic)
    out_filename=template_docx_filename.replace('.docx','')
    print (f'Writing to: {out_filename}')
    doc.save(f'{out_filename}_filled.docx')

def yaml_writer (yaml_file: str, yaml_data: dict):
    scriptfolder = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(f'{scriptfolder}\\{yaml_file}','w', encoding="utf-8") as yaml_file:
            yaml.dump(yaml_data, yaml_file, allow_unicode=True, explicit_start=True, indent=4, sort_keys=False)
    except:
        raise Exception(f'Can\'t find ({yaml_file}) or can\'t write to it.')
    return 1

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
    print (f'Reading from: {details_yaml_filename}, using template from {template_docx_filename}')


    details = yaml_reader(details_yaml_filename)

    # dic = dict()
    # for field in doc_details.items():
    #     key = field[0]
    #     val=str(field[1]['value'])
    #     dic.update({key: val})

    doc_filler (template_docx_filename, details)
