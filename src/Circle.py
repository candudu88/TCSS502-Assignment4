from src.Shape import Shape
from math import pi


class Circle(Shape):
    """Concrete Circle class implements interface Shape

       Attributes:
              _shape_name : string
              __radius : float
    """
    def __init__(self, *args):
        """
        This method is used to create an instance of a Circle, creating private
        fields and initializing shape_name to Circle, and radius from
        values passed as parameters to the method
        """
        self._shape_name = "Circle"
        if len(args) == 1:
            self.__radius = float(args[0])
        else:
            raise TypeError("Input arguments number is wrong for create a circle")

    def area(self):
        """
        This method calculate the area of circle
        :return: float
        """
        return pi * self.__radius * self.__radius

    def perimeter(self):
        """
        This method calculate the perimeter of circle
        :return: float
        """
        return 2.0 * pi * self.__radius
