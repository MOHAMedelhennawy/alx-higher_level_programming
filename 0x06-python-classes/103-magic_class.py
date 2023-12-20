#!/usr/bin/python3
import math


class _MagicClass:
    def __init__(self, radius):
        self._MagicClass__radius = 0

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius
            return None


    def area(self):
        radius = self._MagicClass__radius
        squared_radius = radius ** 2
        result = squared_radius * math.pi
        return result

    def circumference(self):
        result = (math.pi * 2) * self._MagicClass__radius
        return result
