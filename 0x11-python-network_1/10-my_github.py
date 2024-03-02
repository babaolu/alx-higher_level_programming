#!/usr/bin/python3
""" Fetching value from header response """
if __name__ == '__main__':
    import requests
    import sys

    res = requests.get('https://api.github.com/user', 
                       auth=(sys.argv[1], sys.argv[2]))
    try:
        val = res.json()
        if val:
            print(val.get("id"))
    except requests.exceptions.JSONDecodeError:
        pass
