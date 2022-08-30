"""Importing and using MPI.COMM_WORLD"""

import sys
from mpi4py import MPI

def main(comm):
    """Report rank and size of this communicator"""
    rank = comm.rank
    size = comm.size
    sys.stdout.write("Hello from rank {:2d} of {:2d}\n".format(rank, size))

if __name__ == "__main__":
    """Execute in MPI.COMM_WORLD"""
    main(MPI.COMM_WORLD)
