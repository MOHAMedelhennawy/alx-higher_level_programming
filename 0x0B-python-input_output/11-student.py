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

    def to_json(self, attrs=None):
        """Return  a dictionary representation
        of a Student instance"""
        Student_data = self.__dict__

        return {key: value for key, value in Student_data.items()
                if attrs is None or key in attrs}

    def reload_from_json(self, json):
        """method that replaces all attributes of the Student instance
        """
        Student_data = {}
        for key, value in json.items():
            Student_data.update({key: value})
            self.__dict__ = Student_data
