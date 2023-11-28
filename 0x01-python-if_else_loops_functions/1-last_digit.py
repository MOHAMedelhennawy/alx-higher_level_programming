#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number > -1 else (number % 10) - 10

print(f"Last digit of {number:d} is {last}", end=" ")
if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
