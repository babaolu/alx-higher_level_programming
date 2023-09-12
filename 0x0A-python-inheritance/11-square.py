#!/usr/bin/python3
"""
This implements the Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        """ Instantiated Square class """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Informal string printing """
        return "[Square] {}/{}".format(self.__size, self.__size)
