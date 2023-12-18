#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except (ZeroDivisionError, ValueError):
        pass
    finally:
        print("Inside result: {:d}".format(x))
