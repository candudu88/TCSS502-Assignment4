from Shape import Shape


class Square(Shape):
    def __init__(self, name_of_shape, side):
        super().__init__(name_of_shape)
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side

    def draw(self):
        print(str(self))

    def __str__(self):
        return f"{self.get_name()}, area: {self.area()}, perimeter: {self.perimeter()}"
