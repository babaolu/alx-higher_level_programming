#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    s_count = my_list.count(search)
    if s_count == 0:
        return my_list
    else:
        new_list = my_list[:]
        for _ in range(s_count):
            new_list[new_list.index(search)] = replace
        return new_list
