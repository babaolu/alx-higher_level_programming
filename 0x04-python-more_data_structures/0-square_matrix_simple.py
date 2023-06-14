#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = []
    for row in matrix:
        square = [col ** 2 for col in row]
        new_matrix.append(square)
    return new_matrix
