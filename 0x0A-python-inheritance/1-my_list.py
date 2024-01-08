#!/usr/bin/python3


class MyList(list):
    """Subclassing frOm list itself"""

    def print_sorted(self):
        """Print_sorted to print sorted list"""
        new_list = self[:]
        print("{}".format(sorted(new_list)))
