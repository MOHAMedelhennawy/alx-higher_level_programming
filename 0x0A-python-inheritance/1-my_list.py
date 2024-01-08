#!/usr/bin/python3
"""Module 1-my_list.
Creates a class inheriting from the list class.
"""


class MyList(list):
    """Subclassing frOm list itself"""

    def print_sorted(self):
        """Print_sorted to print sorted list"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
