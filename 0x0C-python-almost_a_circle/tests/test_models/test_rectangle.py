#!/usr/bin/python3

""" Module to test Rectangle class """

from io import StringIO
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_is_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))
    
    def test_module_docs(self):
        import models.rectangle as rect
        self.assertTrue(len(rect.__doc__) > 1)

    def test_class_docs(self):
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_init_docs(self):
        """ docs """
        self.assertTrue(len(Rectangle.__init__.__doc__) > 1)

    def test_errors_init_raised(self):
        with self.assertRaises(TypeError):
            Rectangle('10', 10)
            Rectangle('10', '10')
            Rectangle(10, '10')
            Rectangle(1, 2, '1', 1)
            Rectangle(1, 1, 1, '1')

        with self.assertRaises(ValueError):
            Rectangle(0, 10)
            Rectangle(-1, '10')
            Rectangle(10, 0)
            Rectangle(1, 1, -2, 1)
            Rectangle(1, 2, 2, -1)

    def test_accessing_priv_vars(self):
        with self.assertRaises(AttributeError):
            Rectangle.__x
            Rectangle.__y
            Rectangle.__width
            Rectangle.__height

    def test_area_docs(self):
        """ docs """
        self.assertTrue(len(Rectangle.area.__doc__) > 1)

    def test_area(self):
        r1 = Rectangle(10, 10)
        self.assertEqual(r1.area(), 100)
    
    def test_display_docs(self):
        """ docs """
        self.assertTrue(len(Rectangle.display.__doc__) > 1)

    def test_display(self):
        r1 = Rectangle(2, 2)
        expected_output = '##\n##\n'
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            r1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

        r2 = Rectangle(2, 2, 2, 1)
        expected_output2 = '\n  ##\n  ##\n'
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            r2.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output2)

    def test_str_docs(self):
        """ docs len """
        self.assertTrue(len(Rectangle.__str__.__doc__) > 1)

    def test_str(self):
        expected_output = '[Rectangle] (12) 2/1 - 2/2'
        instance = Rectangle(2, 2, 2, 1, 12)
        self.assertEqual(expected_output, str(instance))

    def test_update_docs(self):
        """ docs len """
        self.assertTrue(len(Rectangle.update.__doc__) > 1)

    def test_update(self):
        """ Working with *args """
        r1 = Rectangle(1, 1, 2, 1, 1)
        self.assertEqual(str(r1), '[Rectangle] (1) 2/1 - 1/1')
        r1.update(2, 10, 20, 0, 0)
        self.assertEqual('[Rectangle] (2) 0/0 - 10/20', str(r1))

        """ Working with **kwargs """
        r1.update(id=91, x=2, y=1, width=30, height=90)
        self.assertEqual(str(r1), '[Rectangle] (91) 2/1 - 30/90')

        """ Working with *args and **kwargs """
        r1.update(3, 1, 2, 1, 1, id=91, x=2, y=1, width=30, height=90)
        self.assertEqual(str(r1), '[Rectangle] (3) 1/1 - 1/2')
        r1.update(3, 1, 2, id=91, x=2, y=1, width=30, height=90)
        self.assertEqual(str(r1), '[Rectangle] (3) 1/1 - 1/2')

    def test_to_dict_docs(self):
        """ docs """
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 1)

    def test_to_dictionary(self):
        r1 = Rectangle(2, 2)
        r2 = r1.to_dictionary()
        expected = {'id': 1, 'height': 2, 'x': 0, 'width': 2, 'y': 0}
        self.assertDictEqual(expected, r2)

if __name__ == '__main__':
    unittest.main()
