#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Defines the blueprint of a rectangle.

    Attribute:
        width: the width of the rectangle object.
        height: the height of the rectangle object.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """An object constructor method.
        Initiatilizes Rectangle with width and height.

        Args:
            width: representing object width.
            height: representing object height.

        """
        type(self).number_of_instances -= 1
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

    def area(self):
        """The area of rectangle

        Return: the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """The perimeter of rectangle

        Return: the perimeter of rectangle
        """
        mul = 2
        if self.__height == 0 or self.__width == 0:
            mul = 0

        return (self.__height + self.__width) * mul

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = (
            (self.__width * str(self.print_symbol) + '\n') * self.__height
            )
        return rectangle_str[:-1]

    def __repr__(self):
        """Return a formal string representation of the rectangle
        to be able to recreate a new instance by using eval()"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a msg after deleting a object,
        It is called after an objects garbage collection occurs"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area.

        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size.

        Args:
            size: size to set the new rectangle to

        Returns:
            The new Rectan
        """
        return cls(size, size)
