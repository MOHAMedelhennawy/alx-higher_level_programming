#!/usr/bin/python3
"""Unittest rectangle
Test cases for the Rectangle class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_17_0' for the first test of task 17)
...
"""


from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """ Runs for each test """

        Base._Base__nb_objects = 0

    def test_square_id(self):
        """Test id of square"""

        s1 = Rectangle(10, 2)
        self.assertEqual(s1.id, 1)
        self.assertTrue(type(s1.id), int)

        s2 = Rectangle(2, 10)
        self.assertEqual(s2.id, 2)
        self.assertTrue(type(s2.id), int)

        s3 = Rectangle(210, 23, 0, 0, 12)
        self.assertEqual(s3.id, 12)
        self.assertTrue(type(s3.id), int)

        s4 = Rectangle(10, 2, 0, 0, -2)
        self.assertEqual(s4.id, -2)
        self.assertTrue(type(s4.id), int)

        s5 = Rectangle(11, 44)
        self.assertEqual(s5.id, 3)
        self.assertTrue(type(s5.id), int)

    def test_square_attibute(self):
        """Test square attributes"""

        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 2)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 3)

        s4 = Square(2, 6, 2, 10)
        self.assertEqual(s4.size, 2)
        self.assertEqual(s4.x, 6)
        self.assertEqual(s4.y, 2)
        self.assertEqual(s4.id, 10)

    def test_square_TypeError_exception(self):
        """Test attribute TypeError exception of square"""

        with self.assertRaises(TypeError) as e:
            s1 = Square()
        Err_msg = (
            "Square.__init__() missing 1 required positional"
            +
            " argument: 'size'"
            )
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, 3, 4, 5, 6)
        Err_msg = (
            "Square.__init__() takes from 2 to 5"
            +
            " positional arguments but 7 were given"
            )
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square("1", 3)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square(1, "3")
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 4, "2")
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square([2, 3, 4], 5, 5, 3)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square({"Name": 4}, 5)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square(4, 3, (3, 3), 1)
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

    def test_square_ValueError_exception(self):
        """Test attribute ValueError exception of square"""

        with self.assertRaises(ValueError) as e:
            s1 = Square(-6, 3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -3)
        Err_msg = "x must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1 = Square(0, 0)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1 = Square(3, 1, -1)
        Err_msg = "y must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

    def test_size(self):
        """Test size attribute of square"""

        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_size_TypeError_exception(self):
        """Test TypeError exception of size attribute"""
        s1 = Square(5)

        with self.assertRaises(TypeError) as e:
            s1.size = '5'
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1 = Square('4')
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

    def test_size_ValueError_exception(self):
        """Test TypeError ValueError of size attribute"""

        s1 = Square(5)
        with self.assertRaises(ValueError) as e:
            s1 = Square(-3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))
        with self.assertRaises(ValueError) as e:
            s1.size = 0
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))
        with self.assertRaises(ValueError) as e:
            s1.size = -32
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

    def test_update(self):
        """Test update method on Square."""

        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test_Update_TypeError_Exception(self):
        """Test TypeError Exception msg of update method"""

        s1 = Square(10, 10, 10)
        with self.assertRaises(TypeError) as e:
            s1.update(width=3, height="3")
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(height=3, width=[0, 4, 5])
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(height=3, width=3, x="True")
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(height=3, width=3, x=4, y="False")
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(height=3, width={"3": 3}, x=4, y=3)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(height="String", width=3, x=4, y=3)
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(3, 3, "5")
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(3, "3", 5, 6)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            s1.update(3, 4, 5, "6", 0)
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

    def test_Update_VlaueError_Exception(self):
        """Test update ValueError exception msg of update method"""

        s1 = Square(10, 10, 10, 10)

        with self.assertRaises(ValueError) as e:
            s1.update(width=-3, height=3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(height=-3, width=3)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(height=3, width=3, x=-3)
        Err_msg = "x must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(height=3, width=3, x=4, y=-3)
        Err_msg = "y must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(size=0, x=4, y=3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(size=-1, x=4, y=3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(height=0, width=3, x=4, y=3)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(1, -4)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            s1.update(1, 4, 2, -3)
        Err_msg = "y must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

    def test_str_(self):
        """Test the str representation"""

        s1 = Square(5)
        result = str(s1)
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(result, expected_output)

        s1.size = 10
        result = str(s1)
        expected_output = "[Square] (1) 0/0 - 10"
        self.assertEqual(result, expected_output)

        with self.assertRaises(TypeError) as e:
            s1.size = "10"
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))
        
        with self.assertRaises(ValueError) as e:
            s1.size = -2
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

    def test_to_dictionary(self):
        """Test returned the dictionary representation """

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        excepted_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, excepted_output)
        self.assertEqual(type(excepted_output), dict)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        excepted_output = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s2_dictionary, excepted_output)
        self.assertEqual(type(excepted_output), dict)


if __name__ == "__main__":
    unittest.main()
