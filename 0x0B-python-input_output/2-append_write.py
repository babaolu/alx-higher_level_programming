#!/usr/bin/python3
""" Implements a file appending function """


def append_write(filename="", text=""):
    """ Appends to a file """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
