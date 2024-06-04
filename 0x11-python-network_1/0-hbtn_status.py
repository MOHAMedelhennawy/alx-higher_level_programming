#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

import urllib
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as resp:
    contant = resp.read()
    print('Body response:')
    print('\t- type: {}'.format(type(contant)))
    print('\t- content: {}'.format(contant))
    print("\t- utf8 content: {}".format(contant.decode("utf-8")))
