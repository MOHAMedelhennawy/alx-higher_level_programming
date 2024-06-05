#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests, sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    r = requests.post(url, data=value)

    print(r.text)
