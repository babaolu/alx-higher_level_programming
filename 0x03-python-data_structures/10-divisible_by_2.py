#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    isdiv2 = []
    for val in my_list:
        if (val % 2) == 0:
            isdiv2.append(True)
        else:
            isdiv2.append(False)
    return isdiv2
