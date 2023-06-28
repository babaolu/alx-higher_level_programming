#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Stores a private size field """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
