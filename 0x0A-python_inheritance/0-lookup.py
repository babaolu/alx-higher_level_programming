#!/usr/bin/python3


"""
This modudle implements lookup function
"""


def lookup(obj):
    """
    Returns list of available attributes of obj
    """
    return dir(obj)
