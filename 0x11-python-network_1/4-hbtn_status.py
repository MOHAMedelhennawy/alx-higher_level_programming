#/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:$\n\
    - type: {}\n\
    - content: {}".format(type(r.text), r.text))