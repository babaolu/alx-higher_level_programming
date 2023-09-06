#!/usr/bin/python3
"""
This module provides a function for printing names
"""


def say_my_name(first_name="", last_name=""):
    """ Print name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(first_name) == 0:
        print("I have no name")
        return
    print("My name is {} {}".format(first_name, last_name))
