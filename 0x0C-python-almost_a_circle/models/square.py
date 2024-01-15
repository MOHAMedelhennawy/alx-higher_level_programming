#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        else:
            vars = ("id", "size", "x", "y")
            for var, arg in zip(vars, args):
                setattr(self, var, arg)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}