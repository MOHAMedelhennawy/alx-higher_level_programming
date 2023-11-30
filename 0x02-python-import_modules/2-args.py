#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    le = len(argv) - 1
    print("{} {}".format(le, "argument" if le == 1 else "arguments"), end="")
    print("{}".format("." if le == 0 else ":"))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
