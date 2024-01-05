#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Defines the blueprint of a rectangle.

    Attribute:
        width: the width of the rectangle object.
        height: the height of the rectangle object.
    """
    def __init__(self, width=0, height=0):
        """An object constructor method.
        Initiatilizes Rectangle with width and height.

        Args:
            width: representing object width.
            height: representing object height.

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width object attribute

        Return:
            The width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width object attribute.

        Validates the assignment of the width private attribute.

        Args:
            value: the value to set to width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height object attribute

        Return:
            The height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height object attribute.

        Validates the assignment of the height private attribute.

        Args:
            value: the value to set to height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
