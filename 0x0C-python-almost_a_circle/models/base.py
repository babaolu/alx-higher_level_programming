#!/usr/bin/python3
""" This implements the Base class """


class Base:
    """ Base class implementation """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def nb_objects(cls):
        return cls.__nb_objects
