"""Example of timeit from python script"""

import timeit

def main():

    # code to be executed as setup (must include import statement)
    init = "import numpy; nd = numpy.arange(100).reshape((10,10))"

    t = timeit.Timer(stmt= "nd[5][5]", setup= init)
    print(t.repeat(repeat= 3, number= 10000000))

    t = timeit.Timer(stmt= "nd[5,5]", setup= init)
    print(t.repeat(repeat = 3, number= 10000000))

if __name__ == "__main__":

    main()
