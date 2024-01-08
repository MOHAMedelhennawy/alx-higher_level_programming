#!/usr/bin/python3

def lookup(obj):
    """Function to returns the list of
    available attributes and methods of an object
    
    Args:
        obj: object to find its methods
    """
    return dir(obj)
