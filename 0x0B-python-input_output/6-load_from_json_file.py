#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """Creates an object from JSON file

    Args:
        filename: the name of JSON file

    Return: python obj
    """
    with open(filename) as file_obj:
        file_contant = json.load(file_obj)
        return file_contant
