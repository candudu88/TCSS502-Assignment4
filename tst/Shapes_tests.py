import unittest


from src.Shape import Shape
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class ShapeTests(unittest.TestCase):
    """
    This class tests functionality Shape class.
    """
    def test_circle_area(self):
        """Test created circle area should be as expected"""
        circle_one = Circle(1.0)
        self.assertEqual(3.141592653589793, circle_one.area(), "expected area of 3.141592653589793")

    def test_circle_area_given_valid_ints(self):
        """Test area method of circle by passing int as parameter"""
        circle_one = Circle(1)
        self.assertEqual(3.141592653589793, circle_one.area(), "expected area of 3.141592653589793")

    def test_circle_area_given_valid_strings(self):
        """Test area method of circle by passing string as parameter"""
        circle_one = Circle("1.0")
        self.assertEqual(3.141592653589793, circle_one.area(), "expected area of 3.141592653589793")

    def test_circle_perimeter(self):
        """Test created circle perimeter should be as expected"""
        circle_one = Circle(1.0)
        self.assertEqual(6.283185307179586, circle_one.perimeter(), "expected perimeter of 6.283185307179586")

    def test_circle_perimeter_given_valid_ints(self):
        """Test perimeter method of circle by passing in int parameters"""
        rectangle_one = Rectangle(2, 3)
        self.assertEqual(10.0, rectangle_one.perimeter(), "expected perimeter of 10.0")

    def test_circle_perimeter_given_valid_strings(self):
        """Test perimeter method of circle by passing string as parameter"""
        rectangle_one = Rectangle("2.0", "3.0")
        self.assertEqual(10.0, rectangle_one.perimeter(), "expected perimeter of 10.0")

    def test_circle_property_name(self):
        """Tests get name of circle"""
        circle_one = Circle(1.0)
        self.assertEqual("Circle", circle_one.name, "name should be \"Circle\"")

    def test_circle_str(self):
        """Tests __str__ method should return shape info with proper format"""
        circle_one = Circle(1.0)
        expected_str = "Circle, area: 3.141592653589793, perimeter: 6.283185307179586"
        self.assertEqual(expected_str, str(circle_one), f"str of circle should be \"{expected_str}\"")

    def test_circle_eq(self):
        """Tests __eq__ method should check if two circles are equal"""
        circle_one = Circle(1.0)
        circle_two = Circle(1.0)
        self.assertEqual(circle_one, circle_two, "circles should be equal")

    def test_circle_lt(self):
        """Tests __lt__ method should check if circle is less another circle"""
        circle_one = Circle(1.0)
        circle_two = Circle(2.0)
        self.assertLess(circle_one, circle_two, "circle_one should be less than circle_two")

    def test_create_circle_with_invalid_arguments(self):
        """Test create circle by passing incorrect number of arguments"""
        try:
            Circle(1.0, 2.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_rectangle_area(self):
        """Test created rectangle area should be as expected"""
        rectangle_one = Rectangle(2.0, 3.0)
        self.assertEqual(6.0, rectangle_one.area(), "expected area of 6.0")

    def test_rectangle_area_given_valid_ints(self):
        """Test area method of rectangle by passing in int parameters"""
        rectangle_one = Rectangle(2, 3)
        self.assertEqual(6.0, rectangle_one.area(), "expected area of 6.0")

    def test_rectangle_area_given_valid_strings(self):
        """Test area method of rectangle by passing string as parameter"""
        rectangle_one = Rectangle("2.0", "3.0")
        self.assertEqual(6.0, rectangle_one.area(), "expected area of 6.0")

    def test_rectangle_perimeter(self):
        """Test created rectangle perimeter should be as expected"""
        rectangle_one = Rectangle(2.0, 3.0)
        self.assertEqual(10.0, rectangle_one.perimeter(), "expected perimeter of 10.0")

    def test_rectangle_perimeter_given_valid_ints(self):
        """Test perimeter method of rectangle by passing in int parameters"""
        rectangle_one = Rectangle(2, 3)
        self.assertEqual(10.0, rectangle_one.perimeter(), "expected perimeter of 10.0")

    def test_rectangle_perimeter_given_valid_strings(self):
        """Test perimeter method of rectangle by passing string as parameter"""
        rectangle_one = Rectangle("2.0", "3.0")
        self.assertEqual(10.0, rectangle_one.perimeter(), "expected perimeter of 10.0")

    def test_rectangle_property_name(self):
        """Tests get name of rectangle"""
        rectangle_one = Rectangle(2.0, 3.0)
        self.assertEqual("Rectangle", rectangle_one.name, "name should be \"Rectangle\"")

    def test_rectangle_str(self):
        """Tests __str__ method should return shape info with proper format"""
        rectangle_one = Rectangle(2.0, 3.0)
        expected_str = "Rectangle, area: 6.0, perimeter: 10.0"
        self.assertEqual(expected_str, str(rectangle_one), f"str of rectangle should be \"{expected_str}\"")

    def test_rectangle_eq(self):
        """Tests __eq__ method should check if two rectangles are equal"""
        rectangle_one = Rectangle(2.0, 3.0)
        rectangle_two = Rectangle(2.0, 3.0)
        self.assertEqual(rectangle_one, rectangle_two, "rectangles should be equal")

    def test_rectangle_lt(self):
        """Tests __lt__ method should check if rectangle is less another rectangle"""
        rectangle_one = Rectangle(1.0, 1.0)
        rectangle_two = Rectangle(2.0, 3.0)
        self.assertLess(rectangle_one, rectangle_two, "rectangle_one should be less rectangle_two")

    def test_create_rectangle_with_invalid_arguments(self):
        """Test create rectangle by passing incorrect number of arguments"""
        try:
            Rectangle(1.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_square_area(self):
        """Test created square area should be as expected"""
        square_one = Square(3.0)
        self.assertEqual(9.0, square_one.area(), "expected area of 9.0")

    def test_square_area_given_valid_ints(self):
        """Test area method of square by passing in int parameters"""
        square_one = Square(3)
        self.assertEqual(9.0, square_one.area(), "expected area of 9.0")

    def test_square_area_given_valid_strings(self):
        """Test area method of square by passing string as parameter"""
        square_one = Square("3.0")
        self.assertEqual(9.0, square_one.area(), "expected area of 9.0")

    def test_square_perimeter(self):
        """Test created square perimeter should be as expected"""
        square_one = Square(3.0)
        self.assertEqual(12.0, square_one.perimeter(), "expected perimeter of 12.0")

    def test_square_perimeter_given_valid_ints(self):
        """Test perimeter method of square by passing in int parameters"""
        square_one = Square(3)
        self.assertEqual(12.0, square_one.perimeter(), "expected perimeter of 12.0")

    def test_square_perimeter_given_valid_strings(self):
        """Test perimeter method of circle by passing string as parameter"""
        square_one = Square("3")
        self.assertEqual(12.0, square_one.perimeter(), "expected perimeter of 12.0")

    def test_square_property_name(self):
        """Tests get name of square"""
        square_one = Square(3.0)
        self.assertEqual("Square", square_one.name, "name should be \"Square\"")

    def test_square_str(self):
        """Tests __str__ method should return shape info with proper format"""
        square_one = Square(3.0)
        expected_str = "Square, area: 9.0, perimeter: 12.0"
        self.assertEqual(expected_str, str(square_one), f"str of square should be \"{expected_str}\"")

    def test_square_eq(self):
        """Tests __eq__ method should check if two circles are equal"""
        square_one = Square(3.0)
        square_two = Square(3.0)
        self.assertEqual(square_one, square_two, "squares should be equal")

    def test_square_lt(self):
        """Tests __lt__ method should check if square is less another square"""
        square_one = Square(3.0)
        square_two = Square(4.0)
        self.assertLess(square_one, square_two, "square_one should be less than square_two")

    def test_create_square_with_invalid_arguments(self):
        """Test create square by passing incorrect number of arguments"""
        try:
            Square(1.0, 3.0, 4.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_triangle_area(self):
        """Test created triangle area should be as expected"""
        triangle_one = Triangle(3.0, 4.0, 5.0)
        self.assertEqual(6.0, triangle_one.area(), "expected area of 6.0")

    def test_triangle_area_given_valid_ints(self):
        """Test area method of triangle by passing in int parameters"""
        triangle_one = Triangle(3, 4, 5)
        self.assertEqual(6.0, triangle_one.area(), "expected area of 6.0")

    def test_triangle_area_given_valid_strings(self):
        """Test perimeter method of triangle by passing string as parameter"""
        triangle_one = Triangle("3", "4", "5")
        self.assertEqual(6.0, triangle_one.area(), "expected area of 6.0")

    def test_triangle_perimeter(self):
        """Test created triangle perimeter should be as expected"""
        triangle_one = Triangle(3.0, 4.0, 5.0)
        self.assertEqual(12.0, triangle_one.perimeter(), "expected perimeter of 12.0")

    def test_triangle_perimeter_given_valid_ints(self):
        """Test perimeter method of triangle by passing in int parameters"""
        triangle_one = Triangle(3, 4, 5)
        self.assertEqual(12.0, triangle_one.perimeter(), "expected perimeter of 12.0")

    def test_triangle_perimeter_given_valid_strings(self):
        """Test perimeter method of triangle by passing in strings parameters"""
        triangle_one = Triangle("3", "4", "5")
        self.assertEqual(12.0, triangle_one.perimeter(), "expected perimeter of 12.0")

    def test_triangle_property_name(self):
        """Tests get name of triangle"""
        triangle_one = Triangle(3.0, 4.0, 5.0)
        self.assertEqual("Triangle", triangle_one.name, "name should be \"Triangle\"")

    def test_triangle_str(self):
        """Tests __str__ method should return shape info with proper format"""
        triangle_one = Triangle(3.0, 4.0, 5.0)
        expected_str = "Triangle, area: 6.0, perimeter: 12.0"
        self.assertEqual(expected_str, str(triangle_one), f"str of triangle should be \"{expected_str}\"")

    def test_triangle_eq(self):
        """Tests __eq__ method should check if two circles are equal"""
        triangle_one = Triangle(1.0, 1.0, 1.0)
        triangle_two = Triangle(1.0, 1.0, 1.0)
        self.assertEqual(triangle_one, triangle_two, "triangles should be equal")

    def test_triangle_lt(self):
        """Tests __lt__ method should check if triangle is less another triangle"""
        triangle_one = Triangle(1.0, 1.0, 1.0)
        triangle_two = Triangle(3.0, 4.0, 5.0)
        self.assertLess(triangle_one, triangle_two, "triangle_one should be less than triangle_two")

    def test_create_triangle_with_invalid_arguments(self):
        """Test create triangle by passing incorrect number of arguments"""
        try:
            Triangle(1.0)
            self.assertEqual(True, False, "exception not thrown for not wrong number of arguments")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_given_sides_form_triangle(self):
        """Tests creates shape with sides that can not form a triangle"""
        try:
            Triangle(1.0, 4.0, 5.0)
            self.assertEqual(True, False, "exception not thrown for creating triangle with sides that can't form a triangle")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_shape(self):
        """Tests if create Shape produces an error"""
        try:
            shape = Shape("Shape")
            self.assertEqual(True, False, "exception not thrown for creating Shape instance")
        except TypeError as type_error:
            self.assertEqual(True, True)