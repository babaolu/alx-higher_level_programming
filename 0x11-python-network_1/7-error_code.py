#!/usr/bin/python3
""" Handling errors from server response """
if __name__ == '__main__':
    import requests
    import sys

    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.HTTPError as e:
        if e.response.status_code >= 400:
            print("Error code:", e.response.status_code)
