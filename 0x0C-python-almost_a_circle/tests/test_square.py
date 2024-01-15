#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_id(self):
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

    def test_square_exception(self):
        with self.assertRaises(TypeError):
            s1 = Square()
            s1 = Square(1, 2, 3, 4, 5, 6)
            s1 = Square("1", 3)
            s1 = Square(1, "3")
            s1 = Square(1, 4, "2")
            s1 = Square(1, 4, 2, "5")
            s1 = Square([2, 3, 4],5, 5, 3)
            s1 = Square({"Name": 4}, 5)
            s1 = Square(3, True, 3, 2)
            s1 = Square(3, 1, 3, False)
            s1 = Square(4, 3, (3, 3), 1)
        
        with self.assertRaises(ValueError):
            s1 = Square(-6, 3)
            s1 = Square(1, -3)
            s1 = Square(-2, -1)
            s1 = Square(0, 0)
            s1 = Square(1, 0)
            s1 = Square(0, 1)
            s1 = Square(3, 1, -1, 3)
            s1 = Square(3, 0, -1, 3)
            s1 = Square(3, 1, 1, -3)
            s1 = Square(0, 1, 1, -3)

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaises(TypeError):
            s1.size = '5'
        with self.assertRaises(TypeError):
            s1 = Square('4')
        with self.assertRaises(ValueError):
            s1 = Square(-3)
            s1.size = 0
            s1.size = -32

    def test_update(self):
        s1 = Square(10, 10, 10, 10)

        s1.update(height=1)
        self.assertEqual(s1.height, 1)

        s1.update(width=1, x=2)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.x, 2)

        s1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.id, 89)

        s1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.height, 2)

        with self.assertRaises(ValueError):
            s1.update(width=-3, height=3)
            s1.update(height=-3, width=3)
            s1.update(height=3, width=3, x=-3)
            s1.update(height=3, width=3,x=4, y=-3)
            s1.update(height=3, width=0,x=4, y=3)
            s1.update(height=0, width=3,x=4, y=3)
        
        with self.assertRaises(TypeError):
            s1.update(width=3, height="3")
            s1.update(height=3, width=[0, 4, 5])
            s1.update(height=3, width=3, x=True)
            s1.update(height=3, width=3,x=4, y=False)
            s1.update(height=3, width={"3": 3},x=4, y=3)
            s1.update(height="String", width=3,x=4, y=3)

if __name__ == "__main__":
    unittest.main()