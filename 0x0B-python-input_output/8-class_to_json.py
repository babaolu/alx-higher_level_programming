#!/usr/bin/python3
""" Implements function for obtaining dictionary description of object """


def class_to_json(obj):
    """ Returns dictionary description of argument object """
    return obj.__dict__
