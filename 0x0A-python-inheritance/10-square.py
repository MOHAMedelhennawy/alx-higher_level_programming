#!/usr/bin/python3
"""Module 10-square.
Creates a square class.
"""


Rectangle = __import__("8-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square.
    Private instance attributes:
        - size
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes an instance.

        Args:
            - size: value of both width and height
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Presintation of Square Class"""
        return f"[Rectangle] {self.__size}/{self.__size}"
