#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
#        intval = int(value)
        print("{:d}".format(value))
        return True
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
