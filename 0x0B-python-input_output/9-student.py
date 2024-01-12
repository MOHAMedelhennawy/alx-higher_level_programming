#!/usr/bin/python3
"""Class Student that define a student
"""


class Student:
    """define a class student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation the class

        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return  a dictionary representation
        of a Student instance"""

        return self.__dict__
