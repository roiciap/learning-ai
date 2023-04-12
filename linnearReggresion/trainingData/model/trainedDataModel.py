import numpy

from linnearReggresion.trainingData.model.dataOptions import DataOptions


class SingleDataModel:
    def __init__(self, parameters, values):
        self.value = values
        self.params = numpy.array(parameters)

    def __str__(self):
        return 'params: ' + str(self.params) + ', value: ' + str(self.value)


class TrainedDataModelJson:
    def __init__(self, data):
        self.options = DataOptions(data["options"])
        values = data["data"]
        arr = []
        for i in values:
            toAdd = SingleDataModel(i["params"], i["value"])
            if len(self.options.params) != toAdd.params.size:
                print("Incorrect number of params!!! -> {}".format(toAdd))
            else:
                arr.append(toAdd)
        self.values = arr


class TrainedDataModel:
    def __init__(self, values, options):
        arr = []
        for i in values:
            arr.append(SingleDataModel(i.params, i.value))
        self.values = arr
        self.options = options

    def print(self):
        for i in self.values:
            print(str(i))

    def jsonFormat(self):
        newArr = []
        for i in self.values:
            newArr.append({"value": i.value, "params": i.params.tolist()})
        return newArr
