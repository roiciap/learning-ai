import json


def readData(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def saveData(path, data):
    toSave = json.dumps(data)
    of = open(path, 'w')
    of.write(toSave)


