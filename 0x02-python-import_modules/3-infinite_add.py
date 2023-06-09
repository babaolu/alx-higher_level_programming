#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        numlist = list()
        for _ in sys.argv[1:]:
            numlist.append(int(_))
        print(sum(numlist))
    else:
        print(0)
