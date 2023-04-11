from random import randrange

from linnearReggresion.trainingData.model.trainedDataModel import SingleDataModel, TrainedDataModelJson, \
    TrainedDataModel
from trainingData.infr.dataFilesOperations import readData

def makeSingleNoise(n, range=100):
    x = (randrange(range) - range/2)/1000
    return n + x

def makeNoise(n):
    #deklaracja klonów
    noiseDataParams = []
    noiseData = []
    for i in range(2):
        noiseDataParams.append([])
    #wypelnienie klonów zaszumionymi wartosciami
    for i in n.params:
        for j in noiseDataParams:
            j.append(makeSingleNoise(i))
    for i in noiseDataParams:
        noiseData.append(SingleDataModel(i, makeSingleNoise(n.value)))

    noiseData.append(n)
    return noiseData;

data = TrainedDataModelJson(readData('singleParameter/data.json'))
newSet = []
for singleData in data.values:
    xd = makeNoise(singleData)
    for i in xd:
        newSet.append(i)

data2 = TrainedDataModel(newSet)
data2.print()
