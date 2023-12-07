#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    val = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sum = 0
    last = 0
    for i in range(len(roman_string) - 1, -1, -1):
        if val[roman_string[i]] >= last:
            sum += val[roman_string[i]]
        else:
            sum -= val[roman_string[i]]
        last = val[roman_string[i]]
    return sum
