#!/usr/bin/python3
"""Unittest base.
Test cases for Base class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_17_0' for the first test of task 17)
"""


import json
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for Base class."""

    def setUp(self):
        """ Runs for each test """

        Base._Base__nb_objects = 0

    def test_None_id(self):
        """Test base class without passing id"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_passing_id(self):
        """Test base class passing id"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(15)
        self.assertEqual(b2.id, 15)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(-3)
        self.assertEqual(b4.id, -3)
        b2.id = 6
        self.assertEqual(b2.id, 6)

    def test_types(self):
        """Check the type of id and objects"""
        b1 = Base()
        self.assertTrue(type(b1.id), int)
        self.assertTrue(type(b1), Base)
        self.assertTrue(type(Base), Base)

    def test_to_json_string(self):
        """Test json string"""

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        excepted_output = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, excepted_output)
        
        json_dictionary = Base.to_json_string([])
        excepted_output = '[]'
        self.assertEqual(json_dictionary, excepted_output)

        json_dictionary = Base.to_json_string(None)
        excepted_output = '[]'
        self.assertEqual(json_dictionary, excepted_output)

        with self.assertRaises(TypeError) as e:
            json_dictionary = Base.to_json_string()
        Err_msg = "Base.to_json_string() missing 1 required positional argument: 'list_dictionaries'"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            json_dictionary = Base.to_json_string([dictionary], [dictionary])
        Err_msg = "Base.to_json_string() takes 1 positional argument but 2 were given"
        self.assertEqual(Err_msg, str(e.exception))

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')

        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r') as file:
            content = file.read()
        excepted_output = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(content, excepted_output)

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        Err_msg = "Base.save_to_file() missing 1 required positional argument: 'list_objs'"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file(r1, r2)
        Err_msg = "Base.save_to_file() takes 2 positional arguments but 3 were given"
        self.assertEqual(Err_msg, str(e.exception))


if __name__ == "__main__":
    unittest.main()
