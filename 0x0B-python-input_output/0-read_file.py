#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    with open(filename) as file:
        print(file.read(), end="")


    # 1- is no need to call file.close()
    # 2- but using the with statement makes the code
    #    compact and much more readable
    # 3- With statment: avoiding bugs and leaks by
    #    ensuring that a resource is properly released
    #    when the code using the resource is completely
    #    executed. with statement itself ensures proper
    #    acquisition and release of resources.
