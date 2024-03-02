#!/usr/bin/python3
""" Handling errors from server response """
if __name__ == '__main__':
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode())
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
