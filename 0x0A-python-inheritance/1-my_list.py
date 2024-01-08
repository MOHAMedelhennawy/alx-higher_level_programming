#!/usr/bin/python3


class MyList(list):
    """Subclassing from list itself"""

    def print_sorted(self):
        """Print_sorted to print sorted list"""
        my_list = sorted(self)
        print(my_list)
