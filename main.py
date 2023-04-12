from random import randrange

from linnearReggresion.trainingData.infr.dataFilesOperations import read_data

data = read_data('data.json')
newSet = []
for singleData in data:
    sdCopies = [data[singleData]]
    for param in singleData:
        newParamValues = [data[singleData][param]]
        for i in range(3):
            diff = (randrange(0, 100)/1000) - 500
            newParamValues.append(data[singleData][param] + diff)
        sdCopies.append(newParamValues)
    for i in range(len(sdCopies[0])):
        pv = []
        for j in sdCopies:
            pv.append(sdCopies[j][i])
        newSet.append(pv)

print(newSet)
