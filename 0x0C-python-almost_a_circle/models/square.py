#!/usr/bin/python3
"""Module square.
Create a square class, inheriting from Rectangle.
"""
from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class describing a square.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            - __size: size
            - __x: position
            - __y: position
            - id: id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Retrieves the size attribute."""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size attribute."""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance.

        Args:
            - id attribute
            - size attribute
            - x attribute
            - y attribute
        """

        if len(kwargs) > 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        else:
            vars = ("id", "size", "x", "y")
            for var, arg in zip(vars, args):
                setattr(self, var, arg)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
