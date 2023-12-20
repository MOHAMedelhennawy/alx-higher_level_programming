#!/usr/bin/python3
"""Define a Class"""


class Square:
    """Define a Class Square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def __init__(self, a):
        self.a = a

    def __lt__(self, object2):
        return self.a < object2.a

    def __gt__(self, object2):
        return self.a > object2.a

    def __le__(self, object2):
        return self.a <= object2.a

    def __ge__(self, object2):
        return self.a >= object2.a

    def __eq__(self, object2):
        return self.a == object2.a

    def __ne__(self, object2):
        return self.a != object2.a
