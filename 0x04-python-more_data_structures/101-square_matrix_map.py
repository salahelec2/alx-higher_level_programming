#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    result = [list(map(lambda num: num ** 2, sublist)) for sublist in matrix]
    return result
