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

    def update(self, *args, **kwargs):
        """ Updates the attributes of a Square object """
        if args is None or not args:
            if kwargs:
                super().update(**kwargs)
                for key, value in kwargs.items():
                    if key == "size":
                        self.size = value
            return
        larg = args
        if len(args) > 1:
            larg = list(args)
            larg.insert(1, args[1])
        super().update(*larg)

    def to_dictionary(self):
        """ Returns dictionary representation of Rectangle object """
        my_dict = super().to_dictionary()
        del my_dict["width"]
        del my_dict["height"]
        my_dict["size"] = self.width
        return my_dict
