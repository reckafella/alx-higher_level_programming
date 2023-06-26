#!/usr/bin/python3
""" Module to test Square class """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from  models.base import Base


class TestSquare(unittest.TestCase):
    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_is_subclass(self):
        self.assertTrue(issubclass(Square, Rectangle))
    
    def test_module_docs(self):
        import models.square as square
        self.assertTrue(len(square.__doc__) > 1)

    def test_class_docs(self):
        self.assertTrue(len(Square.__doc__) > 1)

    def test_init_docs(self):
        self.assertTrue(len(Square.__init__.__doc__) > 1)
    
    def test_errors_raised(self):
        with self.assertRaises(TypeError):
            Square('1')
            Square(1, '1', 0, 1)
            Square(1, 1, '1')
        with self.assertRaises(ValueError):
            Square(0)
            Square(1, -1, 1)
            Square(1, 1, -1)

    def test_accessing_priv_vars(self):
        with self.assertRaises(AttributeError):
            Square.__x
            Square.__y
            Square.__width
            Square.__height

    def test_str_docs(self):
        self.assertTrue(len(Square.__str__.__doc__) > 1)

    def test_str(self):
        expected = '[Square] (1) 0/0 - 2'
        s1 = Square(2)
        self.assertEqual(str(s1), expected)

    def test_update_docs(self):
        """ docs len """
        self.assertTrue(len(Square.update.__doc__) > 1)

    def test_update(self):
        """ Working with *args """
        r1 = Square(1, 2, 1, 1)
        self.assertEqual(str(r1), '[Square] (1) 2/1 - 1')
        r1.update(2, 10, 20, 0)
        self.assertEqual('[Square] (2) 20/0 - 10', str(r1))

        """ Working with **kwargs """
        r1.update(id=91, x=2, y=1, size=30)
        self.assertEqual(str(r1), '[Square] (91) 2/1 - 30')

        """ Working with *args and **kwargs """
        r1.update(3, 1, 2, id=91, x=2, y=1, size=90)
        self.assertEqual(str(r1), '[Square] (3) 2/1 - 1')

    def test_to_dict_docs(self):
        """ docs """
        self.assertTrue(len(Square.to_dictionary.__doc__) > 1)

    def test_to_dictionary(self):
        r1 = Square(2)
        r2 = r1.to_dictionary()
        expected = {'id': 1, 'size': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(expected, r2)

if __name__ == '__main__':
    unittest.main()