#!/usr/bin/python3
def print_square(size):
    """print_square function to print a square
    in a # sympol"""
    if (not isinstance(size, int) or isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    strr = ("#" * size + '\n') * size
    print(strr, end="")
