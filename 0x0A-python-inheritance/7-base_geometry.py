#!/usr/bin/python3
"""
This module implements class BaseGeometry
"""


class BaseGeometry:
    """ Class BaseGeometry"""
    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the int value """
        if type(value) is not int:
            raise TypeError("<{}> must be an integer".format(name))
        if value <= 0:
            raise ValueError("<{}> must be greater than 0".format(name))
