#!/usr/bin/python3
"""
This module implements Rectangle class
"""


import importlib
mymod = importlib.import_module('7-base_geometry')


class Rectangle(mymod.BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        __width = width
        __height = height
