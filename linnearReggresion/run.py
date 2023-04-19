from linnearReggresion.trainingData.domSrv.dataNoise import make_noise
from linnearReggresion.trainingData.model.trainedDataModel import TrainedDataModelJson, \
    TrainedDataModel
from trainingData.infr.dataFilesOperations import read_data, save_data

data = TrainedDataModelJson(read_data('input/singleParameter/data.json'))
newSet = []
for singleData in data.trainingValues:
    xd = make_noise(singleData)
    for i in xd:
        newSet.append(i)

data2 = TrainedDataModel(data.trainingValues, data.dataOptions, data.begin)
# data2.manipulate_data()
print(round(data2.getCost(), 2))
# data2.reverse_manipulation()
save_data('input/singleParameter/data2.json', data2.json_format())
