"""Message passing a python object"""

import sys
from mpi4py import MPI

def main(comm):
    """Send a list from rank 0 to rank 1"""

    if comm.rank == 0:
        msg = ["Any", "old", "thing", comm.rank, {"size" : comm.size}]
        comm.send(msg, dest = 1, tag = 999)
    elif comm.rank == 1:
        msg = comm.recv(source = 0, tag = 999)
        sys.stdout.write("Rank 1 received {}\n".format(msg))

if __name__ == "__main__":

    main(MPI.COMM_WORLD)
