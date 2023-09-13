#!/usr/bin/python3
""" This implements the Student class """


class Student:
    """ Student class implementation """
    def __init__(self, first_name, last_name, age):
        """ Instantiation tasks """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary description of self """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            mydict = {}
            for key in attrs:
                if key in self.__dict__:
                    mydict[key] = (self.__dict__)[key]
            return mydict
        else:
            return None

    def reload_from_json(self, json):
        for key in json:
            (self.__dict__)[key] = json[key]
