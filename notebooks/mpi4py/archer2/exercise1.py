"""Exercise: measure the (unidirectional) bandwidth between 2 MPI ranks.
   This version uses Send()/Recv() and numpy arrays.
"""

import sys
import numpy
from mpi4py import MPI

def main(comm, sz, niterations):
    """Report for message size sz and number of iterations niterations"""

    rank = comm.rank
    msg = numpy.ones(sz, numpy.double)

    t0 = MPI.Wtime()

    for n in range(niterations):

        src = n % 2
        dst = (n + 1) % 2

        if rank == src:
            comm.Ssend([msg, sz, MPI.DOUBLE], dst, tag = 999)
        else:
            comm.Recv([msg, sz, MPI.DOUBLE], source = src, tag = 999)

    t1 = MPI.Wtime()

    if rank == 0:
        t = (t1 - t0) / niterations
        report = "Iterations {} Sz: {:8d} Time {:.3e} Bytes/s {:.4e}\n".\
            format(niterations, 8*sz, t, 8.0*sz/t)
        sys.stdout.write(report)


if __name__ == "__main__":
    """Run up to message size 8 bytes * 2^19"""
    niterations = 10000

    if MPI.COMM_WORLD.rank == 0:
        sys.stdout.write("MPI4py bandwidth Ssend version\n")

    main(MPI.COMM_WORLD, 0, niterations)

    for n in range(19):
        sz = 2**n
        main(MPI.COMM_WORLD, sz, niterations)
