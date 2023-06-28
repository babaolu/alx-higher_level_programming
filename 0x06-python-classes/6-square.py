#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Stores a private size field """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ property getter for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ property setter for position """
        if ((type(value) is not tuple) or (len(value) != 2) or
            (value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the area of square"""
        return self.size ** 2

    def my_print(self):
        """ Print square with # character """
        if self.size == 0:
            print("")
        else:
            for ln in range(self.position[1]):
                print("")
        for sz in range(self.size):
            print("{}{}".format(' '*self.position[0], '#'*self.size))
