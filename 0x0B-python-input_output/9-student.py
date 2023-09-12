#!/usr/bin/python3
""" This implements the Student class """


class Student:
    """ Student class implementation """
    def __init__(self, first_name, last_name, age):
        """ Instantiation tasks """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dictionary description of self """
        return self.__dict__
