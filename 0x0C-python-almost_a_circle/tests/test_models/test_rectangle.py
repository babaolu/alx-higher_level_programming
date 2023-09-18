#!/usr/bin/python3
""" This implements tests for the Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Rectangle test implementation """

    def test_init(self):
        rect = Rectangle(3, 5)
        self.assertEqual(rect.area(), 15)
