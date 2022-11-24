from abc import ABC

from Shape import Shape
from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
from ShapeFactory import ShapeFactory


class DrawingProgram():

    def __init__(self):
        self.list_of_shapes = []

    def add_shape(self, shape):
        self.list_of_shapes.append(shape)

    def remove_shape(self, shape):
        self.list_of_shapes.remove(shape)

    def print_shape(self, shape):
        pass

    def sort_shapes(self):
        pass

    def __str__(self):
        for shape in self.list_of_shapes:
            shape.draw()

    def get_shape(self, index):
        pass

    def set_shape(self, index, shape):
        pass





cir = ShapeFactory.create_shape("Circle", 2.0)
rec = ShapeFactory.create_shape("Rectangle", 2, 4)
sqr = ShapeFactory.create_shape("Square", 3)
print(type(cir))
dp = DrawingProgram()
dp.add_shape(cir)
dp.add_shape(cir)
dp.add_shape(rec)
dp.add_shape(sqr)
dp.remove_shape(cir)
print(cir)
