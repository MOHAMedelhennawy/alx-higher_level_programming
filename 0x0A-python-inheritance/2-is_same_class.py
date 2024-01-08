#!/usr/bin/python3
"""Module 2-is_same_class.
Returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Return Ture if an instance, otherwise Flase
    
    Args:
        obj: as the object of class
        a_class:T
    """

    if type(obj) == a_class:
        return True
    else:
        return False
