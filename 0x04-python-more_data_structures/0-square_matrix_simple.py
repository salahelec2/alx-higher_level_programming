#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[pow(num, 2) for num in sublist] for sublist in matrix]
    return result
