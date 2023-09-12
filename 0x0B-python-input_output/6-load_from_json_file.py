#!/usr/bin/python3
""" Implemnents function for reading JSON representation strings from file """
import json


def load_from_json_file(filename):
    """ Read JSON representation string from file """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
