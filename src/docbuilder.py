import argparse
from yaml_handler import *

def values_extractor (yaml_full: dict) -> dict:
    dic = dict()
    for field in yaml_full.items():
        key = field[0]
        val=str(field[1]['value'])
        dic.update({key: val})
    return dic

def docbuilder (template_docx_filename, doc_data, out_docx_filename):
    from docxtpl import DocxTemplate
    doc = DocxTemplate(f'{template_docx_filename}')
    doc.render(doc_data)
    print (f'Writing to: {out_docx_filename}')
    doc.save(f'{out_docx_filename}')

def main():

    my_parser = argparse.ArgumentParser(description='Fill the .docx template with data from .yaml')

    my_parser.add_argument('-t', '--template',
                        metavar='some_template.docx',
                        type=str,
                        help='docx template\'s filename')
    my_parser.add_argument('-d', '--data',
                        metavar='data.yaml',
                        type=str,
                        help='data for filling the template in')
    my_parser.add_argument('-o', '--outfile',
                    metavar='outfile.docx',
                    type=str,
                    help='filename for storing the result')

    args = my_parser.parse_args()

    template_docx_filename = args.template
    data_yaml_filename = args.data
    out_docx_filename = args.outfile

    print (f'Creating {out_docx_filename} using data from {data_yaml_filename} and the .docx template from {template_docx_filename}...')

    details_full = yaml_read (data_yaml_filename)
    details_short = values_extractor (details_full)
    docbuilder (template_docx_filename, details_short, out_docx_filename)

if __name__ == '__main__':
    main()
