#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntTest(unittest.TestCase):
    """ Test Class """
    def test_max_integer(self):
        self.assertEqual(max_integer([34, 8, 12, 4]), 34)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("this"), "t")
        self.assertEqual(max_integer((3,7, 12, 5)), 12)
        self.assertRaises(TypeError, max_integer, {45, 6, 211, 5})
        self.assertRaises(TypeError, max_integer, 3)
