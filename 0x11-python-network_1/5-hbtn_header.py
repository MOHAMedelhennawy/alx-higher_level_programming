#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests, sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
