
import sys
from mpi4py import MPI

def main(comm):
    """The sum of a list is..."""

    mylist = []
    mylist = comm.reduce([comm.rank], op=MPI.SUM, root=0)

    if comm.rank == 0:
        sys.stdout.write("List of ranks: {}\n".format(mylist))


if __name__ == "__main__":

    main(MPI.COMM_WORLD)

