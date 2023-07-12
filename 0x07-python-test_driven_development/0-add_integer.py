#!/usr/bin/python3
""" Task 0 for adding integers """

def add_integer(a, b=98):
    """ Adding integer b to a """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
