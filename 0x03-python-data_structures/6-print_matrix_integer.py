#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (len(matrix) - 1 == 0):
        print("")
        return 
    else:
        for elem in matrix:
            print("{:d} {:d} {:d}".format(elem[0], elem[1], elem[2]))
