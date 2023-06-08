#!/usr/bin/python3
for _ in range(90):
    if (_ % 10) > (_ // 10):
        if _ < 89:
            print("{:02d}".format(_), end=", ")
        else:
            print("{:02d}".format(_))
