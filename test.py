import pandas as pd
import math
import numpy as np

def ManhattanDistance(point_array_1: list, point_array_2: list):
    length_1 = len(point_array_1)
    length_2 = len(point_array_2)

    if length_2 != length_1:
        raise Exception("The dimensions of given points are not equal")


    else:
        point_array_1 = np.array(point_array_1)
        sum = 0
        for i in range(length_1):
            sum += abs(point_array_1[i] - point_array_2[i])

        return sum


def Euclidean(x: list, y: list):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance


def PrintArray(arr):
    for i in arr:
        print(i)


def PrintManhattan(targetPoint):
    man_dist = []
    for i in range(l):
        res = round(ManhattanDistance(values[i][:-1], targetPoint[:-1]), 1)
        man_dist.append({"distance": res, "index": i + 1})

    return man_dist


def PrintEuclidean(targetPoint):
    euc_dist = []
    for i in range(l):
        res = round(Euclidean(values[i][:-1], targetPoint[:-1]), 1)
        euc_dist.append({"distance": res, "index": i + 1})
    return euc_dist


features = ["UAW", "UUCW", "TCF", "ECF"]

data = pd.read_csv("UCP-Dataset.csv")
df = data.drop(features, axis=1)
efforts = data["Real_Effort"]
values = df.values.tolist()
l = len(values)

testDF = pd.read_csv("testData.csv")
testDF = testDF.drop(features, axis=1)
testEfforts = testDF["Real_Effort"]
testData = testDF.values

manDistances = PrintEuclidean(testData[0])
manDistances = sorted(manDistances, key=lambda i: i['distance'])

PrintArray(manDistances)
