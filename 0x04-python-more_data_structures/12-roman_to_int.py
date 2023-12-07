#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    sum = 0
    roman_number = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    my_list = ["I", "V", "X", "L", "C", "D", "M"]
    last = roman_number[roman_string[0]]
    for i in roman_string:
        if i in roman_number.keys():

            if roman_number[i] <= last:
                sum += roman_number[i]
            else:
                sum -= roman_number[i]
        last = roman_number[i]

    return abs(sum)