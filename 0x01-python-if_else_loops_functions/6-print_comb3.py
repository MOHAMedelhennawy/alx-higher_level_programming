#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=", ")
print("{}{}".format(i, j))
