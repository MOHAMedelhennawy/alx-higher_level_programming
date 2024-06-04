#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

import urllib
from urllib import request


url = 'https://alx-intranet.hbtn.io'
with urllib.request.urlopen(url) as resp:
    print(resp.getheader('X-Request-Id'))
