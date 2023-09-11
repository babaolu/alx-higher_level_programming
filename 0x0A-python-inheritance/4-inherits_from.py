#!/usr/bin/python3
"""
This module implements inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is a subclass of a_class
    """
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
