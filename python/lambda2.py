#!/usr/bin/python3
def my_map(my_func, my_list):
    result = []

    for item in my_list:
        result.append(my_func(item))
    return result

nums = [3, 5, 2, 3, 6, 4]

cuped = my_map(lambda a: a**3, nums)
print(cuped)