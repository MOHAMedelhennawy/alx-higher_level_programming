#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))    
