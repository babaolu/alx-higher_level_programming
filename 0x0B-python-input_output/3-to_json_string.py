#!/usr/bin/python3
""" Implements JSON representation function """
import json


def to_json_string(my_obj):
    """ Returns JSON representation of object """
    return json.dumps(my_obj)
