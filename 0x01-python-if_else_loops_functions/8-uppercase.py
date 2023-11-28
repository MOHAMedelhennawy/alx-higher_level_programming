#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 97 <= ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("",end="\n")