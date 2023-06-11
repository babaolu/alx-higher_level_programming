#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    while (new_string.find("C") != -1):
        idx = new_string.find("C")
        new_string = new_string[:idx] + new_string[idx+1:]
    while (new_string.find("c") != -1):
        idx = new_string.find("c")
        new_string = new_string[:idx] + new_string[idx+1:]
    return (new_string)
