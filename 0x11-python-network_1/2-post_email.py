#!/usr/bin/python3
""" Fetching value from header response """
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(sys.argv[1], data.encode('ascii'))
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode())
