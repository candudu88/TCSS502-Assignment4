from src.Shape import Shape
from src.DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:
    """DrawingProgram class represent an drawing program to collection all created shape object
    and implement add_shape, remove_shape, print_shape, sort_shapes, get_shape, set_shape methods

       Attributes:
              list_of_shapes : []
              _size : int
    """
    def __init__(self, list_of_shapes=None):
        """Constructs all the necessary attributes for the DrawingProgram object."""
        if list_of_shapes is None:
            self.list_of_shapes = []
        else:
            self.list_of_shapes = list_of_shapes
        self._size = len(self.list_of_shapes)

    def add_shape(self, shape):
        """
        This method add a valid shape to DrawingProgram object, otherwise raise TypeError exception
        :param shape: shape to add
        :return: None
        """
        if isinstance(shape, Shape):
            self.list_of_shapes.append(shape)
            self._size += 1
        else:
            raise TypeError("adding wrong type of object")

    def remove_shape(self, shape):
        """
        This method remove shape that match input valid type from list and return correct count of removed item,
        otherwise should not remove any item
        :param shape: shape type to remove
        :return: int
        """
        to_remove_shape_list = [];
        for idx in range(len(self.list_of_shapes)):
            if type(self.list_of_shapes[idx]) == type(shape):
                to_remove_shape_list.append(self.list_of_shapes[idx])
        for item in to_remove_shape_list:
            self.list_of_shapes.remove(item)
        self._size -= len(to_remove_shape_list)
        return len(to_remove_shape_list)

    def print_shape(self, shape):
        """
        This method print shape that match input valid type from list, otherwise should not print any items
        :param shape: shape type to print
        :return: None
        """
        for item in self.list_of_shapes:
            if isinstance(item, type(shape)):
                print(item)

    def sort_shapes(self):
        """
        This method sort all shapes. it will be sorted first by name, then by area if names are same
        :return: None
        """
        self.list_of_shapes.sort()

    def __str__(self):
        """
        this method overrides the version from the object class and is called when you print a DrawingProgram
        :return: String
        """
        str_of_shapes = ""
        for shape in self.list_of_shapes:
            str_of_shapes += str(shape) + "\n"
        return str_of_shapes.strip()

    def get_shape(self, index):
        """
        This method get shape with valid index otherwise raise IndexError exception
        :param index: int
        :return: Shape
        """
        return self.list_of_shapes[index]

    def set_shape(self, index, shape):
        """
        This method set shape with valid index otherwise raise IndexError exception
        :param index: int
        :param shape: shape to set
        :return: None
        """
        if isinstance(shape, Shape):
            self.list_of_shapes[index] = shape
        else:
            raise TypeError("set wrong type of object")

    def __iter__(self):
        """
        this method overrides the version from the object class and is called when you loop through DrawingProgram object
        :return: None
        """
        return DrawingProgramIterator(self.list_of_shapes)
