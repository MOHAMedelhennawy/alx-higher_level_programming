#!/usr/bin/python3
"""magic class definition"""
import math


class MagicClass:
    """magicclass that makes same bytecode as in the task"""

    def __init__(self, radius):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius
            return None

    def area(self):
        """area function calculates some weird stuff"""
        result = (self.__radius ** 2) * math.pi
        return result

    def circumference(self):
        """also this func calculate some weird stuff"""
        result = (2 * math.pi) * self.__radius
        return result
