#!/usr/bin/python3
import math

class MagicClass:
    def __init__(self, radius):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
                raise TypeError('radius must be a number')

        else:
            self.__radius = radius

    def area(self):
        result = (self.__radius ** 2) * math.pi 
        return result

    def circumference(self):
        result = (2 * math.pi) * self.__radius
        return result
