#!/usr/bin/python3
""" Fetching value from header response """
if __name__ == '__main__':
    import requests
    import sys

    values = {"email": sys.argv[2]}
    post = requests.post(sys.argv[1], values)
    print(post.text)
