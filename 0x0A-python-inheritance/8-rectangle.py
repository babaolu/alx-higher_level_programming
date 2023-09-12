#!/usr/bin/python3
"""
This implements Rectangle class
"""


import importlib
BaseGeometry = importlib.import_module('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ Instantiates Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
