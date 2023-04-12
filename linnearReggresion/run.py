from linnearReggresion.trainingData.domSrv.dataNoise import make_noise
from linnearReggresion.trainingData.model.trainedDataModel import TrainedDataModelJson, \
    TrainedDataModel
from trainingData.infr.dataFilesOperations import read_data, save_data

data = TrainedDataModelJson(read_data('singleParameter/data.json'))
newSet = []
for singleData in data.values:
    xd = make_noise(singleData)
    for i in xd:
        newSet.append(i)

data2 = TrainedDataModel(newSet, data.options)
data2.print()
# print(data2.values[0].params)

save_data('singleParameter/data2.json', data2.jsonFormat())
