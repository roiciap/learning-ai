import numpy

from linnearReggresion.trainingData.model.dataOptions import DataOptions


class SingleDataModel:
    def __init__(self, parameters, values):
        self.value = values
        self.params = numpy.array(parameters, dtype='f')

    def __str__(self):
        return 'params: ' + str(self.params) + ', value: ' + str(self.value)


class TrainedDataModelJson:
    def __init__(self, data):
        params_size = data["paramsSize"]
        self.dataOptions = DataOptions(data["dataOptions"])
        values = data["data"]
        arr = []
        for i in values:
            to_add = SingleDataModel(i["params"], i["value"])
            if len(self.dataOptions.params) != params_size:
                print("ERROR: Incorrect number of params!!! -> {}".format(to_add))
            else:
                arr.append(to_add)
        if len(data["options"]["begin"]["w"]) != params_size:
            print("ERROR: Incorrect number of params in options.begin.w!!!")
        if len(data["dataOptions"]["params"]) != params_size:
            print("ERROR: Incorrect number of params in dataOptions.params!!!")
        self.begin = data["options"]["begin"]
        self.trainingValues = arr


class TrainedDataModel:
    def __init__(self, values, options, begin):
        arr = []
        for i in values:
            arr.append(SingleDataModel(i.params, i.value))
        self.trainingValues = arr
        self.options = options
        param_arr = []
        for _ in self.options.params:
            param_arr.append(0)
        self.manipulateArr = numpy.array(param_arr)
        self.result = {"w": numpy.array(begin["w"]), "b": begin["b"]}

    def print(self):
        for i in self.trainingValues:
            print(str(i))

    def json_format(self):
        data_arr = []
        for i in self.trainingValues:
            data_arr.append({"value": i.value, "params": i.params.tolist()})
        return data_arr

    def manipulate_data(self):
        m_arr = []
        for paramNum in range(len(self.options.params)):
            min_val = self.trainingValues[0].params[paramNum]
            max_val = self.trainingValues[0].params[paramNum]
            for valueNum in range(len(self.trainingValues)):
                min_val = min(min_val, self.trainingValues[valueNum].params[paramNum])
                max_val = max(max_val, self.trainingValues[valueNum].params[paramNum])
            to_multiply = max_val - min_val
            if to_multiply == 0:
                to_multiply = 1
            m_arr.append(to_multiply)
            for valueNum in range(0, len(self.trainingValues)):
                self.trainingValues[valueNum].params[paramNum] = float(self.trainingValues[valueNum].params[
                                                                           paramNum] / to_multiply)
        self.manipulateArr = m_arr

    def reverse_manipulation(self):
        self.result["params"] = self.result["params"] * self.manipulateArr
        for valueNum in range(len(self.trainingValues)):
            self.trainingValues[valueNum].params = self.trainingValues[valueNum].params * self.manipulateArr

    def getCost(self):
        cost = 0
        for i in self.trainingValues:
            cost = cost + (i.params.dot(self.result["w"]) + float(self.result["b"]) - float(i.value)) ** 2
        return cost/2*len(self.trainingValues)
