import yaml
import os


def generate_paths(config, path = ''):
    folders = []
    if type(config) == list:
        folders = config
    elif type(config) == dict:
        folders = config.keys()

    response = []
    for folder in folders:
        _values = config[folder]
        if type(_values) == dict:
            response += generate_paths(_values, folder)
        else:
            for file in _values:
                if type(file) == dict:
                    response += generate_paths(file, folder)
                elif type(file) == str:
                    response.append(f'{path}/{folder}/{file}')
    return response


if __name__ == '__main__':
    with open('./config.yaml', "r") as stream:
        config = yaml.safe_load(stream)
        for path in generate_paths(config, './templates'):
            print(path)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # f = open(path, mode="wb")
            # f.write()
