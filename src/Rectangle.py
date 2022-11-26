from src.Shape import Shape


class Rectangle(Shape):
    """Concrete Rectangle class implements interface Shape

       Attributes:
              _shape_name : string
              __length : float
              __width : float
    """

    def __init__(self, *args):
        """
        This method is used to create an instance of a Rectangle, creating private
        fields and initializing shape_name to Rectangle, length and
        width from values passed as parameters to the method
        """
        self._shape_name = "Rectangle"
        if len(args) == 2:
            self.__length = float(args[0])
            self.__width = float(args[1])
        else:
            raise TypeError("Input arguments number is wrong for create a rectangle")

    def area(self):
        """
        This method calculate the area of rectangle
        :return: float
        """
        return self.__length * self.__width

    def perimeter(self):
        """
        This method calculate the perimeter of rectangle
        :return: float
        """
        return self.__length * 2 + self.__width * 2

