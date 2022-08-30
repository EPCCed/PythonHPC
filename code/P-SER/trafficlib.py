import numpy as np

def initroad(road, density, seedval):

    np.random.seed(seedval)

    n = len(road)-2

    ncar = 0

    for i in range(1, n+1):
        
        rng = np.random.random()

        if rng < density:
            road[i] = 1
        else:
            road[i] = 0

        ncar = ncar + road[i]

    return ncar


def updateroad(newroad, oldroad):

    n = len(oldroad)-2

    nmove = 0

    for i in range(1, n+1):

#        if oldroad[i] == 1:
#            if oldroad[i+1] == 1:
#                newroad[i] = 1
#            else:
#                newroad[i] = 0
#                nmove = nmove + 1
#        else:
#            if oldroad[i-1] == 1:
#                newroad[i] = 1
#            else:
#                newroad[i] = 0

        if oldroad[i] == 0:
            newroad[i] = oldroad[i-1]
        else:
            newroad[i] = oldroad[i+1]

        if newroad[i] != oldroad[i]:
            nmove = nmove + 1

    nmove = nmove/2

    return nmove


def updatebcs(road):

    n = len(road)-2

    road[0]   = road[n]
    road[n+1] = road[1]


import time

def gettime():

    return time.time()
