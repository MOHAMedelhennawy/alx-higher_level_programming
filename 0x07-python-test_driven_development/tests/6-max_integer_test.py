#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test ordered list"""
        l = [1, 2, 3, 4]
        self.assertEqual(max_integer(l), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        l = [3, 1, 3, 7, 20, 12]
        self.assertEqual(max_integer(l), 20)

    def test_list_of_negativeNumbers(self):
        """Test for passing negative numbers"""
        l = [-1, -3, -4, -5, -6]
        self.assertEqual(max_integer(l), -1)

    def test_mix_of_numbers(self):
        """Test for mix of negative and positive numbers"""
        l = [-1, 3, -10, 40, 20, -14, 34, 12,
              21, 42, -12, -11, -110, 100]
        self.assertEqual(max_integer(l), 100)

    def test_one_index(self):
        """Test for passing list of one index"""
        l = [9]
        self.assertEqual(max_integer(l), 9)

    def test_indexes_TheSameValue(self):
        """Test for passing list of many indexes with the same value"""
        l = [9, 9, 9, 9, 9, 9, 9, 9]
        self.assertEqual(max_integer(l), 9)

    def test_empty_list(self):
        """Test for passign empty list"""
        l = []
        self.assertEqual(max_integer(l), None)

    def test_list_of_String(self):
        """Test for passing a string and numbers"""
        l = ["list","String", "lol"]
        self.assertEqual(max_integer(l), "lol")

    def test_list_of_String_And_Numbers(self):
        """Test for passing a string and numbers"""
        l = ["list", 5, 3, 1, "String", "lol", -2]


    def test_string(self):
        """Test for passing a string"""
        l = "This is string"
        self.assertEqual(max_integer(l), "t")


    def test_list_Of_list(self):
        """Test for passing a list of list"""
        l = [[]]
        self.assertEqual(max_integer(l), [])

    def test_BigNumbers(self):
        """Test for passing big numbers"""
        l = [4444444412, 1212222222, 1, 444444444444444,
              0, 00000, 3232323, 1000000000000000]
        self.assertEqual(max_integer(l), 1000000000000000)

    def test_floatNumbers(self):
        """Test for passing a list of float numbers"""
        l = [3.2, 1.2, 5.7, 7.3]
        self.assertEqual(max_integer(l), 7.3)

    def test_float_And_inegers(self):
        """Test for passing mix of float and integer"""
        l = [2.2, 3, 41.4, 1, 0, 9, 14.2]
        self.assertEqual(max_integer(l), 41.4)
