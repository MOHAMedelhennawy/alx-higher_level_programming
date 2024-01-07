#!/usr/bin/python3
"""Module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """To print My name is followed by first, last name.
    Args:
    first_name: as the first name
    last_name: as the last name

    Raises:
    TypeError: if first name is not passing
    TypeError: if last name is not passing


    Return: nothing return
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
