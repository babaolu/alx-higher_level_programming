#!/usr/bin/python3
""" This implements the Base class """
import json


class Base:
    """ Base class implementation """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation function """
        if id is not None:
            if not isinstance(id, int):
                raise TypeErro("id must be and integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def nb_objects(cls):
        return cls.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves JSON string representation of list of objects to a file """
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
                return
            myl = [x.__dict__ for x in list_objs]
            new_dict = {}
            for i in range(len(myl)):
                for key, value in myl[i].items():
                    bas_n_sub = []
                    bas_n_sub.append(list_objs[i].__class__)
                    bas_n_sub.extend(list_objs[i].__class__.__bases__)
                    bas_n_sub = [x.__name__ for x in bas_n_sub]
                    for name in bas_n_sub:
                        key = key.removeprefix("_" + name + "__")
                    new_dict[key] = value
                myl[i] = new_dict
                new_dict = {}
            json.dump(myl, f)

    @classmethod
    def load_from_file(cls):
        """ Loads JSON string representation to Python string from file """
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                myl = json.load(f)
                if not myl:
                    return []
                new_list = []
                for item in myl:
                    new_list.append(cls.create(**item))
                return new_list
        except OSError as ose:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ Returns new instance of Base """
        if not dictionary:
            return Base()
        for key, value in dictionary.items():
            if key == "id":
                return Base(value)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts string representation of object to JSON string """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Converts JSON string representation of object ot Python string """
        if not json_string:
            return []
        return json.loads(json_string)
