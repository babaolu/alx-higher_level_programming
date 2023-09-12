#!/usr/bin/python3
""" Implements JSON representation function """
import json


def from_json_string(my_str):
    """ Returns object from JSON representation """
    return json.loads(my_str)
