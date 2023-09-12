#!/usr/bin/python3
""" This implements function for reading from file """


def read_file(filename=""):
    """ Reads from file and prints to standard output """
    if not isinstance(filename, str):
        raise TypeError("filename is not a string")
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
