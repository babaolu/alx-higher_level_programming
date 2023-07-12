#!/usr/bin/python3
""" Task 0 for adding integers """


def add_integer(a, b=98):
    """ Adding integer b to a """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or a is None:
        raise TypeError("b must be an integer")
    if (a + b) == float('inf'):
        raise ValueError("value is too large")
    return int(a + b)
