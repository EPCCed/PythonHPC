import numpy
import sys
from mpi4py import MPI

def main(comm):
    """The sum of a list is..."""

    total_sum = numpy.array(0, 'i')
    rank = numpy.array(comm.rank, 'i')
    comm.Reduce([rank, MPI.INTEGER], [total_sum, MPI.INTEGER], op=MPI.SUM, root=0)

    if comm.rank == 0:
        sys.stdout.write("Sum of ranks: {}\n".format(total_sum))


if __name__ == "__main__":

    main(MPI.COMM_WORLD)

