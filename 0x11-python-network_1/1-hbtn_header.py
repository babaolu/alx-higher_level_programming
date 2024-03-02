#!/usr/bin/python3
""" Fetching value from header response """
if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.headers
        print(header.get("X-Request-Id"))
