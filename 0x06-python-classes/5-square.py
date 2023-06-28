#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Stores a private size field """
        self.size = size

    @property
    def size(self):
        """ Property getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Property setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of square"""
        return self.size ** 2

    def my_print(self):
        """ Print square with # character """
        for sz in range(self.size):
            print("{}".format('#'*self.size))
