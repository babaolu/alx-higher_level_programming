#!/usr/bin/python3
""" This implements tests for the Base class """
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Base test implementation """

    count = 0

    @classmethod
    def setUpClass(cls):
        TestBaseClass.count = Base.nb_objects()

    def test_noarg(self):
        """ Test without arguments """
        b = None
        for i in range(4):
            b = Base()
        self.assertEqual(b.id, TestBaseClass.count + 4)

    def test_withargs(self):
        """ Testing with arguments """
        b = Base(33)
        self.assertEqual(b.id, 33)
