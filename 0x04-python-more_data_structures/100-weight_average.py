#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0
    output = []
    for i in my_list:
        mul = i[0] * i[1]
        sum1 += mul
        output.append(i[1])
    return sum1 / sum(output)
