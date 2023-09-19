#!/usr/bin/python3
""" This implements tests for the Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Rectangle test implementation """

    def test_init(self):
        rect = Rectangle(3, 5)
        self.assertEqual(rect.area(), 15)
        self.assertRaises(TypeError, Rectangle, "4", 5)
        self.assertRaises(TypeError, Rectangle, 4, "5")
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_create(self):
        self.assertNotEqual(Rectangle.create(width=1, height=3).__dict__,
                            Rectangle(1, 3).__dict__)
