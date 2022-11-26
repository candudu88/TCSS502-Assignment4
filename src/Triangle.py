from src.Shape import Shape


class Triangle(Shape):
    """Concrete Triangle class implements interface Shape

       Attributes:
              _shape_name : string
              __side_1 : float
              __side_2: float
              __side_3: float
    """
    def __init__(self, *args):
        """
        This method is used to create an instance of a Triangle, creating private
        fields and initializing shape_name to Triangle, and three side from values
        passed as parameters to the method
        """
        self._shape_name = "Triangle"
        if len(args) == 3:
            if float(args[0]) + float(args[1]) > float(args[2]) and float(args[0]) + float(args[2]) > float(args[1]) and float(args[1]) + float(args[2]) > float(args[0]):
                self.__side_1 = float(args[0])
                self.__side_2 = float(args[1])
                self.__side_3 = float(args[2])
            else:
                raise TypeError("Input three side can't form a triangle")
        else:
            raise TypeError("Input arguments number is wrong for create a triangle")

    def area(self):
        """
        This method calculate the area of triangle
        :return: float
        """
        s = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        return (s*(s-self.__side_1)*(s-self.__side_2)*(s-self.__side_3)) ** 0.5

    def perimeter(self):
        """
        This method calculate the perimeter of triangle
        :return: float
        """
        return self.__side_1 + self.__side_2 + self.__side_3




