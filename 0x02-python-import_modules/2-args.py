#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    print("{} {}".format(argc, "argument" if argc == 1 else "arguments"), end="")
    print("{}".format("." if argc == 0 else ":"))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
