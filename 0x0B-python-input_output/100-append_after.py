#!/usr/bin/python3
""" Implements function for inserting text """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts line of text after a line containing a string """
    if not (search_string and new_string):
        return
    with open(filename, mode="r+", encoding="utf-8") as f:
        line_list = f.readlines()
        for i in range(len(line_list)):
            if search_string in line_list[i]:
                line_list.insert(i+1, new_string)
        f.seek(0)
        f.writelines(line_list)
