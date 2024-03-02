#!/usr/bin/python3
""" Fetching value from header response """
if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    print(res.headers["X-Request-Id"])
