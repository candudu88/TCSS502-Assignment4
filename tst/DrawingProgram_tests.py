import unittest
from _ctypes_test import func
from unittest.mock import patch

from src.DrawingProgram import DrawingProgram
from src.ShapeFactory import ShapeFactory


class DrawingProgramTests(unittest.TestCase):
    """
    This class tests a great deal of the functionality provided by the DrawingProgram class.
    """

    def test_init_default_list(self):
        """Tests to see the default list is empty"""
        drawing_program = DrawingProgram()
        self.assertEqual([], drawing_program.list_of_shapes, "default list not set to empty list")

    def test_init_with_shape_list(self):
        """Tests to see the shape list is set to input list"""
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        circle_two = ShapeFactory.create_shape("Circle", 3.0)
        circle_three = ShapeFactory.create_shape("Circle", 1.0)
        shape_list = [circle_one, circle_two, circle_three]
        drawing_program = DrawingProgram(shape_list)
        self.assertEqual(shape_list, drawing_program.list_of_shapes, "shape list not set to input list")

    def test_add_shape_to_list(self):
        """Tests add valid shape to list should succeed"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        drawing_program.add_shape(circle_one)
        self.assertEqual(1, drawing_program._size, "list size not as expected after added one shape to it")

    def test_add_wrong_type_to_list(self):
        """Tests add invalid shape to list should raise TypeError exception"""
        drawing_program = DrawingProgram()
        try:
            drawing_program.add_shape("circle_test_string")
            self.assertEqual(True, False, "exception not thrown for add wrong type")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_remove_shape_from_list(self):
        """Tests remove shape that match input valid type from list and return correct count of removed item"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        circle_two = ShapeFactory.create_shape("Circle", 3.0)
        square_one = ShapeFactory.create_shape("Square", 3.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        drawing_program.add_shape(square_one)
        self.assertEqual(2, drawing_program.remove_shape(circle_two),
                         "removed size not as expected after remove shape from list")

    def test_remove_wrong_type_from_list(self):
        """Tests remove shape with input wrong type from list should not remove any item"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        circle_two = ShapeFactory.create_shape("Circle", 3.0)
        square_one = ShapeFactory.create_shape("Square", 3.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        drawing_program.add_shape(square_one)
        self.assertEqual(0, drawing_program.remove_shape("circle_test_string"),
                         "removed size not as expected after remove shape from list")

    @patch('builtins.print')
    def test_print_shape_from_same_type(self, mock_print):
        """
        Tests print shape that match input valid type from list and mocked print method
        should call same times as how many shape type are matched
        """
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        circle_two = ShapeFactory.create_shape("Circle", 3.0)
        square_one = ShapeFactory.create_shape("Square", 3.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        drawing_program.add_shape(square_one)
        drawing_program.print_shape(circle_two)
        self.assertEqual(None, func())
        self.assertEqual(2, mock_print.call_count, "print call times not match as expected")

    def test_sort_shapes_for_empty_list(self):
        """Tests sort shapes for empty list"""
        drawing_program = DrawingProgram()
        drawing_program.sort_shapes()
        self.assertEqual([], drawing_program.list_of_shapes, "empty list shape after sort not as remain empty")

    def test_sort_shapes_for_1_shape(self):
        """Tests sort shapes for only one shape and list should remain the same"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0, )
        drawing_program.add_shape(circle_one)
        drawing_program.sort_shapes()
        expect_list = [circle_one]
        self.assertEqual(expect_list, drawing_program.list_of_shapes, "one shape list after sort not as remain the order")

    def test_sort_shapes_for_multiple_ascending_shapes(self):
        """Tests sort shapes for multiple ascending shapes and list should remain the same order"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        circle_two = ShapeFactory.create_shape("Circle", 2.0)
        circle_three = ShapeFactory.create_shape("Circle", 3.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        drawing_program.add_shape(circle_three)
        drawing_program.sort_shapes()
        expect_list = [circle_one, circle_two, circle_three]
        self.assertEqual(expect_list, drawing_program.list_of_shapes, "ascending shape list after sort not as remain the same order")


    def test_sort_shapes_for_multiple_descending_shapes(self):
        """Tests sort shapes for multiple descending shapes and list should be sort to ascending order"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
        drawing_program.add_shape(square_one)
        drawing_program.add_shape(rectangle_one)
        drawing_program.add_shape(circle_one)
        drawing_program.sort_shapes()
        expect_list = [circle_one, rectangle_one, square_one]
        self.assertEqual(expect_list, drawing_program.list_of_shapes, "descending shape list after sort not as remain the expected ascending order")

    def test_sort_shapes_for_multiple_random_shapes(self):
        """Tests sort shapes for multiple random shapes and list should be sort to ascending order"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
        triangle_one = ShapeFactory.create_shape("Triangle", 2.0, 3.0, 4.0)
        drawing_program.add_shape(rectangle_one)
        drawing_program.add_shape(square_one)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(triangle_one)
        drawing_program.sort_shapes()
        expect_list = [circle_one, rectangle_one, square_one, triangle_one]
        self.assertEqual(expect_list, drawing_program.list_of_shapes, "random shape list after sort not as remain the expected ascending order")

    def test_to_str(self):
        """Tests __str__ method should convert DrawingProgram to expected string"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(square_one)
        expect_string = "Circle, area: 12.566370614359172, perimeter: 12.566370614359172\nSquare, area: 4.0, perimeter: 8.0"
        self.assertEqual(expect_string, drawing_program.__str__(), "test to str is not as expected string")

    def test_get_shape_valid_index(self):
        """Test get shape method with valid index should get expected shape"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(square_one)
        self.assertEqual(square_one, drawing_program.get_shape(1), "test get shape from valid index is not expected shape")

    def test_get_shape_invalid_index(self):
        """Test get shape method with invalid index should raise IndexError exception"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(square_one)
        try:
            drawing_program.get_shape(2)
            self.assertEqual(True, False, "exception not thrown for invalid index")
        except IndexError as index_error:
            self.assertEqual(True, True)

    def test_set_shape_valid_index(self):
        """Test set shape method with valid index should set index of the list to input shape"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        circle_two = ShapeFactory.create_shape("Circle", 2.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        drawing_program.set_shape(1, square_one)
        self.assertEqual(square_one, drawing_program.get_shape(1), "test set shape to valid index is not expected shape")

    def test_set_shape_invalid_index(self):
        """Test set shape method with invalid index should raise IndexError exception"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        circle_two = ShapeFactory.create_shape("Circle", 2.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        try:
            drawing_program.set_shape(2, square_one)
            self.assertEqual(True, False, "exception not thrown for invalid index")
        except IndexError as index_error:
            self.assertEqual(True, True)

    def test_set_shape_with_wrong_type(self):
        """Test set shape method with wrong type should raise TypeError exception"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        circle_two = ShapeFactory.create_shape("Circle", 2.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        try:
            drawing_program.set_shape(2, "square_one")
            self.assertEqual(True, False, "exception not thrown for invalid index")
        except TypeError as type_error:
            self.assertEqual(True, True)


