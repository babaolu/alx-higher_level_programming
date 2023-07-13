#!/usr/bin/python3
"""
Module describing a function that performs elemental division
"""


def matrix_divided(matrix=[[]], div=1):
    """ Divides elementally by div """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            val = round(val/div, 2)
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
