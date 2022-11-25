#from src.Shape import Shape
from Shape import Shape
#from src.DrawingProgramIterator import DrawingProgramIterator
from DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:
    def __init__(self, list=None):
        if list is None:
            self.list_of_shapes = []
        else:
            self.list_of_shapes = list
        self._size = len(self.list_of_shapes)

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.list_of_shapes.append(shape)
            self._size += 1
        else:
            raise TypeError("adding wrong type of object")

    def remove_shape(self, shape):
        to_remove_shape_list = [];
        for idx in range(len(self.list_of_shapes)):
            if type(self.list_of_shapes[idx]) == type(shape):
                to_remove_shape_list.append(self.list_of_shapes[idx])
        for item in to_remove_shape_list:
            self.list_of_shapes.remove(item)
        self._size -= len(to_remove_shape_list)
        return len(to_remove_shape_list)

    def print_shape(self, shape):
        for item in self.list_Of_Shape:
            if isinstance(item, type(shape)):
                print(item)

    def sort_shapes(self):
        self.list_of_shapes.sort()

    def __str__(self):
        str_of_shapes = ""
        for shape in self.list_of_shapes:
            str_of_shapes += str(shape) + "\n"
        return str_of_shapes

    def get_shape(self, index):
        return self.list_of_shapes[index]

    def set_shape(self, index, shape):
        self.list_of_shapes[index] = shape

    def __iter__(self):  # to make Drawing_Program iterable added __iter__ method.
        return DrawingProgramIterator(self.list_of_shapes)
