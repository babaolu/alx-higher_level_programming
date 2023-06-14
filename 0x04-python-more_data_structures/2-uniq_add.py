#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_add = 0
    while my_list:
        uniq_add += my_list[0]
        rem = my_list[0]
        for _ in range(my_list.count(rem)):
            my_list.remove(rem)
    return uniq_add
