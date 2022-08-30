"""An Example of non-blocking Isend/Irecv pairs"""

import sys
import numpy
from mpi4py import MPI

def main(comm):
    """Exchange messages with 'ajoining' ranks"""
    p1 = comm.rank + 1
    m1 = comm.rank - 1
    if p1 >= comm.size: p1 = 0
    if m1 < 0: m1 = comm.size - 1

    smsg = numpy.array([comm.rank], numpy.int)
    rmsg = numpy.zeros(2, numpy.int)

    reqs1 = comm.Issend(smsg, p1)
    reqs2 = comm.Issend(smsg, m1)
    reqr1 = comm.Irecv(rmsg[0:], source = p1)
    reqr2 = comm.Irecv(rmsg[1:], source = m1)

    reqr1.Wait(); reqr2.Wait()
    sys.stdout.write("Rank {} received messages from ranks {} and {}\n"\
                         .format(smsg, rmsg[1], rmsg[0]))

    MPI.Request.Waitall([reqs1, reqs2])

if __name__ == "__main__":

    main(MPI.COMM_WORLD)
