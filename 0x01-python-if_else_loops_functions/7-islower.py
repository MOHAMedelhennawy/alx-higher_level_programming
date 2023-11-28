#!/usr/bin/python3
def islower(c):
    asciii = ord(c)
    return bool(96 < asciii < 123)
    # or: return True if asciii >= 97 and asciii <= 122 else False
