#!/usr/bin/python3
"""Module base.
Defines a Base class for other classes in the project.
"""

import json
import os
import csv


class Base:
    """Class with:
    Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance.

        Args:
            - id: id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries.

        Args:
            - list_dictionaries: list of dicts

        Returns: JSON representation of the list
        """

        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file.

        Args:
            - list_objs: list of instances who inherits of Base
        """

        list_data = (
            cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            )
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file_obj:
            if list_objs is None or list_objs == []:
                file_obj.write([])
            else:
                file_obj.write(list_data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            - json_string: string to convert to list
        """

        return (
            json.loads(json_string) if json_string and json_string.strip()
            else []
            )

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            - dictionary: used as **kwargs

        Returns: instance created   
        """

        dummy = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        lis = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    lis.append(cls.create(**d))
        return lis

    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = cls.__name__ + ".csv"


        with open(file_name, "w") as file_obj:
            data = csv.writer(file_obj, delimiter=",")
        
            for obj in list_objs:
                data.writerow(obj.to_dictionary())