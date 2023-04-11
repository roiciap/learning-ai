import numpy

class SingleDataModel:
    def __init__(self, parameters, values):
        self.value = numpy.array(values)
        self.params = parameters
    def __str__(self):
        return 'params: '+str(self.params)+', value: '+str(self.value)

class TrainedDataModelJson:
    def __init__(self, values):
        arr = []
        for i in values:
            arr.append(SingleDataModel(i["params"], i["value"]))
        self.values = numpy.array(arr)


class TrainedDataModel:
    def __init__(self, values):
        arr = []
        for i in values:
            arr.append(SingleDataModel(i.params, i.value))
        self.values = numpy.array(arr)
    def print(self):
        for i in self.values:
            print(str(i))

