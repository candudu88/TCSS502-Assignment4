import unittest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.ShapeFactory import ShapeFactory
from src.Square import Square
from src.Triangle import Triangle


class ShapeFactoryTests(unittest.TestCase):
    """
    This class tests functionality ShapeFactory class.
    """
    def test_create_circle_with_valid_argument(self):
        """Test created circle with valid argument should succeed"""
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        self.assertTrue(isinstance(circle_one, Circle))

    def test_create_circle_with_invalid_argument(self):
        """Test created circle with invalid argument should raise TypeError exception"""
        try:
            ShapeFactory.create_shape("Circle", 1.0, 2.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_square_with_valid_argument(self):
        """Test created square with valid argument should succeed"""
        square_one = ShapeFactory.create_shape("Square", 2.0)
        self.assertTrue(isinstance(square_one, Square))

    def test_create_square_with_invalid_argument(self):
        """Test created square with invalid argument should raise TypeError exception"""
        try:
            ShapeFactory.create_shape("Square", 1.0, 2.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_rectangle_with_valid_argument(self):
        """Test created rectangle with valid argument should succeed"""
        rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
        self.assertTrue(isinstance(rectangle_one, Rectangle))

    def test_create_rectangle_with_invalid_argument(self):
        """Test created rectangle with invalid argument should raise TypeError exception"""
        try:
            ShapeFactory.create_shape("Rectangle", 1.0, 2.0, 3.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)


    def test_create_triangle_with_valid_argument(self):
        """Test created triangle with valid argument should succeed"""
        triangle_one = ShapeFactory.create_shape("Triangle", 3.0, 4.0, 5.0)
        self.assertTrue(isinstance(triangle_one, Triangle))

    def test_create_triangle_with_invalid_argument(self):
        """Test created triangle with invalid argument should raise TypeError exception"""
        try:
            ShapeFactory.create_shape("Triangle", 1.0, 2.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_other_non_support_shape(self):
        """Test created non-supported shape types should raise ValueError exception"""
        try:
            ShapeFactory.create_shape("Oval", 3.0)
            self.assertEqual(True, False, "exception not thrown for not support shape")
        except ValueError as value_error:
            self.assertEqual(True, True)