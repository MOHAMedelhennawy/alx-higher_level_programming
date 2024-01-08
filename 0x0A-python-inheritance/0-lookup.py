#!/usr/bin/python3
"""Module 0-lookup.
Finding a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Function to returns the list of
    available attributes and methods of an object

    Args:
        obj: object to find its methods
    """
    return dir(obj)
