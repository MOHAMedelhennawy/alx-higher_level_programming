#!/usr/bin/python3
"""Function to convert a JSON string to python obj"""

import json


def from_json_string(my_str):
    """Returns an python object represented by a JSON string

    Args:
        my_str: JSON representation
    
    Return: python representation
    """

    return json.loads(my_str)
