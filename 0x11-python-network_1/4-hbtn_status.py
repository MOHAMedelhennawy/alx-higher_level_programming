#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.text))
