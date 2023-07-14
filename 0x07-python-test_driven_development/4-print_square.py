#!/usr/bin/python3
"""
This module provides a function for printing a square
"""


def print_square(size=0):
    """ Print square of size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("{}".format(size * '#'))
