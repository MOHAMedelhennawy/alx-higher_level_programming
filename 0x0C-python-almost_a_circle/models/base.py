#!/usr/bin/python3
import json
import os

class Base:

    __nb_objects = 0
    def __init__(self, id=None):
        self.id = None

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        list_data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])   
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file_obj:
            file_obj.write(list_data)
    
    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string and json_string.strip() else []
    

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        l = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l