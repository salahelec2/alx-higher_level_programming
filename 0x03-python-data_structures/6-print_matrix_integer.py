#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        print("{}".format(" ".join("{}".format(element) for element in elem)))
