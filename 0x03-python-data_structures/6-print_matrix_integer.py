#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = len(row)
        iter = 0
        for col in row:
            if iter < length-1:
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col))
            iter += 1
