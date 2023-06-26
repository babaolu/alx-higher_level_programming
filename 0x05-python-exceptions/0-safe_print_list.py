#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_x = 0
    for elem in my_list[:x]:
        try:
            print("{:d}".format(elem), end="")
            real_x += 1
        except Exception:
            pass
    print("")
    return real_x
