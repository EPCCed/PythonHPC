"""Creating a Cartesian Communicator"""

import sys
from mpi4py import MPI

def main(parent):
    """Create a 2-d Cartesian communicator from parent communicator"""

    dims = MPI.Compute_dims(parent.size, 2)

    comm = parent.Create_cart(dims, periods = [True, False])
    rank = comm.Get_rank()
    coords = comm.Get_coords(rank)
    upx = comm.Shift(0, 1)
    upy = comm.Shift(1, 1)

    out = "Rank{:2d} coords{:2d} {:2d} upx(src,dst) {} upy(src,dst) {}\n"\
                         .format(rank, coords[0], coords[1], upx, upy)
    sys.stdout.write(out)

if __name__ == "__main__":
    """Execute in MPI.COMM_WORLD"""
    main(MPI.COMM_WORLD)
