from abc import ABC

from Shape import Shape


class DrawingProgram(Shape):

    def __init__(self):
        self.list_of_shapes = []

    def add_shape(self, shape):
        self.list_of_shapes.append(shape)
        pass

    def remove_shape(self):
        pass

    def print_shape(self):
        pass

    def sort_shapes(self):
        pass

    def __str__(self):
        pass

    def get_shape(self, index):
        pass

    def set_shape(self, index, shape):
        pass