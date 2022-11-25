from abc import ABC, abstractmethod


class Shape(ABC):
    """Interface for shape objects, declares area method and perimeter method"""
    def __init__(self, shape_name):
        self._shape_name = shape_name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        """
        Call to string method converts object to string
        :return:
        """
        print(self.__str__())

    @property
    def name(self):
        return self._shape_name

    def __str__(self):
        """
        Converts field values to strings and formats the values.
        :return: String containing the name, area and perimeter
        """
        return f'{self.name}, area: {self.area()}, perimeter: {self.perimeter()}'

    def __eq__(self, other_shape):
        """
        Compares two shape objects, if shape_name and area both equal will return True otherwise return False
        :param other_shape: Other shape to compare too.
        :return: boolean indicating whether this object is equal to the other.
        """
        if self._shape_name == other_shape._shape_name:
            return self.area() == other_shape.area()
        else:
            return False

    def __lt__(self, other_shape):
        """
        Compares two shape objects by name, if the shape_name are the same, then compares area. otherwise only compare the shape_name.
        :param other_shape: other shape to compare too.
        :return: boolean indicating whether this object is less than the other.
        """
        if self._shape_name == other_shape._shape_name:
            return self.area() < other_shape.area()
        else:
            return self._shape_name < other_shape._shape_name












