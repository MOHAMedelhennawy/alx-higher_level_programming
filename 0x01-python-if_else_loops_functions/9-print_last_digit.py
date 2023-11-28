#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10 if number > -1 else 10 - (number % 10)
    print("{}".format(last), end="")
    return last
