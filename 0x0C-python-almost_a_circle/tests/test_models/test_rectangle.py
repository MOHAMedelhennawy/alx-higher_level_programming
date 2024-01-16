#!/usr/bin/python3
"""Unittest rectangle
Test cases for the Rectangle class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_17_0' for the first test of task 17)
"""


from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """ Runs for each test """

        Base._Base__nb_objects = 0

    def test_rectangle_id(self):
        """Test Rectangle id"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertTrue(type(r1.id), int)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertTrue(type(r2.id), int)

        r3 = Rectangle(210, 23, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertTrue(type(r3.id), int)

        r4 = Rectangle(10, 2, 0, 0, -2)
        self.assertEqual(r4.id, -2)
        self.assertTrue(type(r4.id), int)

        r5 = Rectangle(11, 44)
        self.assertEqual(r5.id, 3)
        self.assertTrue(type(r5.id), int)

    def test_rectangle_attributes(self):
        """Test Rectangle attribute values"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(3, 4, 1, 2)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(6, 2, 7, 0, -5)
        self.assertEqual(r3.width, 6)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 7)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, -5)

        r4 = Rectangle(3, 1, 0, 5)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 1)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 5)
        self.assertEqual(r4.id, 3)

    def test_Rectangle_TypeError_Exception(self):
        """Test TypeError exception mgs of Rectangle attributes"""

        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(5)
        self.assertEqual(
            "Rectangle.__init__() missing 1 required " +
            "positional argument: 'height'", str(
                e.exception))
        s = ("Rectangle.__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as e:
            r2 = Rectangle()
        self.assertEqual(s, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r3 = Rectangle("1", 3)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, "3")
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r5 = Rectangle(1, 4, "2")
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r6 = Rectangle(1, 4, 2, "5")
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r7 = Rectangle([2, 3, 4], 5, 5, 3)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r8 = Rectangle({"Name": 4}, 5)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r9 = Rectangle(3, "True", 3, 2)
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r11 = Rectangle(4, 3, (3, 3), 1)
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

    def test_Rectangle_ValueError_Exception(self):
        """Test ValueError exception mgs of Rectangle attributes"""

        with self.assertRaises(ValueError) as e:
            r12 = Rectangle(-6, 3)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r13 = Rectangle(1, -3)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r14 = Rectangle(-2, -1)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r15 = Rectangle(0, 0)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r16 = Rectangle(1, 0)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r17 = Rectangle(3, 1, -1, 3)
        Err_msg = "x must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r18 = Rectangle(3, 1, 1, -3)
        Err_msg = "y must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

    def test_rectangle_area(self):
        "Test returned area value of Rectangle"

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_update(self):
        """Test update without passing args"""

        r1 = Rectangle(10, 10, 10, 10)
        result = str(r1)
        expected_output = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(result, expected_output)

        r1.update(89)
        result = str(r1)
        expected_output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(result, expected_output)

        r1.update(89, 2)
        result = str(r1)
        expected_output = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(result, expected_output)

        r1.update(89, 2, 3, 4, 5)
        result = str(r1)
        expected_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(result, expected_output)

    def test_update_with_Args(self):
        """Test update with args"""

        r1 = Rectangle(10, 10, 10, 10)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)

    def test_Update_VlaueError_Exception(self):
        """Test update ValueError exception msg of update method"""

        r1 = Rectangle(10, 10, 10, 10)

        with self.assertRaises(ValueError) as e:
            r1.update(width=-3, height=3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(height=-3, width=3)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(height=3, width=3, x=-3)
        Err_msg = "x must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(height=3, width=3, x=4, y=-3)
        Err_msg = "y must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(height=3, width=0, x=4, y=3)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(height=0, width=3, x=4, y=3)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(1, -4)
        Err_msg = "width must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(1, 4, 0)
        Err_msg = "height must be > 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(1, 4, 2, -3)
        Err_msg = "x must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(ValueError) as e:
            r1.update(1, 4, 2, 0, -3)
        Err_msg = "y must be >= 0"
        self.assertEqual(Err_msg, str(e.exception))

    def test_Update_TypeError_Exception(self):
        """Test TypeError Exception msg of update method"""

        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r1.update(width=3, height="3")
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(height=3, width=[0, 4, 5])
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(height=3, width=3, x="True")
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(height=3, width=3, x=4, y="False")
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(height=3, width={"3": 3}, x=4, y=3)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(height="String", width=3, x=4, y=3)
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(3, 3, "5")
        Err_msg = "height must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(3, "3", 5, 6)
        Err_msg = "width must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(3, 4, 5, "6", 0)
        Err_msg = "x must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(3, 4, 5, 2, "0")
        Err_msg = "y must be an integer"
        self.assertEqual(Err_msg, str(e.exception))

    def test_str_(self):
        """Test the str representation of rectangle class"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        result = str(r1)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(result, expected_output)

        r2 = Rectangle(5, 5, 1)
        result = str(r2)
        expected_output = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(result, expected_output)

        r3 = Rectangle(5, 2, 1, 3)
        result = str(r3)
        expected_output = "[Rectangle] (2) 1/3 - 5/2"
        self.assertEqual(result, expected_output)

        r4 = Rectangle(8, 7)
        result = str(r4)
        expected_output = "[Rectangle] (3) 0/0 - 8/7"
        self.assertEqual(result, expected_output)

        r1.update(y=1, width=2, x=3, id=89)
        result = str(r1)
        expected_output = "[Rectangle] (89) 3/1 - 2/6"
        self.assertEqual(result, expected_output)

        r1.update(x=1, height=2, y=3, width=4)
        result = str(r1)
        expected_output = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(result, expected_output)

    def test_to_dictionary(self):
        """Test returned the dictionary representation of a Rectangle"""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        excepted_output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, excepted_output)
        self.assertEqual(type(excepted_output), dict)

        r1.update(height=13, id=4, x=5, y=7, width=10)
        r1_dictionary = r1.to_dictionary()
        excepted_output = {'x': 5, 'y': 7, 'id': 4, 'height': 13, 'width': 10}
        self.assertEqual(r1_dictionary, excepted_output)
        self.assertEqual(type(excepted_output), dict)


if __name__ == "__main__":
    unittest.main()
