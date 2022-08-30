#!/usr/bin/env python

import sys
import time
import numpy as np

from mpi4py import MPI

from trafficlib import initroad, updatebcs, updateroad, gettime

def main(argv):

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

# Simulation parameters
    seedval = 5743
    ncell = 32000000
    maxiter = 3200000000//ncell
    printfreq = maxiter//10

    nlocal = ncell//size

    bigroad  = np.zeros(ncell,dtype=np.int32)
    newroad  = np.zeros(nlocal+2,dtype=np.int32)
    oldroad  = np.zeros(nlocal+2,dtype=np.int32)

    sbuf = np.zeros(1)
    rbuf = np.zeros(1)

    density = 0.52

    if (rank == 0):

        print(f"Length of road is {ncell}")
        print(f"Number of iterations is {maxiter}")
        print(f"Target density of cars is {density}")
        print(f"Running on {size} process(es)")

        # Initialise road accordingly using random number generator
        print(f"Initialising ...")

        ncars = initroad(bigroad, density, seedval)

        print(f"Actual Density of cars is {format(float(ncars)/float(ncell))}\n")
        print(f"Scattering data ...")

    comm.Scatter(bigroad, oldroad[1:nlocal+1], root=0)

    if (rank == 0):
        print(f"... done\n")

    # Compute neighbours

    rankup   = (rank + 1)
    rankdown = (rank - 1)

    # Wrap-around for cyclic boundary conditions, i.e. a roundabout

    if (rankup == size):
        rankup = 0

    if (rankdown == -1):
        rankdown = size-1

    nmove = 0
    nmovelocal = 0

    comm.barrier()
        
    tstart = MPI.Wtime()

    for iter in range(1, maxiter+1):

        comm.Sendrecv(oldroad[nlocal:nlocal+1], dest=rankup,
                      recvbuf=oldroad[0:1], source=rankdown)

        comm.Sendrecv(oldroad[1:2], dest=rankdown,
                      recvbuf=oldroad[nlocal+1:nlocal+2], source=rankup)

        nmovelocal = updateroad(newroad, oldroad)

        sbuf[0] = nmovelocal
        comm.Allreduce(sbuf, rbuf)
        nmove = rbuf[0]

        # Copy new to old array
        oldroad[1:nlocal+1] = newroad[1:nlocal+1]

        if iter % printfreq == 0:

            if (rank == 0):

                print(f"At iteration {iter} average velocity is {float(nmove)/float(ncars):.6f}")

    tstop = MPI.Wtime()

    if (rank == 0):

        print(f"\nFinished\n")
        print(f"Time taken was {tstop-tstart} seconds")
        print(f"Update rate was {1.0e-6*ncell*maxiter/(tstop-tstart)} MCOPs\n")

if __name__ == "__main__":
    main(sys.argv[1:])
