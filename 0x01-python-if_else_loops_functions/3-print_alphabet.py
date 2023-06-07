#!/usr/bin/python3
for _ in range(ord('a'), ord('z') + 1):
    if _ != ord('e') and _ != ord('q'):
        print(f"{chr(_)}", end='')
