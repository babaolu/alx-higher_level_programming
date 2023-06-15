#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_add = 0
    freq = 0
    for x, y in my_list:
        weight_add += x * y
        freq += y
    return weight_add/freq
