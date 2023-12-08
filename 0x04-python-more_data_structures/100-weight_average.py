#!/usr/bin/python3
def weight_average(my_list=[]):
    output = sum([i[1] for i in my_list])
    if my_list == [] or output == 0:
        return 0
    return sum([i * j for i, j in my_list]) / output
