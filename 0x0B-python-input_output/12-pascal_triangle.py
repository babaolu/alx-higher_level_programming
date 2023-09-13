#!/usr/bin/python3
""" This implements a Pascal's triangle function """


def pascal_triangle(n):
    """ Creates a representation of pascal's triangle """
    pt = []
    if n <= 0:
        return pt
    for x in range(n):
        if x == 0:
            pt.append([1])
            continue
        prev = pt[-1]
        curr = []
        temp = 0
        for v in prev:
            curr.append(temp + v)
            temp = v
        curr.append(1)
        pt.append(curr)
    return pt
