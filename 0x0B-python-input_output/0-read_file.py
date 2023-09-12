#!/usr/bin/python3
""" This implements function for reading from file """


def read_file(filename=""):
    """ Reads from file and prints to standard output """
    with open(filename) as f:
        print(f.read())
