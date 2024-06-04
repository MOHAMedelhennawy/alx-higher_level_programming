#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

import urllib
from urllib import request
from sys import argv

url = argv[1]
with urllib.request.urlopen(url) as resp:
    print(resp.getheader('X-Request-Id'))
