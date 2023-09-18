#!/usr/bin/python3
""" This implements the Base class """
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
                return
            myl = [x.__dict__ for x in list_objs]
            new_dict = {}
            for i in range(len(myl)):
                for key, value in myl[i].items():
                    new_dict[key.removeprefix("_" + type(list_objs[i]).__name__
                             + "__")] = value
                myl[i] = new_dict
                new_dict = {}
            json.dump(myl, f)

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
