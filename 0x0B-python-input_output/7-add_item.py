#!/usr/bin/python3
""" Implements for adding commandline arguments to a file """
import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if len(sys.argv) > 1:
    my_list = load_from_json_file("add_item.json")
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, "add_item.json")
else:
    save_to_json_file([], "add_item.json")
