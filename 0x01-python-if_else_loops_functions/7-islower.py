#!/usr/bin/python3
def islower(c):
    asciii = ord(c)
    if asciii >= 97 and asciii <= 122:
        return True
    else:
        return False