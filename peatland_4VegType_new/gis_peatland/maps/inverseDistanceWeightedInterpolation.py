import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def IDW_raster(inputArr, powerNum):
    mask = np.logical_not(np.isnan(inputArr))
    print(mask, mask.shape)

    corrList = np.array([])
    valueList = np.array([])
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i,j]:
                corrList = np.append(corrList, i)
                corrList = np.append(corrList, j)
                valueList = np.append(valueList, inputArr[i,j])
    corrList = corrList.reshape(-1, 2)

    outputArr = np.full(inputArr.shape, np.nan)
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i,j]:
                outputArr[i,j] = inputArr[i,j]
            else:
                weight = np.power((np.power(corrList[:,0]-i, 2) + np.power(corrList[:,1]-j, 2)),powerNum/2)
                weight_sum = np.sum(np.power((np.power(corrList[:,0]-i, 2) + np.power(corrList[:,1]-j, 2)),powerNum/2))
                weight = weight/weight_sum
                outputArr[i,j] = np.sum(valueList*weight)
    return outputArr








