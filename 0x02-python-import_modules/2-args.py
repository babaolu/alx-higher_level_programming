#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(sys.argv)-1))
        count = 1
        for _ in sys.argv[1:]:
            print("{}: {}".format(count, _))
            count += 1

    else:
        print("0 arguments.")
