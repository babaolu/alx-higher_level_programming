#!/usr/bin/python3
""" This module implements a function that find a peak """


def find_peak(list_of_integers):
    """ Finding the peak inside a list """
    if not list_of_integers:
        return
    myl = list_of_integers
    peak = myl[0]
    state = 0
    for i in range(1, len(list_of_integers)):
        if state:
            if myl[i] < myl[i - 1]:
                return myl[i - 1]
            else:
                peak = myl[i]
        else:
            if myl[i] > myl[i - 1]:
                state = 1
                peak = myl[i]
    return peak
