from abc import ABC

from Shape import Shape


class DrawingProgram():

    def __init__(self):
        self.list_of_shapes = []

    def add_shape(self, shape):
        self.list_of_shapes.append(shape)


    def remove_shape(self):
        self.list_of_shapes.remove()

    def print_shape(self):
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