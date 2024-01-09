#!/usr/bin/python3
"""Function to add attribute to class"""


def add_attribute(obj, name, user_name):
    """Adding attribute to class.

    Args:
        - obj: The object of the class
        - name: The attribute to adding
        - use_name: The value of name attribute

    Return: New attribute if True, otherwise raise TypeError
    """
    if ( not hasattr(obj, '__dict__') or
        (hasattr(type(obj), '__slots__')
            and not isinstance(type(obj).__slots__, property))):

        setattr(obj, name, user_name)
    else:
        raise TypeError("can't add new attribute")
