#!/usr/bin/python3
"""Funtion that convert a python obj to json string"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object

    Args:
        my_obj: JSON representation
    """

    return json.dumps(my_obj)
# If you have python obj and want to convert to
# json opj, you use json.dumbs(),
# It takes the Python object as input and
# returns a JSON string. and it's call Encoding (Serializing) JSON
