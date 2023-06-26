#!/usr/bin/python3

""" Module to test Base class """

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import models.rectangle as rec
import os, shutil


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_none(self):
        base1, base2, base3 = Base(), Base(), Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_id_given(self):
        id_given = Base(12)
        self.assertEqual(id_given.id, 12)

    def test_private_variable_access(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_module_docs(self):
        import models.base as bs
        self.assertTrue(len(bs.__doc__) > 1, True)

    def test_class_docs(self):
        self.assertTrue(len(Base.__doc__) > 1, True)
    
    def test_to_json_string_docs(self):
        self.assertTrue(len(Base.to_json_string.__doc__) > 1, True)

    def test_to_json_string(self):
        list_dicts1 = None
        list_dicts2 = {}
        list_dict3 = {"id": 5, "size": 5, "x": 0, "y": 0}, {"id": 6, "size": 7, "x": 9, "y": 1}
        self.assertEqual(Base.to_json_string(list_dicts1), '[]')
        self.assertEqual(Base.to_json_string(list_dicts2), '[]')
        self.assertEqual(Base.to_json_string(list_dict3),
                         '[{"id": 5, "size": 5, "x": 0, "y": 0}, {"id": 6, "size": 7, "x": 9, "y": 1}]')

    def test_save_to_file_docs(self):
        self.assertTrue(len(Base.save_to_file.__doc__) > 1, True)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists('Rectangle.json'))

        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        self.assertTrue(os.path.exists('Square.json'))

    def test_from_json_string(self):
        json_string = '[\
            {"id": 5, "size": 5, "x": 0, "y": 0},\
            {"id": 6, "size": 7, "x": 9, "y": 1}]'
        expected_out = [
            {'id': 5, 'size': 5, 'x': 0, 'y': 0},
            {'id': 6, 'size': 7, 'x': 9, 'y': 1}]
        python_obj = Square.from_json_string(json_string)
        self.assertEqual(python_obj, expected_out)

        json_string1 = None
        json_string2 = []
        self.assertEqual(Square.from_json_string(json_string1), '[]')
        self.assertEqual(Square.from_json_string(json_string2), '[]')

    def test_create_docs(self):
        self.assertTrue(len(Base.create.__doc__) > 1, True)

    def test_create(self):
        sq = Square(1, 2)
        self.assertEqual(sq, sq.create(**sq.to_dictionary()))

        rect = rec.Rectangle(1, 1)
        self.assertEqual(rect, rect.create(**rect.to_dictionary()))

    def test_load_from_file_missing(self):
        shutil.copy("Rectangle.json", 'rect_copy.json')
        os.remove('Rectangle.json')
        self.assertEqual(
            Rectangle.load_from_file(), []
        )
        os.rename('rect_copy.json', 'Rectangle.json')

        shutil.copy("Square.json", 'sq_copy.json')
        os.remove('Square.json')
        self.assertEqual(
            Square.load_from_file(), []
        )
        os.rename('sq_copy.json', 'Square.json')

    def test_load_from_file(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertIsInstance(list_squares_output, list)

        for instance, square in zip(list_squares_input,list_squares_output):
            self.assertIsInstance(square, Square)
            self.assertEqual(instance.id, square.id)
            self.assertNotEqual(id(instance), id(square))

if __name__ == '__main__':
    unittest.main()
