#!/usr/bin/python3
"""Function to add attribute to class"""


def add_attribute(obj, name, user_name):
    """Adding attribute to class.

    Args:
        - obj: The object of the class
        - name: The attribute to adding
        - use_name: The value of name attribute
    """

    if all(name, user_name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, user_name)
