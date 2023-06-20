#!/usr/bin/python3

""" Module to test Base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_none(self):
        id_none = Base()
        self.assertEqual(id_none.id, 1)

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
