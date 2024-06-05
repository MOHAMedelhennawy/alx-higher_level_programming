#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get['X-Request-Id'])
