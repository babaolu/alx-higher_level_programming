#!/usr/bin/python3
"""
This module implements a matrix multiplication function
"""


def matrix_mul(m_a, m_b):
    """ Matrix multiplication """
    mlist = "{mat} must be a list"
    mllist = "{mat} must be a list of lists"
    mrect = "each row of {mat} must be of the same size"
    mint = "{mat} should contain only integers or floats"
    mempty = "{mat} can't be empty"
    if not isinstance(m_a, list):
        raise TypeError(mlist.format(mat="m_a"))
    if not isinstance(m_b, list):
        raise TypeError(mlist.format(mat="m_b"))

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError(mllist.format(mat="m_a"))
        if len(row) != len(m_a[0]):
            raise TypeError(mrect.format(mat="m_a"))
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(mint.format(mat="m_a"))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError(mllist.format(mat="m_b"))
        if len(row) != len(m_b[0]):
            raise TypeError(mrect.format(mat="m_b"))
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(mint.format(mat="m_b"))

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError(mempty.format(mat="m_a"))
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError(mempty.format(mat="m_b"))
    new_mat = []
    for i in range(len(m_a)):
        new_mat.append([])
        for j in range(len(m_b[0])):
            new_mat[i].append(sum([m_a[i][k] *
                                   m_b[k][j] for k in range(len(m_a[0]))]))
    return new_mat
