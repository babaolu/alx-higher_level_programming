#!/usr/bin/python3
""" Fetching from intranet """
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
        as response:
    for line in response.readline():
        print("\t- {}".format(line))
