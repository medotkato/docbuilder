import yaml

def yaml_read (yaml_file: str) -> dict:
    # scriptfolder = os.path.dirname(os.path.abspath(__file__))
    # print (f'scriptfolder is {scriptfolder}')
    try:
        with open(f'{yaml_file}','r', encoding="utf-8") as yaml_file:
            details = yaml.safe_load(yaml_file)
    except:
        raise Exception(f'Can\'t find ({yaml_file}) or can\'t load it.')
    return details

def yaml_write (yaml_file: str, yaml_data: dict):
    try:
        with open(f'{yaml_file}','w', encoding="utf-8") as yaml_file:
            yaml.dump(yaml_data, yaml_file, allow_unicode=True, explicit_start=True, indent=4, sort_keys=False)
    except:
        raise Exception(f'Can\'t find ({yaml_file}) or can\'t write to it.')
    return 1

def main():
    return 1

if __name__ == '__main__':
    main()
