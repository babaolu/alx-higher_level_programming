#!/usr/bin/python3
""" Implemnents function for saving JSON representation strings to file """
import json


def save_to_json_file(my_obj, filename):
    """ Save JSON representation string to file """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
