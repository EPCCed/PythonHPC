import sys
import numpy as np

def initroad(road, density, seedval):

    np.random.seed(seedval)

    n = len(road)-2

    rng = np.random.random(n)

    road[1:n+1] = np.where(rng[:] < density, 1, 0)

    ncar = np.sum(road[1:n+1])
    
    return ncar


def updateroad(newroad, oldroad):

    n = len(oldroad)-2

    newroad[1:n+1] = np.where(oldroad[1:n+1]==0, oldroad[0:n], oldroad[2:n+2])

    nmove = (newroad[1:n+1] != oldroad[1:n+1]).sum(dtype=int)
    nmove = nmove / 2

    return nmove


def updatebcs(road):

    n = len(road)-2

    road[0]   = road[n]
    road[n+1] = road[1]


import time

def gettime():

    return time.time()
