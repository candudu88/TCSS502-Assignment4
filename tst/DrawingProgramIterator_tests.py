import unittest

from src.DrawingProgram import DrawingProgram
from src.ShapeFactory import ShapeFactory


class DrawingProgramIteratorTest(unittest.TestCase):
    """
    This class tests functionality DrawingProgramIterator class.
    """
    def test_iterator_no_shapes(self):
        """Test created DrawingProgram can be looped through for no shape case"""
        drawing_program = DrawingProgram()
        iter_1 = drawing_program.__iter__()
        for item in drawing_program:
            self.assertEqual(item, next(iter_1), "test for loop through drawing_program not equal expected next item")


    def test_iterator_with_one_shapes(self):
        """Test created DrawingProgram can be looped through for one shape case"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1.0)
        drawing_program.add_shape(circle_one)
        iter_2 = drawing_program.__iter__()
        for item in drawing_program:
            self.assertEqual(item, next(iter_2), "test for loop through drawing_program not equal expected next item")

    def test_iterator_with_five_shapes(self):
        """Test created DrawingProgram can be looped through for five shape case"""
        drawing_program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 3.0)
        circle_two = ShapeFactory.create_shape("Circle", 1.0)
        square_one = ShapeFactory.create_shape("Square", 2.0)
        rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
        triangle_one = ShapeFactory.create_shape("Triangle", 2.0, 3.0, 4.0)
        drawing_program.add_shape(circle_one)
        drawing_program.add_shape(circle_two)
        drawing_program.add_shape(square_one)
        drawing_program.add_shape(rectangle_one)
        drawing_program.add_shape(triangle_one)
        iter_3 = drawing_program.__iter__()
        for item in drawing_program:
            self.assertEqual(item, next(iter_3), "test for-loop through drawing_program not equal to expected next item")