#!/usr/bin/python3
""" This implements the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization function for Square object """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """ Return informal string representation of Square object """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
