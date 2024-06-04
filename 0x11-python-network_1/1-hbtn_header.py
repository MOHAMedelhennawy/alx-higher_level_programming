#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""


import urllib
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as resp:
        print(resp.getheader('X-Request-Id'))
