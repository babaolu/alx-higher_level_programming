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
            raise TypeError(f"<{name}> must be an integer")
        if value <= 0:
            raise ValueError(f"<{name}> must be greater than 0")
