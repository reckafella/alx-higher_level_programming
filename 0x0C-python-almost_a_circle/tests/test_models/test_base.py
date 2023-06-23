#!/usr/bin/python3

""" Module to test Base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_none(self):
        first = Base()
        second = Base()
        third = Base()
        self.assertEqual(first.id, 1)
        self.assertEqual(second.id, 2)
        self.assertEqual(third.id, 3)

    def test_id_given(self):
        id_given = Base(12)
        self.assertEqual(id_given.id, 12)

    def test_private_variable_access(self):
        with self.assertRaises(AttributeError):
            __ = Base.__nb_objects

    def test_module_docs(self):
        self.assertTrue(len(Base.__doc__) > 1, True)

    def test_class_docs(self):
        self.assertTrue(len(Base.__class__.__doc__) > 1, True)

if __name__ == '__main__':
    unittest.main()
