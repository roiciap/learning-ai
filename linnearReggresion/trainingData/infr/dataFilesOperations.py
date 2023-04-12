import json


def read_data(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def save_data(path, data):
    toSave = json.dumps(data, indent=2)
    of = open(path, 'w')
    of.writelines(toSave)
    of.close()
