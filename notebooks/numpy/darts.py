""" Calculate an approximation to pi via Monte Carlo "darts" method"""

import numpy as np
import timeit

def calc_pi(ntot):
    x = np.random.ranf(ntot)
    y = np.random.ranf(ntot)
    r = np.sqrt(x*x + y*y)
    c = r[ r <= 1.0 ]
    return 4.0*float((c.size))/float(ntot)


def main():
    """Time result for a number of sample sizes (log spacing)"""

    pts = 6
    ntots = np.logspace(1, 8, num = pts, dtype = np.int)

    for n in ntots:

        t = timeit.timeit(stmt = "darts.calc_pi(x)",
                          setup = "import darts; x =" +  str(n),
                          number = 1)
        print("{:9d} {:6.4e} {:10.8f}".format(n, t, calc_pi(n)))


if __name__ == "__main__":
    main()
