from src.Shape import Shape


class Square(Shape):
    """Concrete Square class implements interface Shape

       Attributes:
              __shape_name : string
              __side : float
    """
    def __init__(self, *args):
        """
        This method is used to create an instance of a Square, creating private
        fields and initializing shape_name to Square, and side from
        values passed as parameters to the method
        """
        self._shape_name = "Square"
        if len(args) == 1:
            self.__side = float(args[0])
        else:
            raise TypeError("Input arguments number is wrong for create a square")

    def area(self):
        """
        This method calculate the area of square
        :return: float
        """
        return self.__side * self.__side

    def perimeter(self):
        """
        This method calculate the perimeter of square
        :return: float
        """
        return 4 * self.__side

