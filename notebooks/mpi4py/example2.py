"""A simple blocking Send/Recv pair"""

import sys
import numpy
from mpi4py import MPI

def main(comm, sz):
    """Send a message between ranks 0 and 1"""
    rank = comm.Get_rank()

    if rank == 0:
        msg = numpy.ones(sz, numpy.double)
        comm.Ssend([msg, sz, MPI.DOUBLE], dest = 1, tag = 999)
    elif rank == 1:
        msg = numpy.zeros(sz, numpy.double)
        comm.Recv([msg, sz, MPI.DOUBLE], source = 0, tag = 999)
        sys.stdout.write("Rank 1 received {}".format(msg))

if __name__ == "__main__":

    sz = 4
    main(MPI.COMM_WORLD, sz)
