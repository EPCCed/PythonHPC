import numpy as np

def initroad(road, density, seedval):

#  Here we expect a road without halos    

    np.random.seed(seedval)

    n = len(road)

    ncar = 0

    for i in range(0, n):
        
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

        if oldroad[i] == 1:
            if oldroad[i+1] == 1:
                newroad[i] = 1
            else:
                newroad[i] = 0
                nmove = nmove + 1
        else:
            if oldroad[i-1] == 1:
                newroad[i] = 1
            else:
                newroad[i] = 0

#
#  The version below will be easier to express as array operations
#  as it has fewer "if" statements.
#
#        if oldroad[i] == 0:
#            newroad[i] = oldroad[i-1]
#        else:
#            newroad[i] = oldroad[i+1]
#            
#        if oldroad[i] - newroad[i] == 1:
#            nmove = nmove + 1

    return nmove


def updatebcs(road):

    n = len(road)-2

    road[0]   = road[n]
    road[n+1] = road[1]


import time

def gettime():

    return time.time()
