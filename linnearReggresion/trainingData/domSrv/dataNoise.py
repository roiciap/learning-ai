from linnearReggresion.trainingData.model.trainedDataModel import SingleDataModel
from random import randrange
import numpy as np


def create_single_noise(amplitude=100, divided=1000):
    return (randrange(amplitude) - amplitude / 2) / divided


def make_noise(n):
    new_arr = [n]
    for i in range(2):
        noise = np.array([n + create_single_noise() for n in range(n.params.size)])
        new_arr.append(SingleDataModel(n.params + noise, n.value + create_single_noise()))
    return new_arr
