#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print("None")
        return
    for item in reversed(my_list):
        print("{:d}".format(item))

# Example 1: Calling the function without providing an argument
print_reversed_list_integer()
# Output: (Nothing is printed)

# Example 2: Calling the function with an empty list
my_list = []
print_reversed_list_integer(my_list)
# Output: (Nothing is printed)

# Example 3: Calling the function with a list
my_list = [1, 2, 3, 4, 5]   
print_reversed_list_integer(my_list)
# Output:
# 5
# 4
# 3
# 2
# 1

# Example 4: Calling the function with None
my_list = None
print_reversed_list_integer(my_list)
# Output: (Nothing is printed)