import unittest


from src.ShapeFactory import ShapeFactory


class ShapeTests(unittest.TestCase):
    """
    This class tests functionality Shape class.
    """
    def test_circle_area(self):
        """Test created circle area should be as expected"""
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        self.assertEqual(3.141592653589793, circle_one.area())


    def test_circle_perimeter(self):
        """Test created circle perimeter should be as expected"""
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        self.assertEqual(6.283185307179586, circle_one.perimeter())

    def test_rectangle_area(self):
        """Test created rectangle area should be as expected"""
        rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
        self.assertEqual(6.0, rectangle_one.area())

    def test_rectangle_perimeter(self):
        """Test created rectangle perimeter should be as expected"""
        rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
        self.assertEqual(10.0, rectangle_one.perimeter())

    def test_square_area(self):
        """Test created square area should be as expected"""
        square_one = ShapeFactory.create_shape("Square", 3.0)
        self.assertEqual(9.0, square_one.area())

    def test_square_perimeter(self):
        """Test created square perimeter should be as expected"""
        square_one = ShapeFactory.create_shape("Square", 3.0)
        self.assertEqual(12.0, square_one.perimeter())

    def test_triangle_area(self):
        """Test created triangle area should be as expected"""
        triangle_one = ShapeFactory.create_shape("Triangle", 3.0, 4.0, 5.0)
        self.assertEqual(6.0, triangle_one.area())

    def test_triangle_perimeter(self):
        """Test created triangle perimeter should be as expected"""
        triangle_one = ShapeFactory.create_shape("Triangle", 3.0, 4.0, 5.0)
        self.assertEqual(12.0, triangle_one.perimeter())

    def test_get_name_property(self):
        """Test created shape get name property perimeter should be as expected"""
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        self.assertEqual("Circle", circle_one.name)