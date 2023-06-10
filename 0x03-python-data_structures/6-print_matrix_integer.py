#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
        return
    else:
        for elem in matrix:
            lenth = len(elem) - 1
            for numb, element in enumerate(elem):
                print("{:d}".format(element), end=" " if numb < lenth else "")
            print("")
