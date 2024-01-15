#!/usr/bin/python3
"""Module Square.
Create a Square class, inheriting from Base.
"""
from models.base import Base


class Square(Base):
    """Class describing a Square.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width of Square"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of Square"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set a height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set a x attribute"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Retrieves y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set a y attribute"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of the Square instance."""

        return self.__width * self.__height

    def display(self):
        """؛rints in stdout the Square instance with the character #"""

        print("\n" * self.__y, end="")
        print((" " * self.__x + "#" * self.__width + '\n')
              * self.__height, end="")

    def __str__(self):
        """Returns Square representation"""

        return (
            f"[Square] ({self.id}) {self.__x}/"
            +
            f"{self.__y} - {self.__width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        """Update the class Square attribute"""

        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            vars = ['id', 'width', 'height', 'x', 'y']
            for var, value in zip(vars, args):
                setattr(self, var, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y}
