#!/usr/bin/python3
"""Module Square.
Create a Square class, inheriting from Square.
"""
from models.Square import Square


class Square(Square):
    """Class describing a square.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Square.
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
        """Returns Square representation"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Retrieves size attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """set the size attribute"""

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
