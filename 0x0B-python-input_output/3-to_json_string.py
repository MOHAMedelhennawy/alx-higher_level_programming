#!/usr/bin/python3
"""Funtion that convert a python obj to json string"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object

    Args:
        my_obj: python representation
    
    Return: JSON representation
    """

    return json.dumps(my_obj)
