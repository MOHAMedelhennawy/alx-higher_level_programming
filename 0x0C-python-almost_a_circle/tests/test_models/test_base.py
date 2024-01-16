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
Base = __import__('models.base', globals(), locals(), ['Base'], 0).Base
Rectangle = __import__('models.rectangle', globals(), locals(), ['Rectangle'], 0).Rectangle
Square = __import__('models.square', globals(), locals(), ['Square'], 0).Square


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


if __name__ == "__main__":
    unittest.main()
