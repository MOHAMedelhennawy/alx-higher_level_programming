#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
    except ZeroDivisionError as E:
        res = None
        print("Exception: {}".format(E), file=sys.stderr)
    except IndexError as E:
        res = None
        print("Exception: {}".format(E), file=sys.stderr)
    return res
