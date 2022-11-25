import unittest

from src.DrawingProgram import DrawingProgram
from src.ShapeFactory import ShapeFactory


class DrawingProgram_tests(unittest.TestCase):

    def test_init_default_list(self):
        drawing_program = DrawingProgram()
        self.assertEqual([], drawing_program.list_of_shapes, "default list not set to empty list")

    def test_init_with_shape_list(self):
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        circle_two = ShapeFactory.create_shape("Circle", 3.0)
        circle_three = ShapeFactory.create_shape("Circle", 1.0)
        shape_list = [circle_one, circle_two, circle_three]
        drawing_program = DrawingProgram(shape_list)
        self.assertEqual(shape_list, drawing_program.list_of_shapes, "default list not set to input list")

    def test_add_shape_to_list(self):
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 2.0)
        drawing_program.add_shape(circle_one)
        self.assertEqual(1, drawing_program._size, "list size not as expected after added one shape to it")

    def test_add_wrong_type_to_list(self):
        drawing_program = DrawingProgram()
        try:
            drawing_program.add_shape("circle_test_string")
        except TypeError as type_error:
            self.assertEqual(True, True)



