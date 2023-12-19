#!/usr/bin/python3
"""Define a Class"""


class Square:
    """Define a Class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
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
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            if self.__position[1] > i:
                print("")
            if self.__position[0] > 0:
                print(" " * self.__position[0], "#" * self.__size, end="")
            else:
                print("#" * self.__size, end="")
            print()
